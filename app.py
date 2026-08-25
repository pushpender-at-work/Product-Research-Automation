from flask import Flask,render_template,request
from services.input_processor import process_inputs
from services.query_builder import build_search_querry
from services.searchapi_service import search_amazon
from services.prodect_filter import filter_product
from services.product_formatter import format_products
from services.sheet_writer import connect_sheet, write_to_sheet

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def search():
    unstr_data=request.form

    data=process_inputs(unstr_data)
    query=build_search_querry(data)
    
    result=search_amazon(query)

    product=result["organic_results"]
    

    filtered_products=filter_product(products=product,criteria=data)
    
    formated_products=format_products(filtered_products)
    print(formated_products)  
    client = connect_sheet()

    sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1ZtFw6fbg3V80ezB1-yI-AOA_tFuRSmR47w9uq-R88Rg/edit?gid=0#gid=0").sheet1
    
    write_to_sheet(sheet,formated_products)


    # keyword=request.form.get("keyword")
    # category=request.form.get("category")
    # max_price=request.form.get('max_price')
    # min_rating=request.form.get("min_rating")
    # min_reviews = request.form.get("min_reviews")
    # num_results = request.form.get("num_results")

    # print(keyword)
    # print(category)
    # print(max_price)
    # print(min_reviews)
    # print(min_rating)
    # print(num_results)

    return f"Exported {len(formated_products)} products!"
    
if __name__== '__main__':
    app.run(debug=True,port=5004)