import os
import requests


def send_diagnostic(to_email: str, prenom: str, pdf_path: str) -> None:
    """Envoie le PDF du diagnostic au prospect via Brevo."""
    import base64

    with open(pdf_path, "rb") as f:
        pdf_b64 = base64.b64encode(f.read()).decode()

    filename = os.path.basename(pdf_path)
    advisor  = os.environ.get("ADVISOR_NAME", "Votre conseiller")
    calendly = os.environ.get("CALENDLY_URL", "#")

    payload = {
        "sender": {
            "name":  advisor,
            "email": os.environ["BREVO_SENDER_EMAIL"],
        },
        "to": [{"email": to_email, "name": prenom}],
        "subject": f"{prenom}, votre diagnostic patrimonial personnalisé est prêt",
        "htmlContent": f"""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;color:#1a1a2e">
  <div style="background:#1a1a2e;padding:32px;text-align:center">
    <h1 style="color:#fff;margin:0;font-size:22px">Votre diagnostic patrimonial</h1>
  </div>
  <div style="padding:32px">
    <p style="font-size:16px">Bonjour <strong>{prenom}</strong>,</p>
    <p>Merci d'avoir complété le questionnaire. Votre diagnostic patrimonial personnalisé
    est disponible en pièce jointe.</p>
    <p>Ce document vous donne une première lecture claire de votre situation financière
    et de vos priorités d'investissement.</p>
    <div style="text-align:center;margin:32px 0">
      <a href="{calendly}"
         style="background:#4361ee;color:#fff;padding:14px 28px;border-radius:8px;
                text-decoration:none;font-weight:bold;font-size:15px">
        Réserver un échange gratuit de 30 min
      </a>
    </div>
    <p style="color:#666;font-size:13px">
      Ce diagnostic ne constitue pas un conseil personnalisé en investissement.
      Il sert à identifier vos grandes priorités patrimoniales.
    </p>
    <p>À très bientôt,<br><strong>{advisor}</strong></p>
  </div>
</div>
""",
        "attachment": [{"name": filename, "content": pdf_b64}],
    }

    resp = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        json=payload,
        headers={
            "api-key":      os.environ["BREVO_API_KEY"],
            "content-type": "application/json",
        },
        timeout=30,
    )
    resp.raise_for_status()


def notify_advisor(prenom: str, email: str, profile_name: str, total: int) -> None:
    """Notifie le conseiller qu'un nouveau diagnostic a été généré."""
    advisor_email = os.environ.get("ADVISOR_EMAIL", os.environ["BREVO_SENDER_EMAIL"])
    advisor_name  = os.environ.get("ADVISOR_NAME", "Conseiller")
    calendly      = os.environ.get("CALENDLY_URL", "#")

    payload = {
        "sender": {"name": advisor_name, "email": os.environ["BREVO_SENDER_EMAIL"]},
        "to": [{"email": advisor_email}],
        "subject": f"🔔 Nouveau diagnostic — {prenom} ({total}/100 · {profile_name})",
        "htmlContent": f"""
<div style="font-family:Arial,sans-serif;max-width:500px;margin:auto">
  <h2>Nouveau prospect qualifié</h2>
  <table style="width:100%;border-collapse:collapse">
    <tr><td style="padding:8px;color:#666">Prénom</td><td><strong>{prenom}</strong></td></tr>
    <tr><td style="padding:8px;color:#666">Email</td><td>{email}</td></tr>
    <tr><td style="padding:8px;color:#666">Score</td><td><strong>{total}/100</strong></td></tr>
    <tr><td style="padding:8px;color:#666">Profil</td><td><strong>{profile_name}</strong></td></tr>
  </table>
  <p style="margin-top:24px">
    <a href="{calendly}" style="background:#4361ee;color:#fff;padding:10px 20px;
       border-radius:6px;text-decoration:none">Voir Calendly</a>
  </p>
</div>
""",
    }

    resp = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        json=payload,
        headers={
            "api-key":      os.environ["BREVO_API_KEY"],
            "content-type": "application/json",
        },
        timeout=30,
    )
    resp.raise_for_status()
