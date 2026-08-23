import streamlit as st

st.title("Aura App")
if st.button("Want Aura"):
    st.success("Your aura is being activated")

add_masala = st.checkbox("increase Aura")

if add_masala:
    st.write("Aura added to you")

Aura_type = st.radio("Pick your aura base: ", ["infinite", "powerful", "unloseable"])
st.write(f"Selected base {Aura_type}")
flavour = st.selectbox("Choose holder: ", ["None","Undertaker", "Henry Cavil", "John Cena", "Abhinav Thakur", "Lionel Messi", "Cristiano Ronaldo", "Virat Kohli"])
if flavour=="None":
    pass
else:
    st.write(f"Great choice, You got {flavour}'s Aura!")


