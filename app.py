import os
import requests
from PIL import Image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import random

st.set_page_config(page_title="Cole's Data Scientist Portfolio", layout="wide")

# --- CSS THEME
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
    input, textarea {
        background-color: #2b2b2b;
        color: #f5a623;
        border: 1px solid #f5a623;
        border-radius: 5px;
    }
    input::placeholder, textarea::placeholder {
        color: #f5a623;
    }
    /* Images */
    .stImage {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
""", unsafe_allow_html=True)

# ---

# --- Load CSS ---
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        print(f"File not found: {file_name}")

local_css("/Users/colepetty/Desktop/Python Portfolio Website/website_style/style.css")

# --- Load Assets ---
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
    # Proceed with processing the lottie animation
    pass
else:
    print("Failed to load lottie animation")

# --- Load Image ---
file_path = r"/Users/colepetty/Desktop/Python Portfolio Website/images/websiteimage1.png"
if os.path.exists(file_path):
    img_contact_form = Image.open(file_path)
else:
    print(f"File not found: {file_path}")
    img_contact_form = None  # Define as None if not found

# --- Define Magic 8 Ball Function ---
def magic_8_ball():
    responses = [
        "Yes, definitely!",
        "It is certain.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    return random.choice(responses)

# --- HEADER SECTION ---
with st.container():
    st.subheader("Welcome!")
    st.title("Hi, I'm Cole, A Data Scientist From Columbus")
    st.write("Based in Columbus, OH, I bring a unique blend of analytical skills, operational expertise, and a passion for technology-driven solutions. With a strong background in safety management and operations, I have successfully streamlined processes to enhance efficiency and reduce costs in high-pressure environments. My experience spans across managing fleet compliance, optimizing warehousing systems, and leading teams to achieve strategic goals. With a dual degree in Business Administration and Psychology, I combine technical acumen with a deep understanding of organizational behavior, driving impactful results in every project I undertake. Let's connect and explore how data and technology can transform business operations.")
    st.write("[Check out my portfolio projects!](https://github.com/pcpetty/Coles-Data-Scientist-Portfolio.git)")

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

    # Lottie Files on right column lottiefiles.com
    with right_column:
        st_lottie(lottie_coding, height=300, key="")

## --- Projects ---
with st.container():
    st.markdown("## 🌟 Machine Learning Project: Income Classification using Logistic Regression")
    st.write("""
    This project focuses on predicting whether an individual's income exceeds $50K per year using Logistic Regression.
    The dataset used is the Census Income dataset from the UCI Machine Learning Repository.
    
    **Key Highlights:**
    - **Data Preprocessing:** Implemented techniques to clean and prepare the data for model training.
    - **Feature Engineering:** Extracted relevant features to improve model accuracy.
    - **Model Training:** Utilized Logistic Regression to classify income levels with high accuracy.
    - **Model Evaluation:** Assessed the model performance using accuracy, precision, recall, and F1 score.
    
    This project demonstrates my ability to apply machine learning techniques to solve real-world problems effectively.
    """)

    st.markdown("[View on GitHub](https://github.com/pcpetty/Coles-Data-Scientist-Portfolio.git)")

# --- Magic 8 Ball Section ---
st.write("---")
st.markdown('</div>', unsafe_allow_html=True)
st.header("Magic 8 Ball")
st.write("Ask the Magic 8 Ball a question and see what it predicts!")

question = st.text_input("Your question:")
if st.button("Ask the Magic 8 Ball"):
    answer = magic_8_ball()
    st.write(f"🎱 Magic 8 Ball says: **{answer}**")
st.markdown('</div>', unsafe_allow_html=True)

# --- Resume Section Master ---
# Custom CSS for styling
st.markdown("""
    <style>
    .resume-section {
        padding: 10px;
        background-color: #f9f9f9;
        border-radius: 5px;
    }
    .resume-header {
        font-size: 30px;
        font-weight: bold;
        color: #333;
    }
    .resume-subheader {
        font-size: 20px;
        font-weight: bold;
        color: #555;
        margin-top: 20px;
    }
    .resume-details {
        font-size: 16px;
        color: #666;
        margin-bottom: 10px;
    }
    .resume-projects {
        margin-top: 20px;
    }
    .project-title {
        font-size: 18px;
        font-weight: bold;
        color: #444;
    }
    .project-description {
        font-size: 16px;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# Resume Header
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

# --- Contact Section ---
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/colepetty57@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # CSS for styling the form
    st.markdown(
        """
        <style>
        input[type=message], input[type=email], input[type=text], textarea {
          width: 100%; /* Full width */
          padding: 12px; /* Some padding */ 
          border: 1px solid #ccc; /* Gray border */
          border-radius: 4px; /* Rounded borders */
          box-sizing: border-box; /* Make sure that padding and width stays in place */
          margin-top: 6px; /* Add a top margin */
          margin-bottom: 16px; /* Bottom margin */
          resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
        }

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

        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )
