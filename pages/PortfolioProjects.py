
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
from Resume import app as resume_app
from PortfolioProjects import app as portfolio_projects_app

def app():
    st.title("Portfolio Projects")
    st.write("This page showcases the various projects I have worked on.")
    # Add your project descriptions, images, and links here

if __name__ == '__main__':
    app()


# Add JavaScript to ensure the page starts at the top when loaded
st.markdown("""
    <script>
    window.scrollTo(0, 0);
    </script>
""", unsafe_allow_html=True)

# Add a decorative top banner with navigation links
st.markdown("""
    <div style="background-color:#f5a623;padding:20px;border-radius:10px;margin-bottom:20px;">
        <h1 style="color:#1e1e1e;text-align:center;font-weight:800;">Cole's Data Science Portfolio</h1>
        <p style="text-align:center;">
            <a href='/' style="color:#1e1e1e;font-weight:bold;margin-right:40px;text-decoration:none;">Home</a>
            <a href='/PortfolioProjects' style="color:#1e1e1e;font-weight:bold;margin-right:40px;text-decoration:none;">Portfolio Projects</a>
            <a href='/Resume' style="color:#1e1e1e;font-weight:bold;text-decoration:none;">Resume</a>
        </p>
    </div>
""", unsafe_allow_html=True)

# Define the pages
PAGES = {
    "Portfolio Projects": portfolio_projects_app,
    "Resume": resume_app
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()), key="navigation")

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
    /* Sidebar button decoration */
    .css-18ni7ap {
        background-color: #f5a623 !important;
        color: #1e1e1e !important;
        border-radius: 5px;
        border: none;
        padding: 8px;
        margin: 5px;
    }
    .css-18ni7ap:hover {
        background-color: #d48c20 !important;
        color: #ffffff !important;
    }
    /* Sidebar button when active */
    .stRadio > label {
        font-weight: bold;
        color: #f5a623;
    }
    .stRadio > div > label > div {
        background-color: #2b2b2b;
        color: #f5a623;
        padding: 8px;
        border-radius: 5px;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .stRadio > div > label > div:hover {
        background-color: #f5a623;
        color: #1e1e1e;
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

# Load Assets (Lottie Animation)
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for HTTP errors
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Failed to parse JSON response")
    return None

lottie_coding = load_lottieurl("https://lottie.host/29566be6-b0c1-4a36-91b7-a01a35804ce4/f89ZcyMIr8.json")
if lottie_coding:
    st_lottie(lottie_coding, height=300, key="coding_animation")

lottie_coding_2 = load_lottieurl("https://lottie.host/embed/b62eb4cd-7f70-48de-a305-b2c146d88f63/D2Xpvp7fKX.json")




# --- What I Do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Global EV Sales Data Analysis")
        st.write("""
        Developed a comprehensive data analysis project focused on electric vehicle (EV) sales and market trends. Utilized Python, Pandas, and Seaborn to filter, clean, and visualize data. Key achievements include:
        """)
        st.markdown("""
        - **Dynamic Visualizations:** Created interactive visualizations to track EV sales growth and market share by region.
        - **Advanced Data Cleaning:** Implemented sophisticated data cleaning techniques to handle missing values and standardize data formats.
        - **Trend Analysis:** Analyzed correlations between EV stock share and sales share, uncovering critical trends and insights.
        - **Streamlit Deployment:** Deployed the project on Streamlit, making the analysis interactive and accessible.
        """)
        st.markdown("[View on GitHub](https://github.com/pcpetty/Coles-Data-Scientist-Portfolio.git)")

    with right_column:
        st_lottie(lottie_coding_2, height=300, key="")

# ---
