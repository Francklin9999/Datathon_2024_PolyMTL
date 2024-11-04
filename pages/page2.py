import streamlit as st
from pathlib import Path
import os
from ai.doc_summarizer import Chunk_and_Summarize
import time
import boto3
from dotenv import load_dotenv

load_dotenv()

def page2():
    st.write("### Upload a file and let AI analyse it")
    st.write("Our LLM is trained on a large number of data, it will take your fill and compare it to others financial institution data.")
    uploaded_file = st.file_uploader("Drop a file here", type=["csv, pdf"])

    if uploaded_file is not None:
        save_folder = os.getenv("save_folder")
        save_path = Path(save_folder, uploaded_file)
        with open(save_path, mode='wb') as w:
            w.write(uploaded_file.getvalue())
 
        if save_path.exists():
            st.success(f'File {uploaded_file.name} is successfully saved!')
 
            st.write(Chunk_and_Summarize(save_path))
 
            os.remove(save_path)