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
    page_title="Projects",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    )

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
        <div class="header-title">🗄️ Projects</div>
    </div>
""", unsafe_allow_html=True)

# Set a fixed height for the iframes
iframe_height = 600


st.markdown("""
    <style>
    .center-header {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
        background: linear-gradient(to right, #e0eafc, #cfdef3);
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    </style>
    <div class="center-header">
        <h2 style="color: #011f4b; font-weight: 600;">📚 Research Projects</h2>
    </div>
""", unsafe_allow_html=True)

# Function to display PDF from a link
def display_pdf_from_link(pdf_link, height=600, width=700):
    pdf_display = f'<iframe src="{pdf_link}" width="{width}" height="{height}" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    with st.expander("📊 :blue[Research Slides] – Evaluating Tutor Training in A_STEP"):
        st.markdown("""
        **Project Overview:**  
        This study evaluates the **effectiveness and implementation** of skills, principles, and strategies in tutor training, based on data from the peer learning tutorial program, **Academic Tutorial Student Excellence Program (A_STEP)** at the **University of the Free State (UFS)**.
        
        🔗 [View Slides (PDF)](https://www.siyaphumelela.org.za/documents/66a368f4ab274.pdf)  
        📅 **Presented at**: Siyaphumelela Conference, June 2024
        """)

        # Optional: display PDF inline (if you want)
        # display_pdf_from_link("https://www.siyaphumelela.org.za/documents/66a368f4ab274.pdf", height=600, width=500)

with col2:
    with st.expander("🛰️ :blue[Research Paper] – Temporal Analysis of PKS 1510-089"):
        st.markdown("""
        **Project Overview:**  
        A temporal variability analysis of the **blazar PKS 1510-089** using optical and gamma-ray data.  
        The study investigates **multi-wavelength flaring activity (2014–2015)**, performs **correlation analysis**, and estimates the emission region's distance from the central **supermassive black hole**.

        🔗 [View Paper (PDF)](https://pos.sissa.it/426/053/pdf)  
        📍 **Conference**: High Energy Astrophysics in Southern Africa 2022- HEASA2022
        """)

        # Optional: display PDF inline
        # display_pdf_from_link("https://pos.sissa.it/426/053/pdf", height=600, width=500)



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






