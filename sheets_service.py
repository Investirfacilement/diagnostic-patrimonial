import os
import json
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

SCOPES    = ["https://www.googleapis.com/auth/spreadsheets"]
SHEET_ID  = "146p3MagmL0_WAxDl0I5CYXBBKxj7OfF5gg-m6hNF1_M"
HEADERS   = ["Date", "Prénom", "Email", "Score", "Profil"]


def _get_sheet():
    creds_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not creds_json:
        raise RuntimeError("GOOGLE_SERVICE_ACCOUNT_JSON non défini")
    creds = Credentials.from_service_account_info(json.loads(creds_json), scopes=SCOPES)
    client = gspread.authorize(creds)
    return client.open_by_key(SHEET_ID).sheet1


def log_prospect(prenom: str, email: str, score: int, profile_name: str) -> None:
    sheet = _get_sheet()
    if sheet.row_count == 0 or sheet.cell(1, 1).value != "Date":
        sheet.insert_row(HEADERS, 1)
    sheet.append_row([
        datetime.now().strftime("%d/%m/%Y %H:%M"),
        prenom,
        email,
        score,
        profile_name,
    ])
