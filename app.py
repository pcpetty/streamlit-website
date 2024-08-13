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

# Setting the Streamlit page configuration
st.set_page_config(page_title="Cole's Data Scientist Portfolio", layout="wide")

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

# Define Magic 8 Ball Function
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

    with right_column:
        st_lottie(lottie_coding, height=300, key="")

# --- Machine Learning Project ---
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
    
# --- Bio Project ---
st.title("Biodiversity Analysis in National Parks")
st.markdown("""
This project explores the biodiversity across various national parks in the United States, 
focusing on conservation statuses and species diversity. The analysis includes data visualization, 
model implementation, and feature engineering to uncover insights into species endangerment.
""")

@st.cache
def load_data():
    species_url = 'https://raw.githubusercontent.com/pcpetty/Coles-Data-Scientist-Portfolio/pcpetty-patch-1/species_info.csv'
    observations_url = 'https://raw.githubusercontent.com/pcpetty/Coles-Data-Scientist-Portfolio/pcpetty-patch-1/observations.csv'
    return pd.read_csv(species_url), pd.read_csv(observations_url)

# Load the data
species_df, observations_df = load_data()

# Display Raw Data (Optional)
if st.checkbox("Show Raw Data"):
    st.write("Species DataFrame:")
    st.write(species_df)
    st.write("Observations DataFrame:")
    st.write(observations_df)

# Visualizations Section
st.subheader("Visualizations")

# Toggle to display pie chart
if st.checkbox("Show Conservation Status Pie Chart"):
    # Calculate the conservation status proportions
    conservation_proportion = species_df['conservation_status'].value_counts().astype(float)

    # Define a custom color palette to match the orange and black theme
    color_palette = sns.color_palette(['#FF7F0E', '#2E2E2E', '#FFA07A', '#D3D3D3', '#000000'])

# Plot the 2D pie chart with labels
if st.checkbox("Show Conservation Status Pie Chart"):
    fig, ax = plt.subplots(figsize=(6, 6))  # Adjusted figure size for better layout
    fig.patch.set_facecolor('#1e1e1e')  # Match the background color of the page
    ax.pie(
        conservation_proportion,
        labels=conservation_proportion.index,  # Add labels to the slices
        autopct='%1.1f%%',
        startangle=140,
        colors=color_palette
    )
    plt.title('Proportion of Conservation Statuses Across All Species', pad=20, color='white')
    plt.setp(ax.get_legend().get_texts(), color='white')
    st.pyplot(fig)
    
# Explanation of Pie Chart Percentages
st.markdown("""
### Explanation of Pie Chart Percentages
The pie chart above represents the distribution of species across various conservation statuses in the dataset. 
Each slice of the pie corresponds to a different conservation status, with the percentage indicating the proportion of species in that status relative to the total number of species in the dataset. 
""")
st.markdown("""
For example:
- **Endangered:** If the chart shows 10%, it means that 10% of all species in the dataset are classified as endangered.
- **Threatened:** If the chart shows 15%, it means that 15% of all species in the dataset are classified as threatened.
- **No Intervention:** The largest slice typically represents species not currently under any specific conservation status.
""")
st.markdown("""
These percentages help visualize how conservation efforts are distributed across different species and highlight areas where more attention might be needed.
""")

# Identify threatened species

threatened_species_df = species_df[species_df['conservation_status'].isin(['Endangered', 'Threatened'])]

# Merge with observations to get location data
threatened_species_with_location = pd.merge(threatened_species_df, observations_df, on='scientific_name')

# Display threatened species and their locations
st.subheader("List of Threatened Species and Their Locations")
st.dataframe(threatened_species_with_location[['common_names', 'scientific_name', 'category', 'conservation_status', 'park_name', 'observations']])

st.markdown("""
This table provides a detailed list of species that are categorized as endangered or threatened, along with the national parks where they are observed. 
This information is crucial for understanding which species are at risk and where conservation efforts may need to be focused.
""")

# Key Insights Section
st.subheader("Key Insights from the Research")
st.markdown("""
### Key Insights
1. **High Concentration of Species Without Conservation Status:**
   - A significant proportion of species across the national parks are classified under "No Intervention." This suggests that a large number of species are currently not under any specific conservation monitoring or protection efforts, which could be a potential area of concern.
   
2. **Endangered Species are Concentrated in Specific Parks:**
   - The data reveals that certain parks, such as [Park Name A] and [Park Name B], have a disproportionately high number of endangered species. These parks may require more focused conservation efforts to protect these vulnerable species.
   
3. **Certain Species Categories are More at Risk:**
   - Species belonging to certain categories, such as mammals and birds, are more likely to be classified as endangered or threatened. This indicates that conservation efforts may need to be more targeted towards these groups.
   
4. **Observation Efforts Vary Greatly by Park:**
   - The number of species observations recorded varies significantly across parks, suggesting that some parks may be under-surveyed. This uneven distribution of data could lead to gaps in understanding the true conservation needs of various species.

These insights provide a foundation for further research and conservation planning, helping to prioritize efforts where they are most needed.
""")

# Additional Visualizations (Placeholder)
# st.write("Add more visualizations here...")

# --- Magic 8 Ball Section ---

st.write("---")
st.header("Magic 8 Ball")
st.write("Ask the Magic 8 Ball a question and see what it predicts!")

question = st.text_input("Your question:")
if st.button("Ask the Magic 8 Ball"):
    answer = magic_8_ball()
    st.write(f"🎱 Magic 8 Ball says: **{answer}**")

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
        input[type=email], input[type=text], textarea {
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
