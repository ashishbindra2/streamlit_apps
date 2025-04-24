import streamlit as st
import pandas as pd 
import numpy as np

# title
st.title("Chitchat application💲")

# st.subheader("First application")
st.text(f"This is our first web-app 💞")



data = pd.DataFrame(data=np.random.rand(10,3),columns=["c1","c2","c3"])

# st.write("ashish")
# st.subheader("This is our dummy data")

st.sidebar.header("Made with 💚 By Ashish bindra")
st.sidebar.text("Please selct parameters")

st.text_input("data needed")
st.button("mui", type="secondary",)
st.chat_input("Hy how u doing")
car_color = st.sidebar.selectbox("Please select the color of car",["red", "pink", "black"])
# btn = st.sidebar.button("submit")

# if btn:
#     st.write(f"You selected {car_color}")
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background: {car_color}
#     }}
 
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# st.write(data)
# st.line_chart(data=data,x_label="student age")
# st.bar_chart(data)
# # num1 = st.text_input("Enter first number")
# nust.text_input("Enter second  number")