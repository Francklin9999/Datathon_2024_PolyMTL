from .base import *
from dotenv import load_dotenv
import os
import finnhub
import datetime

load_dotenv()

API_KEY_FINANCIAL = os.getenv("API_KEY_FINNHUB")

def finnhub_connect():
    return finnhub.Client(api_key=API_KEY_FINANCIAL)

def get_today_date():
    return datetime.date.today().strftime("%Y-%m-%d")

def get_finnhub_news_by_company(company):
    finnhub_client = finnhub_connect()

    data = finnhub_client.company_news(company, _from="2020-06-01", to=get_today_date())

    print(data)

    return (
        data
    )

def get_finnhub_market_new():
    finnhub_client = finnhub_connect()

    data = finnhub_client.general_news('general', min_id=0)

    print(data)

    return (
        data
        )