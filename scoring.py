"""
Système de scoring du diagnostic patrimonial.
4 blocs × 25 points = 100 points au total.
"""

BLOCKS = {
    1: "Sécurité financière",
    2: "Capacité d'investissement",
    3: "Objectifs patrimoniaux",
    4: "Maturité investisseur",
}

QUESTIONS = [
    # ── Bloc 1 — Sécurité financière ────────────────────────────────
    {
        "id": "q1", "block": 1,
        "text": "Combien de mois de dépenses couvre votre épargne de précaution ?",
        "answers": [
            {"text": "Je n'en ai pas", "points": 0},
            {"text": "Moins d'1 mois", "points": 1},
            {"text": "1 à 3 mois", "points": 2},
            {"text": "3 à 6 mois", "points": 3},
            {"text": "Plus de 6 mois", "points": 4},
        ],
    },
    {
        "id": "q2", "block": 1,
        "text": "Avez-vous des dettes coûteuses (crédit conso, découvert récurrent…) ?",
        "answers": [
            {"text": "Oui, plusieurs", "points": 0},
            {"text": "Oui, une seule", "points": 1},
            {"text": "Non, seulement un crédit immobilier", "points": 3},
            {"text": "Non, aucune dette", "points": 4},
        ],
    },
    {
        "id": "q3", "block": 1,
        "text": "Votre budget mensuel est-il globalement maîtrisé ?",
        "answers": [
            {"text": "Non, je suis souvent dans le rouge", "points": 0},
            {"text": "Je m'en sors juste", "points": 1},
            {"text": "Oui, avec peu de marge", "points": 2},
            {"text": "Oui, avec une bonne marge", "points": 4},
        ],
    },
    {
        "id": "q4", "block": 1,
        "text": "Seriez-vous à l'abri financièrement en cas de perte d'emploi pendant 3 mois ?",
        "answers": [
            {"text": "Non", "points": 0},
            {"text": "Difficilement", "points": 1},
            {"text": "Oui", "points": 3},
            {"text": "Oui, et bien au-delà", "points": 4},
        ],
    },
    {
        "id": "q5", "block": 1,
        "text": "Avez-vous une couverture prévoyance (décès, invalidité) ?",
        "answers": [
            {"text": "Non, aucune", "points": 0},
            {"text": "Uniquement celle de mon employeur", "points": 2},
            {"text": "Oui, une prévoyance complémentaire", "points": 3},
            {"text": "Oui, une couverture complète et révisée", "points": 4},
        ],
    },
    {
        "id": "q6", "block": 1,
        "text": "Quelle part de vos revenus représentent vos charges fixes (loyer, crédits…) ?",
        "answers": [
            {"text": "Plus de 60 %", "points": 0},
            {"text": "Entre 50 et 60 %", "points": 1},
            {"text": "Entre 35 et 50 %", "points": 3},
            {"text": "Moins de 35 %", "points": 4},
        ],
    },

    # ── Bloc 2 — Capacité d'investissement ──────────────────────────
    {
        "id": "q7", "block": 2,
        "text": "Quelle est votre capacité d'épargne mensuelle actuelle ?",
        "answers": [
            {"text": "Nulle ou négative", "points": 0},
            {"text": "Moins de 100 €", "points": 1},
            {"text": "100 à 300 €", "points": 2},
            {"text": "300 à 800 €", "points": 3},
            {"text": "Plus de 800 €", "points": 4},
        ],
    },
    {
        "id": "q8", "block": 2,
        "text": "Avez-vous un capital disponible à investir aujourd'hui ?",
        "answers": [
            {"text": "Non", "points": 0},
            {"text": "Moins de 5 000 €", "points": 1},
            {"text": "5 000 à 20 000 €", "points": 2},
            {"text": "20 000 à 50 000 €", "points": 3},
            {"text": "Plus de 50 000 €", "points": 4},
        ],
    },
    {
        "id": "q9", "block": 2,
        "text": "Quelle est votre situation professionnelle ?",
        "answers": [
            {"text": "Situation instable / sans emploi", "points": 0},
            {"text": "CDD ou mission", "points": 1},
            {"text": "CDI ou fonctionnaire", "points": 3},
            {"text": "Indépendant / chef d'entreprise avec revenus stables", "points": 4},
        ],
    },
    {
        "id": "q10", "block": 2,
        "text": "Votre revenu est-il susceptible d'augmenter dans les 3 prochaines années ?",
        "answers": [
            {"text": "Non, plutôt en baisse", "points": 0},
            {"text": "Stable", "points": 2},
            {"text": "Probablement oui", "points": 3},
            {"text": "Très certainement (promotion, projet…)", "points": 4},
        ],
    },
    {
        "id": "q11", "block": 2,
        "text": "Avez-vous des projets de dépenses importants dans les 2 prochaines années ?",
        "answers": [
            {"text": "Oui, très importants (achat immo, mariage, bébé…)", "points": 0},
            {"text": "Oui, modérés", "points": 2},
            {"text": "Non, situation stable", "points": 4},
        ],
    },
    {
        "id": "q12", "block": 2,
        "text": "Investissez-vous déjà régulièrement, même un petit montant ?",
        "answers": [
            {"text": "Non, jamais", "points": 0},
            {"text": "Ponctuellement", "points": 1},
            {"text": "Oui, de façon irrégulière", "points": 2},
            {"text": "Oui, tous les mois, automatiquement", "points": 4},
        ],
    },

    # ── Bloc 3 — Objectifs patrimoniaux ─────────────────────────────
    {
        "id": "q13", "block": 3,
        "text": "Quel est votre objectif patrimonial principal ?",
        "answers": [
            {"text": "Je n'en ai pas vraiment défini", "points": 0},
            {"text": "Mettre de l'argent de côté sans objectif précis", "points": 1},
            {"text": "Préparer ma retraite / générer des revenus complémentaires", "points": 3},
            {"text": "Investir dans l'immobilier ou développer un patrimoine", "points": 3},
            {"text": "Optimiser ma fiscalité ou préparer une transmission", "points": 4},
        ],
    },
    {
        "id": "q14", "block": 3,
        "text": "Quel est votre horizon d'investissement ?",
        "answers": [
            {"text": "Court terme (moins de 3 ans)", "points": 0},
            {"text": "Moyen terme (3 à 7 ans)", "points": 2},
            {"text": "Long terme (7 à 15 ans)", "points": 3},
            {"text": "Très long terme (plus de 15 ans)", "points": 4},
        ],
    },
    {
        "id": "q15", "block": 3,
        "text": "Avez-vous une vision claire de vos objectifs financiers ?",
        "answers": [
            {"text": "Non, je ne sais pas vraiment où je vais", "points": 0},
            {"text": "Quelques idées vagues", "points": 1},
            {"text": "Une direction relativement claire", "points": 2},
            {"text": "Oui, avec un plan en tête", "points": 4},
        ],
    },
    {
        "id": "q16", "block": 3,
        "text": "Avez-vous commencé à préparer votre retraite ?",
        "answers": [
            {"text": "Non, c'est trop loin", "points": 0},
            {"text": "J'y pense mais n'ai rien mis en place", "points": 1},
            {"text": "Oui, j'ai commencé à épargner", "points": 3},
            {"text": "Oui, avec un dispositif dédié (PER, assurance vie…)", "points": 4},
        ],
    },
    {
        "id": "q17", "block": 3,
        "text": "Avez-vous des proches à protéger financièrement ?",
        "answers": [
            {"text": "Non", "points": 2},
            {"text": "Oui, sans protection mise en place", "points": 0},
            {"text": "Oui, avec une protection partielle", "points": 2},
            {"text": "Oui, avec une protection complète", "points": 4},
        ],
    },
    {
        "id": "q18", "block": 3,
        "text": "Êtes-vous propriétaire de votre résidence principale ?",
        "answers": [
            {"text": "Non et pas de projet", "points": 1},
            {"text": "Non, mais projet dans les 3 ans", "points": 2},
            {"text": "Oui, avec crédit en cours", "points": 3},
            {"text": "Oui, crédit remboursé", "points": 4},
        ],
    },

    # ── Bloc 4 — Maturité investisseur ──────────────────────────────
    {
        "id": "q19", "block": 4,
        "text": "Avez-vous déjà investi dans des produits financiers ?",
        "answers": [
            {"text": "Non, jamais", "points": 0},
            {"text": "Livret A / LDDS uniquement", "points": 1},
            {"text": "Assurance vie ou PEA", "points": 2},
            {"text": "Plusieurs enveloppes différentes", "points": 3},
            {"text": "Bourse, immobilier, placements divers", "points": 4},
        ],
    },
    {
        "id": "q20", "block": 4,
        "text": "Si votre placement perdait 20 % en 6 mois, que feriez-vous ?",
        "answers": [
            {"text": "Je panique et vends tout", "points": 0},
            {"text": "Je m'inquiète mais j'attends", "points": 1},
            {"text": "Je conserve calmement", "points": 3},
            {"text": "J'en profite pour investir davantage", "points": 4},
        ],
    },
    {
        "id": "q21", "block": 4,
        "text": "Connaissez-vous la différence entre PEA, assurance vie et PER ?",
        "answers": [
            {"text": "Non", "points": 0},
            {"text": "Vaguement", "points": 1},
            {"text": "Oui, globalement", "points": 3},
            {"text": "Oui, parfaitement", "points": 4},
        ],
    },
    {
        "id": "q22", "block": 4,
        "text": "Avez-vous une stratégie d'investissement définie ?",
        "answers": [
            {"text": "Non, j'investis au hasard des opportunités", "points": 0},
            {"text": "Quelques idées sans plan structuré", "points": 1},
            {"text": "Une approche globale mais perfectible", "points": 2},
            {"text": "Une stratégie claire et cohérente", "points": 4},
        ],
    },
    {
        "id": "q23", "block": 4,
        "text": "Connaissez-vous votre taux marginal d'imposition ?",
        "answers": [
            {"text": "Non", "points": 0},
            {"text": "Vaguement", "points": 1},
            {"text": "Oui", "points": 3},
            {"text": "Oui, et je l'intègre dans mes décisions", "points": 4},
        ],
    },
    {
        "id": "q24", "block": 4,
        "text": "Avez-vous déjà consulté un professionnel du patrimoine (CGP, notaire…) ?",
        "answers": [
            {"text": "Non, jamais", "points": 0},
            {"text": "Non, mais j'y pense", "points": 1},
            {"text": "Oui, une ou deux fois", "points": 2},
            {"text": "Oui, j'ai un suivi régulier", "points": 4},
        ],
    },
]


