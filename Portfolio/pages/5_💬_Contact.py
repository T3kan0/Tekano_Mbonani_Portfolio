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



st.markdown("""
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    </style>
    <div class="center">
        <h1 style="color: dimgrey;">Contact Me</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    </style>
    <div class="center">
        <h3 style="color: dimgrey;">Thank you for visiting my portfolio!</h3>
    </div>
""", unsafe_allow_html=True)


# NO CODE TOOL

WEBHOOK_URL = 'https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZkMDYzNDA0MzU1MjZiNTUzMDUxMzci_pc'

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email) is not None

#def contact_form():
with st.form('contact_form'):
    name = st.text_input('First Name')
    email = st.text_input('Email Adress')
    message = st.text_area('Your Message')
    submit_button = st.form_submit_button('submit')

    if submit_button:
        if not WEBHOOK_URL:
            st.error(
                'Email service is not set up. Please try again later.'
            )
            st.stop()
        if not name:
            st.error('Please provide your name.', icon='👨🏼')
            st.stop()
        if not email:
            st.error('Please provide your email address.', icon='📧')
            st.stop()
        if not is_valid_email(email):
            st.error('Please provide a valid email address.', icon='📧')
            st.stop()
        
        if not message:
            st.error('Please provide a message.', icon='💬')
            st.stop()
        #prepare the data payload and send it to the specified webhook URL
        data = {'email':email, 'name':name, 'message':message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success('Your message has beenn sent successfully!', icon='💬')
        else:
            st.error('There was an error sending your message!', icon='😧')








            

