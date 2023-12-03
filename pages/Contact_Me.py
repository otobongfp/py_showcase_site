import streamlit as st

st.header("Contact Me")

with st.form("key"):
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit = st.form_submit_button()
    if submit:
        print(submit)
