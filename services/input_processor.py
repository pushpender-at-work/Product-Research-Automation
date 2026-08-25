def process_inputs(form_data):

    data = {
    "keyword": form_data.get("keyword", "").strip(),
    "category": form_data.get("category", "").strip(),
    "max_price": int(form_data["max_price"]) if form_data.get("max_price") else None,
    "min_rating": float(form_data["min_rating"]) if form_data.get("min_rating") else None,
    "min_reviews": int(form_data["min_reviews"]) if form_data.get("min_reviews") else None,
    "num_results": int(form_data["num_results"]) if form_data.get("num_results") else 20,
    "exclude": form_data.get("exclude", "").strip()
}

    return data