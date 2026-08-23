import streamlit as st

st.title("Aura Legends")

col1, col2 = st.columns(2)

with col1:
    st.header("Villian's Aura")
    st.image("C:\\Users\\abhin\\Downloads\\doom.webp", caption="Thanos",width=300)

with col2:
    st.header("Hero's Aura")
    st.image("C:\\Users\\abhin\\OneDrive\\Pictures\\licensed-image.jpg", caption="John cena",width=300)