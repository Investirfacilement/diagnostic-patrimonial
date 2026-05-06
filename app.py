import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

import scoring as sc
import claude_service as claude
import pdf_generator as pdf_gen
import email_service as email_svc

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", questions=sc.QUESTIONS)


@app.route("/submit", methods=["POST"])
def submit():
    data    = request.get_json()
    prenom  = data.get("prenom", "").strip()
    email   = data.get("email", "").strip()
    answers = data.get("answers", {})

    if not prenom or not email:
        return jsonify({"error": "Prénom et email requis"}), 400

    try:
        # 1. Scoring
        scores  = sc.compute_scores(answers)
        profile = sc.get_profile(scores["total"])

        # 2. Projection
        monthly  = sc.get_monthly_savings_from_answers(answers)
        horizon  = sc.get_horizon_from_answers(answers)
        proj     = sc.compute_projection(monthly, horizon)

        # 3. Textes Claude
        insights = claude.generate_insights(prenom, scores, answers, profile)

        # 4. Génération PDF
        context  = pdf_gen.build_context(prenom, email, scores, profile, insights, proj)
        pdf_path = pdf_gen.generate_pdf(context)

        # 5. Emails
        email_svc.send_diagnostic(email, prenom, pdf_path)
        email_svc.notify_advisor(prenom, email, profile["name"], scores["total"])

        return jsonify({
            "success": True,
            "score":   scores["total"],
            "profile": profile["name"],
        })

    except Exception as exc:
        app.logger.error(f"Erreur diagnostic : {exc}", exc_info=True)
        return jsonify({"error": "Une erreur est survenue, veuillez réessayer."}), 500


@app.route("/merci")
def merci():
    return render_template("merci.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
