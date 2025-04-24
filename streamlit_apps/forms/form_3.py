import streamlit as st

# Text Area

message = st.text_area("Enter your message","Type here...")

if st.button("submit", key=2):
    result = message.title()
    st.success(result)

occupation = st.selectbox("Your Occuption", ["programmer","data scientist", "Doctor", "Businessman"])

st.write("you Selected this option", occupation)

## Miltiselect

location = st.multiselect("Where do you work", ("pbi","mumbai", "punjaie","delhi"))


st.write("You selected", len(location), "locations")


status = st.radio("What is your Status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are active")
else:
    st.warning("Inactive, asd")
    
if st.checkbox("Show / Hide"):
    st.text("Showing or hiding widget")