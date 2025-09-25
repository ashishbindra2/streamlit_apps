# Streamlit

A Faster wav to build and share data apps

- Purealy based on python

we are write code 2 types

1. inpretive code
2. declarative code:- eg yaml, tom

- declartiver not reqired html, css, js

## To Display messages

```py
import streamlit as st

st.title("Hello Chat App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first application")
st.write("choose your fav variety of chai")
```

### output

![alt text](img/1.png)

## Select box

```py
chai = st.selectbox("Your fav  chai: ", ["Masala chai", "Lemon Tea", "Adrak chai", "kesar Chai"])

st.write(f"Your choose {chai}. Excellent choise")
st.success("Your chai has been brewed!")
```

### output

![alt text](img/image.png)

## conditional

### if with success msg

```py
import streamlit as st

st.title("Cahi Maker App")

if st.button("Make Chai"):
    st.success("Your chai is being brewed")
```

Output:

![alt text](img/image-1.png)

### check box

```py
add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai")
```

![alt text](img/image-2.png)

### radio button

```py
tea_type = st.radio("Pick your chai base: ", ["Milk", "Water", "Almond Milk"])

st.write(f"Select base {tea_type}")
```

![alt text](img/image-3.png)

### select and slider

```py
flavour = st.selectbox("Choose flavour ", ["Adrak", "Kesar", "Tulsi"] )

sugar = st.slider("Sugar level", 0, 5, 2)
```

output
![alt text](img/image-4.png)

### numbers

```py
cups = st.number_input("How many cups", min_value=1, max_value=10, step=2)
st.write(f"Selected sugar level {cups}")
```

![alt text](img/image-5.png)

## input

```py
name = st.text_input("Plz ender your name")

if name:
    st.write(f"We {name}, Your chai is on the way")
```

![alt text](img/image-6.png)

```py
dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth {dob}")
```

![alt text](img/image-7.png)

## plit the page

```py
import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting masala chai")

elif vote2:
    st.success("Thanks for voting Adrak Chai")
```

![alt text](img/image-8.png)

```py

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/28052357/pexels-photo-28052357.jpeg", width=200)
    vote2 = st.button("Vote Adrak Chai")

```

![alt text](img/image-9.png)

### sidebar

```py
    

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "kesae", "Adrak"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")

```

![alt text](img/image-10.png)

### Expander

```py
with st.expander("show chai Making Instructions"):
    st.write(
        """
             1. Boil water with tea leaves
             2. Add milk and spices
             3. Serve hot
        """
    )
```

![alt text](img/image-11.png)

### makdow

```py
st.markdown("""
            ## test
            
            > new row
            """)
```

## file upload

```py
import streamlit as st
import pandas as pd

st.title("Chai Sale Dashboard")

file = st.file_uploader("Upload your csv file", type=['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())
```

![alt text](img/image-12.png)
![alt text](img/image-13.png)

## filter data

```py
if file:
    cities = df["city"].unique()
    selected_city = st.selectbox("Filter  by cites", cities)
    
    
    filtered_data = df[df["city"] == selected_city]
    st.dataframe(filtered_data)

```

![alt text](img/image-14.png)