def compute_scores(answers: dict) -> dict:
    """
    answers = {"q1": 2, "q2": 0, ...}  (index de la réponse choisie)
    Retourne les scores par bloc et le total sur 100.
    """
    raw = {1: 0, 2: 0, 3: 0, 4: 0}
    max_raw = {1: 0, 2: 0, 3: 0, 4: 0}

    for q in QUESTIONS:
        qid = q["id"]
        block = q["block"]
        max_pts = max(a["points"] for a in q["answers"])
        max_raw[block] += max_pts
        if qid in answers:
            idx = int(answers[qid])
            pts = q["answers"][idx]["points"]
            raw[block] += pts

    block_scores = {}
    for b in range(1, 5):
        block_scores[b] = round((raw[b] / max_raw[b]) * 25) if max_raw[b] else 0

    total = sum(block_scores.values())
    return {"blocks": block_scores, "total": total}


def get_profile(total: int) -> dict:
    if total <= 40:
        return {
            "num": 1,
            "name": "À sécuriser",
            "color": "#d62828",
            "icon": "🛡️",
            "message": "Avant d'investir davantage, votre priorité est de renforcer votre socle de sécurité financière. Des bases solides sont le préalable indispensable à tout investissement serein.",
        }
    elif total <= 60:
        return {
            "num": 2,
            "name": "Prêt à structurer",
            "color": "#f77f00",
            "icon": "📐",
            "message": "Vous avez déjà une base intéressante. Le vrai sujet est maintenant d'organiser votre argent avec une stratégie cohérente et des enveloppes adaptées à vos objectifs.",
        }
    elif total <= 80:
        return {
            "num": 3,
            "name": "Investisseur en construction",
            "color": "#4361ee",
            "icon": "🏗️",
            "message": "Vous êtes déjà passé à l'action. Votre enjeu est maintenant d'améliorer la cohérence, la régularité et la diversification de votre stratégie pour maximiser l'impact de vos efforts.",
        }
    else:
        return {
            "num": 4,
            "name": "Patrimoine à optimiser",
            "color": "#06d6a0",
            "icon": "⚙️",
            "message": "Votre situation mérite une approche plus fine : allocation, fiscalité, enveloppes, transmission et protection. L'optimisation est votre levier principal.",
        }


