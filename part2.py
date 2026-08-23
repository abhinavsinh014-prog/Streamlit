import streamlit as st

st.title("Aura App")
if st.button("Want Aura"):
    st.success("Your aura is being activated")

add_masala = st.checkbox("Increase Aura")

