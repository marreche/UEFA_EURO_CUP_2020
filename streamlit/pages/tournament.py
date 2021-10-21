import streamlit as st
from support.api_connect import get_teams


def tournament_page(add_selectbox="tournament"):
    st.title("EURO CUP 2020 TOURNAMENT PAGE")
    st.caption(get_teams())
    
    