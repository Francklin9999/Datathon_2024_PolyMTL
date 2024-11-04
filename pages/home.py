from api.financial import get_fiancial_top_gainers, get_fiancial_top_losers
import pandas as pd
import plotly.graph_objs as go
import streamlit as st


def home() :
    top_gainers = get_fiancial_top_gainers()
    top_losers = get_fiancial_top_losers()

    gainer_symbols = [g['symbol'] for g in top_gainers]
    gainer_changes = [g['change'] for g in top_gainers]
    loser_symbols = [l['symbol'] for l in top_losers]
    loser_changes = [l['change'] for l in top_losers]

    fig_combined = go.Figure()
    fig_combined.add_trace(go.Bar(x=gainer_symbols, y=gainer_changes, name='Gainers', marker_color='green'))
    fig_combined.add_trace(go.Bar(x=loser_symbols, y=loser_changes, name='Losers', marker_color='red'))

    fig_combined.update_layout(title='Gainers and Losers',
                            xaxis_title='Symbols',
                            yaxis_title='Change',
                            barmode='group')

    fig_gainers = go.Figure()
    fig_gainers.add_trace(go.Bar(x=gainer_symbols, y=gainer_changes, name='Gainers', marker_color='green'))
    fig_gainers.update_layout(title='Gainers',
                            xaxis_title='Symbols',
                            yaxis_title='Change')

    fig_losers = go.Figure()
    fig_losers.add_trace(go.Bar(x=loser_symbols, y=loser_changes, name='Losers', marker_color='red'))
    fig_losers.update_layout(title='Losers',
                            xaxis_title='Symbols',
                            yaxis_title='Change')

    st.title('Stock Market Gainers and Losers')
    st.plotly_chart(fig_combined)
    st.plotly_chart(fig_gainers)
    st.plotly_chart(fig_losers)