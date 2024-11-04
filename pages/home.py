from api.financial import get_fiancial_top_gainers, get_fiancial_top_losers
import pandas as pd
import plotly.graph_objs as go
import streamlit as st
from api.alpha import get_alpha_news
import datetime


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

    st.write("Market Sentiment")

    data = get_alpha_news()

    if data:
        st.subheader("Definitions")
        st.write("Sentiment Score: ", data['sentiment_score_definition'])
        st.write("Relevance Score: ", data['relevance_score_definition'])

        # Display feed items
        st.subheader("Feed Items")
        for item in data['feed']:
            st.markdown(f"### {item['title']}")
            st.write(f"Published on: {item['time_published']}")
            st.write(f"Authors: {', '.join(item['authors'])}")
            st.write(f"Summary: {item['summary']}")
            st.write(f"[Read more]({item['url']})")
            
            if item['banner_image']:
                st.image(item['banner_image'], caption=item['title'], use_column_width=True)

            st.write("---")
    else :
        st.write("No news available")