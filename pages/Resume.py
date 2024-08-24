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

import streamlit as st

st.title("Cole Petty's Data Analyst Resume")

st.subheader("Contact Information")
st.write("""
**Location:** Columbus, OH 43212  
**Phone:** (740) 525-3738  
**Email:** colepetty57@gmail.com  
[LinkedIn Profile](https://linkedin.com/in/cole-petty-095027121)
""")

st.subheader("Professional Summary")
st.write("""
Detail-oriented Data Analyst with strong proficiency in Python, Excel, SQL, and data visualization tools such as Power BI and Tableau. Equipped with hands-on experience in data wrangling, cleaning, and analysis, coupled with a solid foundation in business operations and management. Adept at leveraging data to drive decision-making and improve operational efficiency. Recently certified in key data analytics and machine learning courses, showcasing a commitment to ongoing learning and development in the field. Seeking to apply analytical skills and data-driven insights to contribute to a dynamic team.
""")

st.subheader("Skills")
st.write("""
- **Programming Languages:** Python (Pandas, NumPy, Matplotlib, Scikit-learn)
- **Data Visualization:** Power BI, Tableau, Matplotlib, Seaborn
- **Data Analysis:** Excel (Advanced Functions, Pivot Tables), SQL, Data Wrangling, Data Cleaning, Data Mining
- **Machine Learning:** Logistic Regression, Decision Trees, Random Forest, Model Evaluation
- **Tools & Technologies:** Jupyter Notebook, VSCode, Git, Docker
- **Business Skills:** Strategic Planning, Budget Management, Operations Management
""")

st.subheader("Certifications")
st.write("""
- **Data Scientist Certification** – Codecademy
- **Machine Learning Certification** – Codecademy
- **Python 3 Certification** – Codecademy
- **Data Analysis & Excel Certification** – Codecademy
- **Business Intelligence Certification** – Codecademy
""")

st.subheader("Professional Experience")

st.markdown("""
**Safety Generalist (3 years)**  
*Forward Air, Groveport, OH | March 2019 – Present*
- Demonstrated reliability and consistency by maintaining fleet compliance with company and FMCSA standards for three consecutive years, contributing to sustained high safety ratings.
- Employed data-driven approaches to analyze accident and incident reports, improving documentation accuracy and reducing incident recurrence by 15%.
- Successfully managed multiple high-stress projects independently and within teams, optimizing safety protocols through data analysis.

**Operations Manager**  
*Forward Air Solutions, Lockbourne, OH | August 2020 – February 2022*
- Led a warehouse team to develop and implement process improvements, reducing labor costs by 25% through data-driven decision-making.
- Maintained an inventory accuracy of 89% by implementing a 3-factor verification process, minimizing lost and damaged freight.
- Used data analysis to identify inefficiencies and propose operational changes, directly improving service delivery and customer satisfaction.

**Account Manager**  
*Scioto Services, Columbus, OH | July 2019 – August 2020*
- Managed a monthly budget of $15,000 for a major corporate office, using financial data to optimize spending and reduce waste.
- Oversaw a team of 24 associates, using workforce analytics to ensure efficient staff deployment and operational coverage.
- Assisted in strategic territory development, leveraging data insights to expand service reach and client satisfaction.
""")

st.subheader("Education")
st.write("""
**Bachelor of Arts in Business Administration & Psychology**  
*Ohio Wesleyan University, Delaware, OH | 2019*  
Majors: Business Administration (Management), Psychology (Organizational Behavior)  
**OSHA 10 & 30 Hour Training Certification** – General Industry | 2023
""")

st.subheader("Projects")

st.markdown("""
**Endangered Species Analysis in National Parks**  
- Conducted a comprehensive data analysis project using Python to identify patterns in endangered species across U.S. national parks.
- Utilized data wrangling, cleaning, and visualization techniques to present findings, demonstrating the ability to derive actionable insights from large datasets.
- Project showcased in a Jupyter Notebook with clear documentation and visualizations, designed to communicate findings effectively to non-technical stakeholders.

**Credit Card Fraud Detection Using Logistic Regression**  
- Developed a machine learning model in Python to predict credit card fraud, achieving a high accuracy rate using logistic regression.
- The project involved data preprocessing, feature selection, model training, and evaluation, with results presented in a professional format.

**Wine Quality Analysis with Regularization**  
- Conducted a detailed analysis of wine quality datasets, employing regularization techniques such as Ridge and Lasso to prevent overfitting.
- Utilized Python and Scikit-learn to preprocess data, select features, and build predictive models that accurately classified wine quality.
- Presented findings in a comprehensive report, including visualizations that highlighted the impact of different regularization methods on model performance.
""")

