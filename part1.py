import streamlit as st

st.title("My Streamlit Aura")
st.subheader("Welcome to my Streamlit infinity Aura!")
st.text("This is a proof of my Aura which is infinite and never-ending.")
st.write("Streamlit is a powerful Aura tool for creating interactive web applications with Python. It allows you to build and deploy data-driven apps quickly and easily.")

aura = st.selectbox("Choose your Aura Farmer:", ["Undertaker", "Henry Cavil", "John Cena", "Abhinav Thakur", "Lionel Messi", "Cristiano Ronaldo", "Virat Kohli"])

st.success(f"You have selected {aura} as your Aura Farmer. Enjoy the infinite Aura experience!")