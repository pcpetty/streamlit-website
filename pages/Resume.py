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

def app():
    st.title("Resume")
    st.write("This page contains my professional resume.")
    # You can embed your resume PDF, or list your work experience, skills, and education here

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

# --- Resume Section ---
st.markdown("""
    <style>
    .resume-section {
        background-color: #1e1e1e; /* Dark background for contrast */
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .resume-header {
        font-size: 32px;
        font-weight: bold;
        color: #FF7F0E; /* Orange color for header text */
        text-align: center;
    }
    .resume-subheader {
        font-size: 22px;
        font-weight: bold;
        color: #FF7F0E; /* Orange color for subheader text */
        margin-top: 20px;
        text-align: left;
    }
    .resume-details {
        font-size: 16px;
        color: #FFFFFF; /* White text for readability */
        line-height: 1.6;
        margin-bottom: 10px;
    }
    .resume-details ul {
        padding-left: 20px;
    }
    .resume-details li {
        margin-bottom: 10px;
    }
    .resume-projects {
        margin-top: 20px;
    }
    .project-title {
        font-size: 18px;
        font-weight: bold;
        color: #FF7F0E; /* Orange color for project titles */
    }
    .project-description {
        font-size: 16px;
        color: #FFFFFF; /* White text for readability */
    }
    a {
        color: #FFA07A; /* Softer orange for links */
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="resume-section">
    <div class="resume-header">
        Cole Petty
    </div>
    <div class="resume-details">
        Columbus, OH 43212 | (740) 525-3738 | colepetty57@gmail.com | <a href="https://linkedin.com/in/cole-petty-095027121" target="_blank">LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("""
<div class="resume-section">
    <div class="resume-subheader">Skills</div>
    <div class="resume-details">
        <ul>
            <li><strong>Data Science Skills:</strong> Python, SQL, Pandas, NumPy, Matplotlib, Seaborn, Machine Learning (Scikit-learn), Data Cleaning, Data Visualization</li>
            <li><strong>Active Listening:</strong> Developed and maintained relationships company-wide to find and resolve safety issues.</li>
            <li><strong>Adaptability:</strong> Ability to respond quickly to changing trends, processes, and approaches to project goals.</li>
            <li><strong>Transportation Systems:</strong> Utilize software and technology to optimize fleet management and compliance.</li>
            <li><strong>Customer Service:</strong> Coordinated with vendors and customers to ensure timely completion of work orders.</li>
            <li><strong>Warehousing and Storage:</strong> Ensured goods are stored and handled safely and efficiently.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Experience Section
st.markdown("""
<div class="resume-section">
    <div class="resume-subheader">Experience</div>
    <div class="resume-details">
        <strong>Forward Air, Groveport, OH</strong> — Safety Generalist (03/2022 - Present)
        <ul>
            <li>Maintains fleet compliance and sustains the company’s safety rating with FMCSA.</li>
            <li>Documents and reviews all accidents and incidents using strong analytical skills.</li>
            <li>Manages multiple projects independently and handles high-stress situations efficiently.</li>
        </ul>
        <strong>Forward Air Solutions, Lockbourne, OH</strong> — Operations Manager (08/2020 - 02/2022)
        <ul>
            <li>Streamlined operations, reducing warehouse labor costs by 25%.</li>
            <li>Maintained an inventory accuracy of 89% by implementing a 3-factor freight verification process.</li>
        </ul>
        <strong>Scioto Services, Columbus, OH</strong> — Account Manager (07/2019 - 08/2020)
        <ul>
            <li>Managed a monthly budget of $15,000 to supply and upkeep a major corporate office.</li>
            <li>Oversaw the daily planning of 22 associates and 2 shift supervisors.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Education Section
st.markdown("""
<div class="resume-section">
    <div class="resume-subheader">Education and Certifications</div>
    <div class="resume-details">
        <strong>Ohio Wesleyan University, Delaware, OH</strong> — Bachelor of Arts Degree (2019)
        <ul>
            <li>Majors: Business Administration and Psychology (Organizational Behavior)</li>
        </ul>
        <strong>Certifications:</strong>
        <ul>
            <li>Data Scientist: Machine Learning — Codecademy (Aug 2024) | Credential ID: 66B22DB05A | <a href="https://www.codecademy.com" target="_blank">View Credential</a></li>
            <li>Data Scientist: Analytics — Codecademy (Jun 2024) | Credential ID: 66730BDA89 | <a href="https://www.codecademy.com" target="_blank">View Credential</a></li>
            <li>Learn Microsoft Excel for Data Analysis — Codecademy (Aug 2024) | Credential ID: 66B3B4DDDC | <a href="https://www.codecademy.com" target="_blank">View Credential</a></li>
            <li>Learn Python 3 — Codecademy (Jun 2024) | Credential ID: 66803CD763 | <a href="https://www.codecademy.com" target="_blank">View Credential</a></li>
            <li>OSHA 10-Hour & 30-Hour Training — 360training (Jul 2023) | Credential IDs: 26-707446395, 26-907460874 | <a href="https://www.360training.com" target="_blank">View Credential</a></li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)
