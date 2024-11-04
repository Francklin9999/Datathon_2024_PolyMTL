import streamlit as st
import pandas as pd


def page2():
    st.write("### Upload a file and let AI analyse it")
    st.write("Our LLM is trained on a large number of data, it will take your fill and compare it to others financial institution data.")
    uploaded_file = st.file_uploader("Drop a file here", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("File successfully uploaded! Here are the first few rows:")
        st.dataframe(df.head())

        textAI = st.text_area("What do you want to extract from this?")
        
        if st.button("Get content"):
            st.write("Generating...")
            