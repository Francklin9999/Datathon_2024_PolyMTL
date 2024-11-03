import talib
import streamlit as st
from streamlit import session_state as ss
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import csv
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_directory, 'stock_info.csv') 

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
years_options = {"1 Year": "1y", "2 Years": "2y", "5 Years": "5y", "10 Years": "10y", "All Time": "max"}
data_options = ["Open", "Close", "High", "Low", "Volume"]

st.set_page_config(initial_sidebar_state=ss.sidebar_state, layout="wide")

st.title("Datathon PolyMTL 2024")

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'collapsed'

def change():
    ss.sidebar_state = (
        "collapsed" if ss.sidebar_state == "expanded" else "expanded"
    )

st.sidebar.button('Click to toggle sidebar state', on_click=change)

def chat_interface():
    st.write("### Chat")
    st.text_input("Type your message here...")
    # Additional chat elements can be added here

# State to track whether the chat is visible
if 'show_chat' not in st.session_state:
    st.session_state.show_chat = False

# Button to toggle chat visibility
toggle_chat = st.button("Toggle Chat")

# Update chat visibility state
if toggle_chat:
    st.session_state.show_chat = not st.session_state.show_chat


if st.session_state.show_chat:
    st.markdown(
        """
        <div style="position: fixed; right: 0; top: 20%; width: 300px; height: 500px; background-color: #f9f9f9; box-shadow: -2px 0 5px rgba(0,0,0,0.3); border-left: 1px solid #ccc; z-index: 100;">
            <div style="padding: 10px;">
                {}
            </div>
        </div>
        """.format(chat_interface()),
        unsafe_allow_html=True
    )

st.write("### Upload a file and let AI analyse it")
uploaded_file = st.file_uploader("Drop a file here", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("File successfully uploaded! Here are the first few rows:")
    st.dataframe(df.head())

    textAI = st.text_area("What do you want to extract from this?")
    
    if st.button("Get content"):
        st.write("Generating...")

colsmultiplechoice = st.columns([2, 1, 1, 1]) 

selected_stock = colsmultiplechoice[0].selectbox("Choose a stock to view", options=list(stock_options.keys()), format_func=lambda x: stock_options[x])
selected_period = colsmultiplechoice[1].selectbox("Select time range", options=list(years_options.keys()))
selected_data = colsmultiplechoice[2].multiselect("Select data to display on the graph", options=data_options, default=["Close"])
selected_indicators = colsmultiplechoice[3].multiselect("Select indicators to display", options=indicator_options)

if selected_stock and selected_period and selected_data:
    stock_data = yf.Ticker(selected_stock)
    
    df = stock_data.history(period=years_options[selected_period])

    colsgraph1 = st.columns([3, 2]) 

    colsgraph1[0].write(f"### {stock_options[selected_stock]} ({selected_stock}) Prices - Last {selected_period}")

    df_reset = df.reset_index() 
    df_csv = df_reset[["Date", "Open", "High", "Low", "Close", "Volume"]] 

    csv_data = df_csv.to_csv(index=False)

    colsgraph1[1].download_button(
        label="Download data as CSV",
        data=csv_data,
        file_name=f"{selected_stock}_data_{years_options[selected_period]}.csv",
        mime="text/csv"
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

    # prompt = st.chat_input("Say something")
    # if prompt:
    #     st.write("YESSSS")


