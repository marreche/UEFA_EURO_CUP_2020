import streamlit as st
from pages.tournament import tournament_page
from pages.home import home_page
from pages.squads import squads_page

st.set_page_config(
    page_title="Euro 2020",
    initial_sidebar_state="collapsed"
)


st.sidebar.title('Navigation')
selection = st.sidebar.radio(
    "Go to",
    ("Home", "Tournament", "Squads"))

if selection == "Tournament":
    tournament_page()
elif selection == "Squads":
    squads_page()
else:
    home_page()