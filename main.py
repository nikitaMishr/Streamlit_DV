import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Visualization with Streamlit",
                   page_icon="😁"
                   
)
st.write("HI this is new chnages")
st.title("Data Visualization with Streamlit")
with st.sidebar:
    upload=st.file_uploader("Upload CSV")


if upload is not None:
    df=pd.read_csv(upload)
    st.dataframe(df.head())