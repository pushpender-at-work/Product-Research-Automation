def format_products(products):

    formatted = []

    for product in products:

        formatted.append({
            "title": product.get("title"),
            "price": product.get("extracted_price"),
            "rating": product.get("rating"),
            "reviews": product.get("reviews"),
            "link": product.get("link")
        })

    return formatted