import streamlit as st

st.title("Aura Legends")

col1, col2 = st.columns(2)

with col1:
    st.header("Villian's Aura")
    st.image("C:\\Users\\abhin\\Downloads\\doom.webp", caption="Doom",width=300)
    vote_1 = st.button("Dr Doom Aura")
with col2:
    st.header("Hero's Aura")
    st.image("C:\\Users\\abhin\\OneDrive\\Pictures\\licensed-image.jpg", caption="John cena",width=300)
    vote_2 = st.button("John Cena Aura")

if vote_1:
    st.write("You selected Dr Doom's Aura")
elif vote_2:
    st.write("You selected John Cena's Aura")

name = st.sidebar.text_input("Enter your name")
side = st.sidebar.selectbox("Choose your side:", ["Hero", "Villian"])

 