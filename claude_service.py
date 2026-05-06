import anthropic
import os
import json
import re

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

SYSTEM = """Tu es un conseiller en gestion de patrimoine expert, pédagogue et bienveillant.
Tu analyses un profil financier et génères des textes courts, personnalisés, professionnels.
Ton style : rassurant, direct, sans jargon inutile, sans promesse de rendement.
Réponds TOUJOURS en JSON valide, sans texte autour."""


def generate_insights(prenom: str, scores: dict, answers: dict, profile: dict) -> dict:
    block_labels = {
        1: "Sécurité financière",
        2: "Capacité d'investissement",
        3: "Objectifs patrimoniaux",
        4: "Maturité investisseur",
    }
    block_summary = "\n".join(
        f"- {block_labels[b]} : {scores['blocks'][b]}/25"
        for b in range(1, 5)
    )

    prompt = f"""Profil de {prenom} :
Score total : {scores['total']}/100
Profil : {profile['name']}
{block_summary}

Génère exactement ce JSON :
{{
  "points_forts": ["<point fort 1>", "<point fort 2>", "<point fort 3>"],
  "vigilances": [
    {{"niveau": "orange"|"rouge", "texte": "<point de vigilance 1>"}},
    {{"niveau": "orange"|"rouge", "texte": "<point de vigilance 2>"}},
    {{"niveau": "orange"|"rouge", "texte": "<point de vigilance 3>"}}
  ],
  "priorites": [
    {{"titre": "<titre court>", "description": "<2-3 lignes max>"}},
    {{"titre": "<titre court>", "description": "<2-3 lignes max>"}},
    {{"titre": "<titre court>", "description": "<2-3 lignes max>"}}
  ],
  "conclusion": "<2 phrases personnalisées pour {prenom}, bienveillantes, qui donnent envie d'aller plus loin>"
}}

Règles :
- Points forts : vrais points positifs du profil, pas génériques
- Vigilances : orange = à améliorer, rouge = prioritaire
- Priorités : rester général, ne jamais nommer de produit financier précis
- Conclusion : mentionner le prénom, ton chaleureux mais professionnel"""

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = msg.content[0].text
    json_match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not json_match:
        raise ValueError(f"Réponse Claude invalide : {raw}")
    return json.loads(json_match.group())
