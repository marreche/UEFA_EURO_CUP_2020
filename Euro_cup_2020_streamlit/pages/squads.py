import streamlit as st
from support.api_connect import get_teams


def squads_page(add_selectbox="Squads"):
    st.title("EURO CUP 2020 SQUADS PAGE")