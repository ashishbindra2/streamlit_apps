import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image(
        "https://images.pexels.com/photos/31188110/pexels-photo-31188110.jpeg",
        width=200,
    )
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image(
        "https://images.pexels.com/photos/28052357/pexels-photo-28052357.jpeg",
        width=200,
    )
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("THanks for voting masala chai")

elif vote2:
    st.success("Thanks for voting Adrak Chai")


name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "kesae", "Adrak"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")

with st.expander("show chai Making Instructions"):
    st.write(
        """
             1. Boil water with tea leaves
             2. Add milk and spices
             3. Serve hot
        """
    )

st.markdown("""
            ## test
            
            > new row
            """)
