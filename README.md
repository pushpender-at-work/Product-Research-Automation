#Online Product Researcher

A tool that takes product details from the user and automatically scrapes google for that product data and pushes it into a google sheet.

##what it does

user fills a form with product info like name, category, price range, reviews etc. the tool searches google using serpapi, collects the results and writes everything directly into a google sheet — no manual copy paste needed.

##tech used
-Python
SerpAPI — to search google programmatically
gspread — to write data into google sheets
HTML — for the user input form
how to run
pip install -r requirements.txt
python app.py
setup
get your api key from serpapi.com
set up google sheets api credentials from google cloud console, download the json key
create a .env file and add:
SERPAPI_KEY=your_key_here
put your google credentials json file in the project folder
update the sheet name in the code to match your google sheet
flow
user fills form → serpapi searches google → data extracted → pushed to google sheet
note

make sure your google sheet is shared with the service account email from your credentials json file otherwise gspread will throw a permission error.
