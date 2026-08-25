from google.oauth2.service_account import Credentials
import gspread

def connect_sheet():

    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    return client

def write_to_sheet(sheet, products):

    sheet.clear()

    rows = [
        ["Title", "Price", "Rating", "Reviews", "Link"]
    ]

    for product in products:
        rows.append([
            product["title"],
            product["price"],
            product["rating"],
            product["reviews"],
            product["link"]
        ])

    sheet.update("A1", rows)