from services.sheet_writer import connect_sheet, write_to_sheet

client = connect_sheet()

sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1ZtFw6fbg3V80ezB1-yI-AOA_tFuRSmR47w9uq-R88Rg/edit?gid=0#gid=0"
).sheet1

products = [
    {
        "title": "Test Product",
        "price": 99,
        "rating": 4.5,
        "reviews": 100,
        "link": "https://example.com"
    }
]

write_to_sheet(sheet, products)

print("Success")