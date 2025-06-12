#!/usr/bin/env python
# coding: utf-8
import scipy.stats as stats
from scipy.stats import f_oneway
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import numpy as np
import pandas as pd
from io import BytesIO
import streamlit as st
import streamlit.components.v1 as components
from datetime import date
from PIL import Image
import requests


st.set_page_config(
    page_title="TekanoMbonani",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
    )

# --- LOAD CSS, PDF & PROFIL PIC ---
# URL of your CSS file on GitHub
url = "https://raw.githubusercontent.com/T3kan0/Tekano_Mbonani_Portfolio/main/config0.css"

# Fetch the content
response = requests.get(url)
#if response.status_code == 200:
    #css_content = response.text
    #st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
#else:
    #st.error("Failed to fetch CSS. Check the URL or connection.")


st.markdown("""
    <style>
    .intro-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 200px;
        background: linear-gradient(to right, #b3cde0, #ffffff);
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .intro-title {
        font-size: 2.8rem;
        font-weight: bold;
        color: #011f4b;
        margin-bottom: 0.5rem;
    }
    .intro-subtitle {
        font-size: 1.3rem;
        font-style: italic;
        color: #7f8c8d;
    }
    </style>

    <div class="intro-container">
        <div class="intro-title">Tekano Mbonani, M.Sc.</div>
        <div class="intro-subtitle">Welcome To My Portfolio</div>
    </div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns([25, 50, 25])

with c2:
    st.markdown("""
        <style>
        .profile-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }

        .profile-image {
            width: 60%;
            max-width: 320px;
            border-radius: 20px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
            border: 4px solid #b3cde0;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }

        .profile-image:hover {
            transform: scale(1.03);
            border-color: #011f4b;
        }
        </style>

        <div class="profile-container">
            <img class="profile-image" src="https://i.postimg.cc/BQnYw23B/image.png" alt="Tekano Mbonani"/>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <hr style="border: 2px solid #b3cde0;">
""", unsafe_allow_html=True)

# Socials

EMAIL = 'mbonanits@ufs.ac.za'

SOCIAL_MEDIA = {
    'LinkedIn': ('https://linkedin.com/in/tekano-mbonani', 'https://cdn-icons-png.flaticon.com/512/174/174857.png'),
    'Github': ('https://github.com/T3kan0', 'https://cdn-icons-png.flaticon.com/512/733/733553.png'),
    'Streamlit': ('https://share.streamlit.io/user/t3kan0', 'https://streamlit.io/images/brand/streamlit-mark-color.svg'),
    'Upwork': ('https://www.upwork.com/freelancers/~017eff56853580df4c?mp_source=share', 'https://cdn.worldvectorlogo.com/logos/upwork-1.svg')
}

# --- Style for hover & layout ---
st.markdown("""
    <style>
    .social-icon {
        width: 40px;
        height: 40px;
        margin-bottom: 6px;
        transition: transform 0.2s ease-in-out;
    }
    .social-icon:hover {
        transform: scale(1.15);
    }
    .social-label {
        font-size: 0.9rem;
        color: #2c3e50;
        text-align: center;
        margin-top: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Layout social media in a row using columns ---
cols = st.columns(len(SOCIAL_MEDIA))

for col, (platform, (url, icon)) in zip(cols, SOCIAL_MEDIA.items()):
    col.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="{url}" target="_blank">
                <img src="{icon}" class="social-icon" alt="{platform} icon"/>
            </a>
            <div class="social-label">{platform}</div>
        </div>
    """, unsafe_allow_html=True)

# --- Optional: email centered below ---
st.markdown(f"""
    <div style='text-align: center; margin-top: 20px; font-size: 0.9rem; color: grey;'>
        📧 <a href="mailto:{EMAIL}" style="color: #6c63ff;">{EMAIL}</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .icon-header {
        text-align: center;
        font-size: 36px;
        color: #011f4b;
        font-weight: bold;
        margin-top: 30px;
    }

    .icon-header span {
        display: inline-block;
        margin-right: 10px;
    }
    </style>

    <div class="icon-header">
        Professional Summary
    </div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #378cfc;">
    <h4 style="margin-top: 0;">🌟 <strong>Professional Snapshot</strong></h4>
    <ul style="line-height: 1.8; font-size: 16px; color: #333;">
        <li><strong style="color:#FFA500;">Data Analyst</strong>, <strong style="color:#FF4B4B;">Web App Developer</strong>, and <strong style="color:#2ECC71;">Researcher</strong> with a passion for extracting insights through predictive modeling and statistical methods.</li>
        <li>Holder of an <strong>M.Sc. in Astrophysics</strong>, with aspirations to advance in the field of astronomical research.</li>
        <li>Experienced tutor in <strong style="color:#FF4B4B;">Python</strong>, <strong style="color:#FF4B4B;">R</strong>, Mathematics, and Physics — delivered both <em>online</em> and <em>face-to-face</em>.</li>
        <li>Excellent communicator with strong <em>verbal and written</em> skills, adept at simplifying complex topics.</li>
        <li>Freelance <strong>Data Consultant</strong>, bridging data and decision-making for diverse clients.</li>
    </ul>
</div>
""", unsafe_allow_html=True)


st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)


st.markdown("""
<h3 style="color: dimgrey;" align="center">Languages and Tools:</h3>
<div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px;">
    <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer">
        <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="60" height="60"/>
    </a>
    <a href="https://d3js.org/" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/d3js/d3js-original.svg" alt="d3js" width="60" height="60"/>
    </a>
    <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer">
        <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="60" height="60"/>
    </a>
    <a href="https://dotnet.microsoft.com/" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/dot-net/dot-net-original-wordmark.svg" alt="dotnet" width="60" height="60"/>
    </a>
    <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer">
        <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="60" height="60"/>
    </a>
    <a href="https://git-scm.com/" target="_blank" rel="noreferrer">
        <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="60" height="60"/>
    </a>
    <a href="https://www.linux.org/" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="60" height="60"/>
    </a>
    <a href="https://www.mathworks.com/" target="_blank" rel="noreferrer">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" alt="matlab" width="60" height="60"/>
    </a>
    <a href="https://www.microsoft.com/en-us/sql-server" target="_blank" rel="noreferrer">
        <img src="https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg" alt="mssql" width="60" height="60"/>
    </a>
    <a href="https://www.mysql.com/" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="60" height="60"/>
    </a>
    <a href="https://www.postgresql.org" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="60" height="60"/>
    </a>
    <a href="https://www.python.org" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/>
    </a>
    <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer">
        <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="60" height="60"/>
    </a>
</div>
""", unsafe_allow_html=True)

