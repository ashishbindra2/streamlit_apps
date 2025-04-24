import streamlit as st
import numpy as np

#  One line code display
st.text("Display Row Code")
st.code("import numpy as np")

# Display row code with dataframe
with st.echo():
    import pandas as pd
    df = pd.DataFrame()
    

## Progress bar
import time
my_bar = st.progress(0,text="this is progress")
for p in range(10):
    # time.sleep(1)
    my_bar.progress(p+10)
    

## spinner
with st.spinner("waiting...."):
    time.sleep(3)

st.success("Sucessful!!")

## Display JSON Ouput
st.text("Display JSON Data")
st.json({
    "Name": "Shivan",
    "Gender": "Male"})