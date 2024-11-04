import streamlit as st


def load_config():
    st.set_page_config(layout="wide")
    
    with st.sidebar:
        st.write("Powered by AI")

        st.write("How can I help you?")

        st.chat_input("Say something")