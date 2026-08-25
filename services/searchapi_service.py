
import requests

API_KEY="zeosrxg9s72tiyyc9izWoobV"

def search_amazon(query):
    url="https://www.searchapi.io/api/v1/search"

    params = {
        "engine": "amazon_search",
        "q": query,
        "api_key": API_KEY
    }
    response=requests.get(url,params=params)

    return response.json()