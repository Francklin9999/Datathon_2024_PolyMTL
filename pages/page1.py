import talib
import streamlit as st
import os
import csv
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from api.alpha import *
import yfinance as yf
import matplotlib.pyplot as plt
import json
from api.finnhub import get_finnhub_news_by_company, get_finnhub_market_new
import datetime


def page1():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(current_directory, '..', 'static', 'stock_info.csv')

    stock_options = {}

    with open(file_path, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            stock_options[row['Ticker']] = row['Name']

    textAI = None

    indicators = {
        "SMA": {"func": talib.SMA, "name": "30-Day SMA", "timeperiod": 30, "dash": "dash"},
        "EMA": {"func": talib.EMA, "name": "30-Day EMA", "timeperiod": 30, "dash": "dash"},
        "RSI": {"func": talib.RSI, "name": "14-Day RSI", "timeperiod": 14, "dash": "dot"},
        # "MACD": {"func": talib.MACD, "name": "MACD", "params": {"fastperiod": 12, "slowperiod": 26, "signalperiod": 9}, "dash": "solid"},
        # "BBANDS_upper": {"func": lambda x: talib.BBANDS(x, timeperiod=20)[0], "name": "Bollinger Upper", "timeperiod": 20, "dash": "dash"},
        # "BBANDS_middle": {"func": lambda x: talib.BBANDS(x, timeperiod=20)[1], "name": "Bollinger Middle", "timeperiod": 20, "dash": "solid"},
        # "BBANDS_lower": {"func": lambda x: talib.BBANDS(x, timeperiod=20)[2], "name": "Bollinger Lower", "timeperiod": 20, "dash": "dash"},
        # "ATR": {"func": talib.ATR, "name": "ATR", "timeperiod": 14, "dash": "dot"},
        # "STOCH_slowk": {"func": lambda high, low, close: talib.STOCH(high, low, close)[0], "name": "Stochastic %K", "dash": "dashdot"},
        # "STOCH_slowd": {"func": lambda high, low, close: talib.STOCH(high, low, close)[1], "name": "Stochastic %D", "dash": "dot"},
        # "OBV": {"func": talib.OBV, "name": "On-Balance Volume", "dash": "solid"}
    }       
    indicator_options = list(indicators.keys())

    time_options = {
        "1 Day": "1d",
        "5 Days": "5d",
        "1 Month": "1mo",
        "3 Months": "3mo",
        "6 Months": "6mo",
        "1 Year": "1y",
        "2 Years": "2y",
        "5 Years": "5y",
        "10 Years": "10y",
        "All Time": "max"
    }
    data_options = ["Open", "Close", "High", "Low", "Volume"]

    st.title("Datathon PolyMTL 2024")

    colsmultiplechoice = st.columns([2, 1, 1, 1]) 

    selected_stock = colsmultiplechoice[0].selectbox("Choose a stock to view", options=list(stock_options.keys()), format_func=lambda x: stock_options[x])
    selected_period = colsmultiplechoice[1].selectbox("Select time range", options=list(time_options.keys()))
    selected_data = colsmultiplechoice[2].multiselect("Select data to display on the graph", options=data_options, default=["Close"])
    selected_indicators = colsmultiplechoice[3].multiselect("Select indicators to display", options=indicator_options)

    if selected_stock and selected_period and selected_data:
        stock_data = yf.Ticker(selected_stock)

        # Check if the information exists and display it
        row_data = []

        if stock_data.info.get("industry"):
            row_data.append(stock_data.info["industry"])

        if stock_data.info.get("sector"):
            row_data.append(stock_data.info["sector"])

        # Combine city and country if both exist
        if stock_data.info.get("City") and stock_data.info.get("country"):
            row_data.append(f"{stock_data.info['City']}, {stock_data.info['country']}")

        # Check if the website exists and create a link
        if stock_data.info.get("website"):
            row_data.append(f"[Company Website]({stock_data.info['website']})")

        # Display the collected data in one row
        if row_data:  # Only display if there's any data to show
            st.write(" | ".join(row_data))

        # Long Business Summary toggle
        if stock_data.info.get("longBusinessSummary"):
            with st.expander("Long Business Summary", expanded=False):  # Set expanded=True to show by default
                st.write(stock_data.info["longBusinessSummary"])

        
        df = stock_data.history(period=time_options[selected_period])

        colsgraph1 = st.columns([3, 2, 2]) 

        colsgraph1[0].write(f"### {stock_options[selected_stock]} ({selected_stock}) Prices - Last {selected_period}")

        df_reset = df.reset_index() 
        df_csv = df_reset[["Date", "Open", "High", "Low", "Close", "Volume"]] 

        csv_data = df_csv.to_csv(index=False)

        colsgraph1[1].download_button(
            label="Download chart data",
            data=csv_data,
            file_name=f"{selected_stock}_data_{time_options[selected_period]}.csv",
            mime="text/csv"
        )

        colsgraph1[2].download_button(
            label="Download company data",
            data=json.dumps(stock_data.info, indent=4),
            file_name=f"{selected_stock}_company_data.json",
            mime="application/json"
        )

        fig = go.Figure()

        for data in selected_data:
            if data != "Volume":
                fig.add_trace(go.Scatter(x=df.index, y=df[data], mode='lines', name=f"{data} Price"))

        for indicator in selected_indicators:
            config = indicators[indicator]
            df[indicator] = config["func"](df['Close'], timeperiod=config["timeperiod"])
            fig.add_trace(go.Scatter(
                x=df.index,
                y=df[indicator],
                mode='lines',
                name=config["name"],
                line=dict(dash=config["dash"])
            ))

        st.plotly_chart(fig)

        if stock_data.info["sector"]:
            get_sector_data(stock_data.info, time_options[selected_period])

        news_data = get_finnhub_market_new()

        for news in news_data:
            with st.expander(news["headline"], expanded=False):
                st.image(news["image"], use_column_width=True)
                st.write(f"**Source:** {news['source']}")
                st.write(f"**Summary:** {news['summary']}")
                st.write(f"[Read more]({news['url']})")



def get_sector_data(data, time):
    subdirectory = "static/nasdaq/"
    
    file = os.path.join(subdirectory, f"nasdaq_{data['sector'].strip()}.csv")

    df = None

    try:
        df = pd.read_csv(file)
    except FileNotFoundError:
        st.write("No corraleted sector.")
        return
    
    cols = st.columns([3, 3]) 
    
    with cols[0]:
        st.write("Sector Data:")
        st.write(df.head(10))

    closing_prices = []

    for index, row in df.iterrows():
        symbol = row['Symbol']
        name = row['Name']
        
        stock_data = yf.download(symbol, period=time)
        closing_prices.append(stock_data['Close'])
        
        if index >= 9: 
            break
    closing_prices_df = pd.concat(closing_prices, axis=1)
    closing_prices_df.columns = df['Name'][:10]

    average_closing_prices = closing_prices_df.mean(axis=1)

    with cols[1]:
        st.subheader("Average Closing Price of First 10 Stocks")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=average_closing_prices.index, y=average_closing_prices, mode='lines', name='Average Closing Price', line=dict(color='blue')))
        fig1.update_layout(title='Average Closing Price of First 10 Stocks', xaxis_title='Date', yaxis_title='Price (USD)')
        st.plotly_chart(fig1)

    st.subheader("Closing Prices of First 10 Stocks")
    fig2 = go.Figure()
    for column in closing_prices_df.columns:
        fig2.add_trace(go.Scatter(x=closing_prices_df.index, y=closing_prices_df[column], mode='lines', name=column))
    fig2.update_layout(title='Closing Prices of First 10 Stocks', xaxis_title='Date', yaxis_title='Price (USD)')
    st.plotly_chart(fig2)

def get_date_subtracted(option):
    time_deltas = {
        "1 Day": datetime.timedelta(days=1),
        "5 Days": datetime.timedelta(days=5),
        "1 Month": datetime.timedelta(days=30),
        "3 Months": datetime.timedelta(days=90), 
        "6 Months": datetime.timedelta(days=180), 
        "1 Year": datetime.timedelta(days=365),
        "2 Years": datetime.timedelta(days=730), 
        "5 Years": datetime.timedelta(days=1825),
        "10 Years": datetime.timedelta(days=3650),
        "All Time": datetime.timedelta(days=3650)
    }

    today = datetime.date.today()
    
    if option in time_deltas:
        delta = time_deltas[option]
        if delta:
            return (today - delta).strftime("%Y-%m-%d")
        else:
            return None 
    else:
        raise ValueError("Invalid option provided")