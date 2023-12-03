# Main Application
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.jpg", width=600)

with col2:
    st.title("About Me")
    content = """
    My name is Otobong. I love building things. For me it is satisfying to tackle problems and finally figure out the solution.
    In this showcase page I update simple projects I have built with python.
    It is still a living and breathing project. I have been writing python since 2019, but I paused for a while to pursue my interest in blockchain technology.
    This year with my interests to pursue DevOps and Cloud, I had to refresh my mind.
    """
    st.write(content)