import talib
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

st.title("Datathon PolyMTL 2024")

uploaded_file = st.file_uploader("Drop a file here", type=["csv"])

stock_options = {
    "AAPL": "Apple",
    "GOOGL": "Alphabet (Google)",
    "MSFT": "Microsoft",
    "AMZN": "Amazon",
    "TSLA": "Tesla",
    "NFLX": "Netflix",
}

selected_stock = st.selectbox("Choose a stock to view", options=list(stock_options.keys()), format_func=lambda x: stock_options[x])

years_options = {"1 Year": "1y", "2 Years": "2y", "5 Years": "5y", "10 Years": "10y"}
selected_period = st.selectbox("Select time range", options=list(years_options.keys()))

data_options = ["Open", "Close", "High", "Low", "Volume"]
selected_data = st.multiselect("Select data to display on the graph", options=data_options, default=["Close"])

indicator_options = ["SMA", "EMA", "RSI"]
selected_indicators = st.multiselect("Select indicators to display", options=indicator_options)

if selected_stock and selected_period and selected_data:
    stock_data = yf.Ticker(selected_stock)
    df = stock_data.history(period=years_options[selected_period])

    st.write(f"### {stock_options[selected_stock]} ({selected_stock}) Prices - Last {selected_period}")

    fig = go.Figure()

    for data in selected_data:
        if data != "Volume":
            fig.add_trace(go.Scatter(x=df.index, y=df[data], mode='lines', name=f"{data} Price"))

    if "SMA" in selected_indicators:
        df['SMA'] = talib.SMA(df['Close'], timeperiod=30)
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA'], mode='lines', name='30-Day SMA', line=dict(dash='dash')))

    if "EMA" in selected_indicators:
        df['EMA'] = talib.EMA(df['Close'], timeperiod=30)
        fig.add_trace(go.Scatter(x=df.index, y=df['EMA'], mode='lines', name='30-Day EMA', line=dict(dash='dash')))

    if "RSI" in selected_indicators:
        df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
        fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], mode='lines', name='14-Day RSI', line=dict(dash='dot')))

    fig.update_layout(
        title=f"{stock_options[selected_stock]} ({selected_stock}) Prices",
        xaxis_title="Date",
        yaxis_title="Price",
        legend_title="Data",
        hovermode="x unified"
    )

    st.plotly_chart(fig)

    df_reset = df.reset_index() 
    df_csv = df_reset[["Date", "Open", "High", "Low", "Close", "Volume"]] 

    csv_data = df_csv.to_csv(index=False)

    st.download_button(
        label="Download data as CSV",
        data=csv_data,
        file_name=f"{selected_stock}_data_{years_options[selected_period]}.csv",
        mime="text/csv"
    )