def get_block_color(score: int) -> str:
    if score >= 18:
        return "green"
    elif score >= 10:
        return "orange"
    else:
        return "red"


def compute_projection(monthly_savings: int, horizon_years: int) -> dict:
    """Calcule 3 scénarios de capitalisation (prudent / équilibré / dynamique)."""
    scenarios = {"prudent": 0.03, "equilibre": 0.06, "dynamique": 0.09}
    result = {}
    n = horizon_years * 12
    for name, rate in scenarios.items():
        r = rate / 12
        if r == 0:
            fv = monthly_savings * n
        else:
            fv = monthly_savings * ((1 + r) ** n - 1) / r
        result[name] = int(fv)
    result["versements"] = monthly_savings * n
    return result


def get_monthly_savings_from_answers(answers: dict) -> int:
    """Estime l'épargne mensuelle depuis la réponse à q7."""
    q7_map = {0: 0, 1: 50, 2: 200, 3: 500, 4: 1000}
    idx = int(answers.get("q7", 0))
    return q7_map.get(idx, 200)


def get_horizon_from_answers(answers: dict) -> int:
    """Estime l'horizon en années depuis la réponse à q14."""
    q14_map = {0: 2, 1: 5, 2: 10, 3: 20}
    idx = int(answers.get("q14", 2))
    return q14_map.get(idx, 10)
