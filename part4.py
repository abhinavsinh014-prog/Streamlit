import streamlit as st
import pandas as pd

st.title("Aura Legends")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df= pd.read_csv(file)
    st.subheader("Uploaded Data")
    st.dataframe(df)

if file:
    st.subheader("Data Summary")
    st.write(df.describe())