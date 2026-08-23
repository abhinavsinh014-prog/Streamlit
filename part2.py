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

Aura = st.slider("Aura level ", 0, 9999, 100)
st.write(f"Aura level got {Aura}")

cups = st.number_input("How many days U Aura remain?", min_value=1, max_value=10, step=1)
st.write(f"Selected Aura days U get {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ! You get unmachable Aura")

dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth {dob}")