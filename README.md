# ProductScout 🔍

> Find winning Amazon products in seconds — set your filters, we handle the rest.

ProductScout lets you search and filter Amazon products by keyword, category, price, rating and reviews — and dumps everything straight into your Google Sheet. No manual searching, no copy-pasting.

![ProductScout UI](screenshot.png)

---

## How it works

1. Enter a product keyword (e.g. `yoga mat`, `led strips`)
2. Set your filters — category, max price, min rating, min reviews
3. Hit **Search & export to Google Sheets**
4. Results land in your Google Sheet instantly

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Frontend | HTML + CSS |
| Search | SerpAPI (Google Shopping results) |
| Sheets | gspread (Google Sheets API) |
| Backend | Python |

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/pushpender-at-work/Product-Research-Automation.git
cd Product-Research-Automation
pip install -r requirements.txt
```

**2. Add your API keys**

Create a `.env` file:

SERPAPI_KEY=your_serpapi_key_here


**3. Add Google Sheets credentials**

- Go to Google Cloud Console
- Create a service account → download the JSON key
- Save it as `credentials.json` in the project folder
- Share your Google Sheet with the service account email

**4. Run**
```bash
python app.py
```

---

## Filters available

- Product keyword
- Category
- Max price
- Min rating (3.0 / 3.5 / 4.0 / 4.5)
- Min reviews
- Number of results
- Exclude keywords

---

## Note

`credentials.json` is not committed to this repo for security reasons. You need to generate your own from Google Cloud Console.
