#!/usr/bin/env python
# coding: utf-8
import scipy.stats as stats
from scipy.stats import f_oneway
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import numpy as np
import pandas as pd
from PyPDF2 import PdfWriter

import base64

import streamlit as st



st.set_page_config(
    page_title="A_STEP_Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    )

# --- LOAD CSS, PDF & PROFIL PIC ---
#with open('config.css') as f:
    #st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Set a fixed height for the iframes
iframe_height = 600

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
        <h1 style="color: dimgrey;">Projects</h1>
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
        <h4 style="color: dimgrey;">Research</h4>
    </div>
""", unsafe_allow_html=True)

st.sidebar.write('Welcome')


# Function to display PDF
def display_pdf(file_path, height=600, width=700):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="{width}" height="{height}" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)




col1, col2 = st.columns([50, 50])


with col1:
    with st.expander(":blue[Research Slides]: Evaluating the effectiveness and implementation of skills, principles and strategies in tutor training."):
        st.markdown("Based on the tutor training data sample of the peer learning tutorial program; Academic Tutorial Student Excellence Program (A_STEP) at the University of the Free State (UFS). For more details, visit [Project Link](https://example.com).")
       
        # Display the PDF inline
        display_pdf("/pages/HEASA2022_053.pdf", height=iframe_height, width=500)  # Adjust width here as needed        
with col2:
    with st.expander(":blue[Research Paper]: Physical inference from the temporal analysis of PKS 1510-089 during the 2014 - 2015 multi-wavelength flaring events."):
        st.markdown("The optical and gamma-ray temporal variability analysis of the quasar PKS 1510-089. Results include correlation studies and locating the emission region distance from the central supermassive black hole. For more details, visit [Project Link](https://example.com).")
        
        display_pdf("https://github.com/T3kan0/Tekano_Mbonani_Portfolio/blob/main/Portfolio/pages/HEASA2022_053.pdf", height=iframe_height, width=500)  # Adjust width here as needed

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
        <h4 style="color: dimgrey;">Python</h4>
    </div>
""", unsafe_allow_html=True)


col3, col4, col5 = st.columns([1, 1, 1])
col3.markdown('''
    <div style="text-align: center;">
        <a href="https://www.python.org" target="_blank" rel="noreferrer">
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/>
        </a>
    </div>    
    ''', unsafe_allow_html=True)
col3.markdown("[![Github](https://img.shields.io/badge/GitHub-Project)](https://github.com/T3kan0/Web_Scrapper)", unsafe_allow_html=True)
with col3:
    with st.expander(":blue[Project 1]: Web Scrapping"):
        st.markdown("The pipelne downloads documents from online using links. For more details, visit [Project Link](https://github.com/T3kan0/Web_Scrapper).")



col4.markdown('''
    <div style="text-align: center;">
        <a href="https://www.python.org" target="_blank" rel="noreferrer">
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/>
        </a>
    </div>    
    ''', unsafe_allow_html=True)
col4.markdown("[![App](https://img.shields.io/badge/Live_App-Link)](https://github.com/T3kan0/Polynomial_Regression)")

with col4:
    with st.expander(":blue[Project 2]: ML - Polynomial Regression"):
        st.markdown("A polynomial machine learning algorithm trained and tested. For more details, visit [Project Link](https://github.com/T3kan0/Polynomial_Regression).")



col5.markdown('''
    <div style="text-align: center;">
        <a href="https://www.python.org" target="_blank" rel="noreferrer">
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/>
        </a>
    </div>    
    ''', unsafe_allow_html=True)
col5.markdown("[![Research](https://img.shields.io/badge/Research-Output)](https://github.com/T3kan0/Light_Curve_Temp_Profile)")
with col5:
    with st.expander(":blue[Project 3]: Time-Series Modeling"):
        st.markdown("An exponential fit of gamma-ray light-curves to extract rise and fall times. For more details, visit [Project Link](https://github.com/T3kan0/Light_Curve_Temp_Profile).")

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
        <h4 style="color: dimgrey;">Power BI</h4>
    </div>
""", unsafe_allow_html=True)


col6, col7 = st.columns(2)
with col6:
    with st.expander(":blue[Project 1]: One-on-One Tutorials"):       
        st.markdown("""
        <style>
        .center-image {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        .center-image img {
            max-width: 100%; /* Ensures the image doesn't exceed the expander width */
            height: auto;    /* Maintain aspect ratio */
        }
        </style>
        <div class="center-image">
            <img src="https://i.postimg.cc/rFxn6sQn/bi1.png" alt="Alt Text"/>
        </div>
        """, unsafe_allow_html=True)
with col7:
    with st.expander(":blue[Project 2]: A_STEP Longitudinal Tutorials"):       
        st.markdown("""
        <style>
        .center-image {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        .center-image img {
            max-width: 100%; /* Ensures the image doesn't exceed the expander width */
            height: auto;    /* Maintain aspect ratio */
        }
        </style>
        <div class="center-image">
            <img src="https://i.postimg.cc/PJbJKHhq/longitudinal.png" alt="Alt Text"/>
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
        <h4 style="color: dimgrey;">Web Apps</h4>
    </div>
""", unsafe_allow_html=True)

col8, col9 = st.columns(2)
with col8:
    with st.expander(":blue[Project 1]: MARS"):       
        st.markdown("Merges tutorial attendance register files. For more, visit [MARS](https://marsv100-da5bwqvb8pdtbck8yjqdme.streamlit.app/).")
        st.markdown("""
        <style>
        .center-image {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        .center-image img {
            max-width: 100%; /* Ensures the image doesn't exceed the expander width */
            height: auto;    /* Maintain aspect ratio */
        }
        </style>
        <div class="center-image">
            <img src="https://i.postimg.cc/zDn21QGS/MARS.png" alt="Alt Text"/>
        </div>
        """, unsafe_allow_html=True)

with col9:
    with st.expander(":blue[Project 2]: A.T&T.E"):       
        st.markdown("Analyses data & compiles PDF reports. For more, visit [A.T&T.E](https://module-evaluations-7n8wlbykdft8crfxmvl3pf.streamlit.app/).")
        st.markdown("""
        <style>
        .center-image {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        .center-image img {
            max-width: 100%; /* Ensures the image doesn't exceed the expander width */
            height: auto;    /* Maintain aspect ratio */
        }
        </style>
        <div class="center-image">
            <img src="https://i.postimg.cc/MZRNpTdB/ATTE.png" alt="Alt Text"/>
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
        <h4 style="color: dimgrey;">Websites</h4>
    </div>
""", unsafe_allow_html=True)






