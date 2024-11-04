import streamlit as st
from ai import invoke_agent as agenthelper
import streamlit as st
import json
import pandas as pd


def load_config():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    if 'responses' not in st.session_state:
        st.session_state.responses = []

    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>Powered by AI</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>How can I help you?</h4>", unsafe_allow_html=True)

        user_input = st.text_input("Ask something", placeholder="Type here...")

        if st.button("Submit"):
            if user_input:
                response = call_llm(user_input) 
                st.session_state.responses.append((user_input, response)) 
                st.experimental_rerun()

        if st.session_state.responses:
            response_container = st.container()
            with response_container:
                for input_text, response_text in st.session_state.responses:
                    st.markdown(f"**You:** {input_text}")
                    st.markdown(f"**AI:** {response_text}")
                    st.markdown("---") 

            st.markdown(
                """
                <style>
                .streamlit-expanderHeader {
                    font-size: 16px;
                }
                .css-18ni7ap {
                    max-height: 300px; /* Set the height for the scrollable area */
                    overflow-y: auto; /* Enable vertical scrolling */
                }
                </style>
                """, unsafe_allow_html=True
            )

def call_llm(prompt):
    event = {
        "sessionId": "MYSESSION",
        "question": prompt
    }
    response = agenthelper.lambda_handler(event, None)
    
    try:
        # Parse the JSON string
        if response and 'body' in response and response['body']:
            response_data = json.loads(response['body'])
            print("TRACE & RESPONSE DATA ->  ", response_data)
        else:
            print("Invalid or empty response received")
    except json.JSONDecodeError as e:
        print("JSON decoding error:", e)
        response_data = None 
    
    try:
        # Extract the response and trace data
        all_data = format_response(response_data['response'])
        the_response = response_data['trace_data']
    except:
        all_data = "..." 
        the_response = "Apologies, but an error occurred. Please rerun the application" 
        # Use trace_data and formatted_response as needed
        st.sidebar.text_area("", value=all_data, height=300)
        st.session_state['history'].append({"question": prompt, "answer": the_response})
        st.session_state['trace_data'] = the_response


def format_response(response_body):
    try:
        # Try to load the response as JSON
        data = json.loads(response_body)
        # If it's a list, convert it to a DataFrame for better visualization
        if isinstance(data, list):
            return pd.DataFrame(data)
        else:
            return response_body
    except json.JSONDecodeError:
        # If response is not JSON, return as is
        return response_body