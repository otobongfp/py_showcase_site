# Main Application
import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.jpg")

with col2:
    st.title("Otobong Peter")
    content = """
    My name is Otobong. I love building things. For me it is satisfying to tackle problems and finally figure out the solution.
    In this showcase page I update simple projects I have built with python.
    It is still a living and breathing project. I have been writing python since 2019, but I paused for a while to pursue my interest in blockchain technology.
    This year with my interests to pursue DevOps and Cloud, I had to get my python wheels oiled again.
    """
    st.info(content)

content = """Below are some of the projects I have worked on"""
st.write(content)


col3, empty, col4 = st.columns([1.5, 0.5, 1.5])

# Import the data
data = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, rows in data[:10].iterrows():
        st.header(rows["title"])
        img = "images/" + rows["image"]
        st.image(img)
        st.write(rows["description"])
        st.write(f"[Source Code]{rows['url']}")

with col4:
    for index, rows in data[10:].iterrows():
        st.header(rows["title"])
        img = "images/" + rows["image"]
        st.image(img)
        st.write(rows["description"])
        st.write(f"[Source Code]{rows['url']}")