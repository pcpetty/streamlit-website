
import streamlit as st
from Home import app as home_app
from Page1 import app as page1_app

PAGES = {
    "Home": home_app,
    "Page 1": page1_app
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Display the selected page
page = PAGES[selection]
page()
