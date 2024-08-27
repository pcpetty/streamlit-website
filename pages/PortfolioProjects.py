
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

# def app():
#     st.title("Portfolio Projects")
#     st.write("This page showcases the various projects I have worked on.")
#     # Add your project descriptions, images, and links here

# if __name__ == '__main__':
#     app()


# Define the pages
PAGES = {
    "Portfolio Projects": portfolio_projects_app,
    "Resume": resume_app
}

# selection = st.sidebar.selectbox("Navigate to", list(PAGES.keys()))
# if selection == "Thank You":
#     from pages.ThankYou import app as thank_you_app
#     thank_you_app()

# # Display the selected page
# page = PAGES[selection]
# page()


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

# lottie_coding = load_lottieurl("https://lottie.host/29566be6-b0c1-4a36-91b7-a01a35804ce4/f89ZcyMIr8.json")
# if lottie_coding:
#     st_lottie(lottie_coding, height=300, key="coding_animation")

lottie_coding_2 = load_lottieurl("https://lottie.host/b62eb4cd-7f70-48de-a305-b2c146d88f63/D2Xpvp7fKX.json")




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


# ---- FoodWheel Project

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV files from GitHub
orders_url = "https://github.com/pcpetty/streamlit-website/blob/0e355db7373f6798e11a32d366b0a323d4968066/pages/orders.csv"
restaurants_url = "https://github.com/pcpetty/streamlit-website/blob/0e355db7373f6798e11a32d366b0a323d4968066/pages/restaurants.csv"

df_cleveland = pd.read_csv(cleveland_url)
df_orders = pd.read_csv(orders_url)
df_restaurants = pd.read_csv(restaurants_url)

# Display the data in Streamlit
st.title("Cleveland Heart Disease Analysis")
st.write("### Cleveland Data Overview")
st.dataframe(df_cleveland.head())

st.title("FoodWheel Analysis")
st.write("### Orders Data Overview")
st.dataframe(df_orders.head())

st.write("### Restaurants Data Overview")
st.dataframe(df_restaurants.head())

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
# if st.checkbox("Show Conservation Status Pie Chart"):
# Calculate the conservation status proportions
conservation_proportion = species_df['conservation_status'].value_counts().astype(float)

# Define a custom color palette to match the orange and black theme
color_palette = sns.color_palette(['#FF7F0E', '#2E2E2E', '#FFA07A', '#D3D3D3', '#000000'])

# Plot the 2D pie chart with labels
if st.checkbox("Show Conservation Status Pie Chart"):
    fig, ax = plt.subplots(figsize=(6, 6))  # Adjusted figure size for better layout
    fig.patch.set_facecolor('#1e1e1e')  # Match the background color of the page
    wedges, texts, autotexts = ax.pie(
        conservation_proportion,
        labels=conservation_proportion.index,  # Add labels to the slices
        autopct='%1.1f%%',
        startangle=140,
        colors=color_palette
    )

    # Change the color of the percentages to white
    for autotext in autotexts:
        autotext.set_color('white')

    plt.title('Proportion of Conservation Statuses Across All Species', pad=20, color='white')

    # Add a legend outside the pie chart
    ax.legend(wedges, conservation_proportion.index, title="Conservation Status", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize='small')

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

# ---

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

