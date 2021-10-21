import streamlit as st
from pages.img.Euro import img

def home_page(add_selectbox = "home"):
    st.title("EURO CUP 2020 DASHBOARD")
    st.image(img)
    st.write("Welcome to my Euro Cup 2020 Dashboard")
    st.caption("The aim of this streamlit was to learn how to deploy a project. All data shown in this page is stored in a database hosted in MongoAtlas created by myself, scraped from different webpages, cleaned and manipulated by myself as well. After this process I created an API to serve as a hub between this dashboard and the database. Finally I created this dashboard to visualize the data.")
    st.caption("Navigate through the dashboard by using the sidebar to the left.")
    st.caption("- The Tournament tab displays match details, tournament matchups and more! ")
    st.caption("- The Squads tab displays details about the different teams involved, players details and such")