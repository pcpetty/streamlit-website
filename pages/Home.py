
import streamlit as st
import os
import requests
from PIL import Image
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from streamlit_lottie import st_lottie
import random

def app():
    st.title("Welcome to My Data Scientist Portfolio")
    st.write("This is the homepage of the portfolio.")
    # Add your content here

if __name__ == '__main__':
    app()

# --- CSS THEME ---
st.markdown("""
    <style>
    /* General Theme */
    body {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stApp {
        background-color: #1e1e1e;
    }
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #f5a623;
        font-weight: 700;
    }
    /* Text */
    p, li {
        font-size: 18px;
        line-height: 1.6;
        color: #d3d3d3;
    }
    /* Links */
    a {
        color: #f5a623;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    /* Buttons */
    .stButton>button {
        background-color: #f5a623;
        color: #1e1e1e;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #d48c20;
        color: #ffffff;
    }
    /* Containers */
    .stContainer {
        background-color: #2b2b2b;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    /* Input Fields */
    input[type=email], input[type=text], textarea {
        background-color: #2b2b2b;
        color: #f5a623;
        border: 1px solid #f5a623;
        border-radius: 5px;
        width: 100%;
        padding: 12px;
        margin-top: 6px;
        margin-bottom: 16px;
        box-sizing: border-box;
    }
    input::placeholder, textarea::placeholder {
        color: #f5a623;
    }
    /* Images */
    .stImage {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    /* Contact Form Button */
    button[type=submit] {
        background-color: #04AA6D;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    button[type=submit]:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)
