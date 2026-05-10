import os
from datetime import date
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates", "pdf")
OUTPUT_DIR   = os.path.join(os.path.dirname(__file__), "generated")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def generate_pdf(context: dict) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    template = env.get_template("diagnostic.html")
    html_content = template.render(**context)

    prenom_clean = context.get("prenom", "prospect").replace(" ", "_")
    filename = f"diagnostic_{prenom_clean}_{date.today().isoformat()}.pdf"
    output_path = os.path.join(OUTPUT_DIR, filename)

    HTML(string=html_content).write_pdf(output_path)

    return output_path


def build_context(prenom: str, email: str, scores: dict, profile: dict,
                  insights: dict, projection: dict) -> dict:
    from scoring import get_block_color, BLOCKS

    block_colors = {b: get_block_color(scores["blocks"][b]) for b in range(1, 5)}

    color_map = {
        "green":  "#06d6a0",
        "orange": "#f77f00",
        "red":    "#d62828",
    }
    block_hex = {b: color_map[block_colors[b]] for b in range(1, 5)}

    score_label_map = {
        range(0, 41):   ("Bases à sécuriser",       "#d62828"),
        range(41, 61):  ("Situation à structurer",   "#f77f00"),
        range(61, 81):  ("Bon potentiel patrimonial","#4361ee"),
        range(81, 101): ("Optimisation avancée",     "#06d6a0"),
    }
    score_label, score_color = "—", "#333"
    for r, (lbl, col) in score_label_map.items():
        if scores["total"] in r:
            score_label, score_color = lbl, col
            break

    return {
        "prenom":       prenom,
        "email":        email,
        "date_str":     date.today().strftime("%d/%m/%Y"),
        "scores":       scores,
        "blocks":       BLOCKS,
        "block_colors": block_colors,
        "block_hex":    block_hex,
        "profile":      profile,
        "insights":     insights,
        "projection":   projection,
        "score_label":  score_label,
        "score_color":  score_color,
        "calendly_url": os.environ.get("CALENDLY_URL", "#"),
        "advisor_name": os.environ.get("ADVISOR_NAME", "Votre conseiller"),
    }
