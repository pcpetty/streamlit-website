import streamlit as st

def app():
    st.title("Resume")
    st.write("This page contains my professional resume.")
    # You can embed your resume PDF, or list your work experience, skills, and education here

if __name__ == '__main__':
    app()


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
