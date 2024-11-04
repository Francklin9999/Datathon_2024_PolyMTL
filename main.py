import talib
import streamlit as st
from streamlit import session_state as ss
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import csv
import os
from app_config import load_config
from pages.home import home
from pages.page1 import page1
from pages.page2 import page2

load_config()

pages = {
    "Daily Stock Highlights": "home",
    "View a stock": "page1",
    "Summerize a Stock Document": "page2",
}

selected_page = st.selectbox("Select a page", list(pages.keys()))

if selected_page == "Daily Stock Highlights":
    home()
elif selected_page == "View a stock":
    page1()
elif selected_page == "Summerize a Stock Document":
    page2()
