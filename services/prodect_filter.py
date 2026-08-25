def filter_product(products,criteria):

    filtered=[]

    for product in products:

        price=product.get('extracted_price')
        rating=product.get('rating')
        reviews=product.get('reviews')
        title=product.get('title',"").lower()

       
        if criteria["max_price"] is not None:
            if price is None or price > criteria["max_price"]:
                continue

        
        if criteria["min_rating"] is not None:
            if rating is None or rating < criteria["min_rating"]:
                continue

       
        if criteria["min_reviews"] is not None:
            if reviews is None or reviews < criteria["min_reviews"]:
                continue

        
        if criteria["exclude"]:
            if criteria["exclude"].lower() in title:
                continue

        filtered.append(product)

    return filtered
