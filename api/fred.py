from .base import *
from dotenv import load_dotenv
import os
import pandas as pd
import plotly.express as px

load_dotenv()

API_KEY_FRED = os.getenv("API_KEY_FRED")

def get_fred_series_search(text_search):
    result = '+'.join(text_search.lower().split())
    url = f"https://api.stlouisfed.org/fred/series/search?search_text={result}&api_key={API_KEY_FRED}&file_type=json"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None

    
def get_fred_series_observationns(text_search):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={text_search}&api_key={API_KEY_FRED}&file_type=json"
    data = get_request(url, 10)
    if data:
        return data.json()
    else:
        return None
    

def get_data(text):
    data = get_fred_series_search(text)
    for idx, series in enumerate(data["seriess"]):
        if not series:
            continue
        if idx > 5:
            break
        dates = get_fred_series_observationns(series["id"])

        date =[]
        value = []

        for observation in dates["observations"]:
            date_str = observation["date"] 
            value_str = observation["value"].strip() 

            if value_str and value_str != '.':
                try:
                    value_float = float(value_str)
                    date.append(date_str)
                    value.append(value_float)
                except ValueError:
                    print(f"Invalid value for conversion: {value_str}")
            else:
                print(f"Skipping invalid value: {value_str}")

        df = pd.DataFrame({
            'Date': date,
            'Value': value,
        })

        fig = px.line(df, x='Date', y='Value', title='', markers=True)
        fig.update_layout(xaxis_title='Date', yaxis_title='Value', xaxis_tickangle=-45)
        
        return fig