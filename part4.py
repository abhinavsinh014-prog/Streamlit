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

if file:
    st.subheader("Data Visualization")
    st.line_chart(df)

if file:
    cities = df['city'].unique()
    selected_city = st.selectbox("Select a city to filter data:", cities)
    filtered_data = df[df['city'] == selected_city]
    st.subheader("Filtered Data")
    st.dataframe(filtered_data)