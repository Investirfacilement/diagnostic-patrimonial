import os
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def _get_smtp():
    return {
        "host":     os.environ.get("SMTP_HOST", "smtp-relay.brevo.com"),
        "port":     int(os.environ.get("SMTP_PORT", 587)),
        "login":    os.environ["SMTP_LOGIN"],
        "password": os.environ["SMTP_PASSWORD"],
        "sender":   os.environ["SMTP_SENDER_EMAIL"],
    }


def _send(to_email: str, to_name: str, subject: str, html: str, pdf_path: str = None) -> None:
    cfg = _get_smtp()

    msg = MIMEMultipart("mixed")
    msg["From"]    = f"{os.environ.get('ADVISOR_NAME', 'Conseiller')} <{cfg['sender']}>"
    msg["To"]      = f"{to_name} <{to_email}>"
    msg["Subject"] = subject

    msg.attach(MIMEText(html, "html", "utf-8"))

    if pdf_path and os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(pdf_path)}",
        )
        msg.attach(part)

    with smtplib.SMTP(cfg["host"], cfg["port"]) as server:
        server.ehlo()
        server.starttls()
        server.login(cfg["login"], cfg["password"])
        server.sendmail(cfg["sender"], to_email, msg.as_string())


def send_diagnostic(to_email: str, prenom: str, pdf_path: str) -> None:
    advisor   = os.environ.get("ADVISOR_NAME", "Votre conseiller")
    calendly  = os.environ.get("CALENDLY_URL", "#")

    html = f"""
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
"""
    _send(to_email, prenom, f"{prenom}, votre diagnostic patrimonial est prêt", html, pdf_path)


def notify_advisor(prenom: str, email: str, profile_name: str, total: int) -> None:
    advisor_email = os.environ.get("ADVISOR_EMAIL", os.environ["SMTP_SENDER_EMAIL"])
    advisor_name  = os.environ.get("ADVISOR_NAME", "Conseiller")
    calendly      = os.environ.get("CALENDLY_URL", "#")

    html = f"""
<div style="font-family:Arial,sans-serif;max-width:500px;margin:auto">
  <h2>🔔 Nouveau prospect qualifié</h2>
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
"""
    _send(advisor_email, advisor_name,
          f"🔔 Nouveau diagnostic — {prenom} ({total}/100 · {profile_name})",
          html)
