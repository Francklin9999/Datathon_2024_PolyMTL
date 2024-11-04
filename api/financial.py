from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_FINANCIAL = os.getenv("API_KEY_FINANCIAL")

def get_fiancial_top_gainers():
    url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={API_KEY_FINANCIAL}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        raise Exception("No data")

def get_fiancial_top_losers():
    url = f"https://financialmodelingprep.com/api/v3/stock_market/losers?apikey={API_KEY_FINANCIAL}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        raise Exception("No data")