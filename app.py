import os
import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import random

st.set_page_config(page_title="Cole's Data Scientist Portfolio", layout="wide")

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
    st.write("I am passionate about using Python and Machine Learning to be more effective in business settings.")
    st.write("[Check out my portfolio projects! >](https://github.com/pcpetty/Coles-Data-Scientist-Portfolio.git)")

# --- What I Do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Data Analysis Projects")
        st.write("##")
        st.write("Highlights")

    # Lottie Files on right column lottiefiles.com
    with right_column:
        st_lottie(lottie_coding, height=300, key="")

# --- Projects ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if img_contact_form:
            st.image(img_contact_form)
        else:
            st.write("Image not available")
    with text_column:
        st.subheader("Hurricane Analysis in Python")
        st.write(
            """
            Analyzing Hurricane Severity
            """
        )
        st.markdown("[Code](https://github.com/pcpetty/Data-Analyst-Portfolio.git)")

# --- Magic 8 Ball Section ---
st.write("---")
st.header("Magic 8 Ball")
st.write("Ask the Magic 8 Ball a question and see what it predicts!")

question = st.text_input("Your question:")
if st.button("Ask the Magic 8 Ball"):
    answer = magic_8_ball()
    st.write(f"🎱 Magic 8 Ball says: **{answer}**")

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

    if img_contact_form:
        st.image(img_contact_form, width=300)
