# Intro to Stramlit

Streamlit is an opensource app framework for Machine Leaning and Data Science projects. It Allows you to create beautiful web applications for your achine leaning and data science projects with simple python scrips.


## for titlt
`st.title("hello title")`

## How to run streamlit application
`streamlit run app.py`


## Display a sample text
```py
st.write("This is sample text!!")
```

## Display the Dataframe

### Create a simple Dataframe
```py
df = pd.DataFrame({
    "first column": [1,2,3,4],
    "secound coulmn": [10,20,30,40]
})

st.write("Here is the dataframe")
st.write(df)
```
## Create a line chart
```py
chart_data = pd.DataFrame(
    np.random.randn(10,3), columns = ['a','b','c']
)

st.line_chart(chart_data)
```
## Happ Birthday
```py
st.title("Happy Birthday!!")

st.balloons()
```

## One line code display
```py
st.text("Display Row Code")
st.code("import numpy as np")
```

## Display row code with dataframe
```py
with st.echo():
    import pandas as pd
    df = pd.DataFrame()
```

## Progress bar
```py
import time
my_bar = st.progress(0,text="this is progress")
for p in range(100):
    time.sleep(1)
    my_bar.progress(p+10)
```

## spinner
```py
with st.spinner("waiting...."):
    time.sleep(3)

st.success("Sucessful!!")
```
## side bar
```py
# Sidebar
st.sidebar.header("About")
st.sidebar.title("This is our demo Project")

algorithms = st.sidebar.selectbox("Your Alogorithm",["Liner Regration","Logistic Regration", "dession tree"])
```

## Selector 
```py
occupation = st.selectbox("Your Occuption", ["programmer","data scientist", "Doctor", "Businessman"])
st.write("you Selected this option", occupation)
```

## Miltiselect
```py
location = st.multiselect("Where do you work", ("pbi","mumbai", "punjaie","delhi"))
st.write("You selected", len(location), "locations")
```

## Display JSON Output
```py
st.text("Display JSON Data")
st.json({
    "Name": "Shivan",
    "Gender": "Male"})
```

status = st.radio(")