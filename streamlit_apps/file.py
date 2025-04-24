import streamlit as st
import pandas as pd

st.title("Sample Data Dashboard")

upload_file = st.file_uploader("Choose a CSV filr", type="csv")


if upload_file:
    st.write("File uploaded")
    pd.read_csv(upload_file)