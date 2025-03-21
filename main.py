import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.set_page_config(page_title="Data Visualization With Streamlit",
                   page_icon="😁")
with st.sidebar:
  st.write("Hi this is new changes")
  st.title("Data Visualization With Streamlit")
  upload=st.file_uploader("Upload CSV")

if upload is not None:
    df=pd.read_csv(upload)
    st.dataframe(df.head())
