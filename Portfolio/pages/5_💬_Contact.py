#!/usr/bin/env python
# coding: utf-8
import scipy.stats as stats
from scipy.stats import f_oneway
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import numpy as np
import pandas as pd
from PIL import Image
import base64
from PIL import Image
from io import BytesIO
import streamlit as st
import streamlit.components.v1 as components
import requests
import re


# --- LOAD CSS, PDF & PROFIL PIC ---
#with open('config.css') as f:
    #st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.markdown("""
    <style>
    .header-container {
        background: linear-gradient(to right, #dbe9f4, #ffffff);
        padding: 2rem;
        border-radius: 10px;
        border: 2px solid #011f4b;  /* Added border */ 
        box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .header-title {
        text-align: center;
        color: #011f4b;
        font-size: 3rem;
        font-weight: bold;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    </style>
    <div class="header-container">
        <div class="header-title">📩 Contact Me</div>
    </div>
""", unsafe_allow_html=True)

# NO CODE TOOL

WEBHOOK_URL = 'https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZkMDYzNDA0MzU1MjZiNTUzMDUxMzci_pc'

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email) is not None

def contact_form():
    
    with st.form('contact_form'):
        name = st.text_input('👤 First Name', placeholder="Your name")
        email = st.text_input('📧 Email Address', placeholder="you@example.com")
        message = st.text_area('💬 Your Message', placeholder="Type your message here...")
        submit_button = st.form_submit_button('Send Message')

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later.")
                st.stop()

            # Field validations
            if not name:
                st.error("Please provide your name. 🙋")
                st.stop()
            if not email:
                st.error("Please provide your email address. 📧")
                st.stop()
            if not is_valid_email(email):
                st.error("That doesn't look like a valid email address. 🚫")
                st.stop()
            if not message:
                st.error("Message field can't be empty. 📝")
                st.stop()

            # Prepare and send
            data = {"name": name, "email": email, "message": message}
            try:
                response = requests.post(WEBHOOK_URL, json=data, timeout=10)
                if response.status_code == 200:
                    st.success(f"✅ Thanks {name}, your message has been sent!")
                else:
                    st.error("😕 Something went wrong. Please try again later.")
            except requests.exceptions.RequestException:
                st.error("🚫 Network error. Please check your connection.")

    st.markdown("</div>", unsafe_allow_html=True)

# Call the function
contact_form()

st.markdown("""
    <style>
    .closing-message {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 120px;
        background: linear-gradient(to right, #dbe9f4, #e6e6e6);
        border-radius: 12px;
        border: 2px solid #011f4b;  /* Added border */
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-top: 40px;
        font-family: 'Segoe UI', sans-serif;
    }
    .closing-message h3 {
        color: #dbe9f4;
        font-weight: 600;
        font-size: 22px;
        text-align: center;
    }
    </style>
    <div class="closing-message">
        <h3>👋 Thank you for visiting my portfolio!<br>Let's connect and create something impactful </h3>
    </div>
""", unsafe_allow_html=True)





            

