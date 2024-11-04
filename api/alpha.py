from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_ALPHA = os.getenv("API_KEY_ALPHAVANTAGE")


def get_alpha_top_stocks():
    url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={API_KEY_ALPHA}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None

def get_alpha_balance_sheet_by_company(company):
    url = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={company}&apikey={API_KEY_ALPHA}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None
    
def get_alpha_sentiment_analysis_by_company(company):
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={company}&apikey={API_KEY_ALPHA}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None

def get_alpha_insider_transaction(company):
    url = f"https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&symbol={company}&apikey={API_KEY_ALPHA}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None
    
def get_alpha_company_overview(company):
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={company}&apikey={API_KEY_ALPHA}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None

def get_alpha_company_etf(company):
    url = f"https://www.alphavantage.co/query?function=ETF_PROFILE&symbol={company}&apikey={API_KEY_ALPHA}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None
    
def get_alpha_company_earnings(company):
    url =f"https://www.alphavantage.co/query?function=EARNINGS&symbol={company}&apikey={API_KEY_ALPHA}"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None
