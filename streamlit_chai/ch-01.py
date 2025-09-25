import streamlit as st

st.title("Hello Chat App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first application")
st.write("choose your fav variety of chai")

chai = st.selectbox("Your fav  chai: ", ["Masala chai", "Lemon Tea", "Adrak chai", "kesar Chai"])

st.write(f"Your choose {chai}. Excellent choise")

st.success("Your chai has been brewed!")