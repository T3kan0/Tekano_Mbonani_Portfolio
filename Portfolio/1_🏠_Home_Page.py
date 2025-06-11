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
        background: linear-gradient(to right, #03396c, #ffffff);
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .intro-title {
        font-size: 2.8rem;
        font-weight: bold;
        color: #2c3e50;
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


EMAIL = 'mbonanits@ufs.ac.za'

SOCIAL_MEDIA = {
    'LinkedIn': ('https://linkedin.com/in/tekano-mbonani', 'https://cdn-icons-png.flaticon.com/512/174/174857.png'),
    'Github': ('https://github.com/T3kan0', 'https://cdn-icons-png.flaticon.com/512/733/733553.png'),
    'Streamlit': ('https://share.streamlit.io/user/t3kan0', 'https://streamlit.io/images/brand/streamlit-mark-color.svg'),
    'Upwork': ('https://www.upwork.com/freelancers/~017eff56853580df4c?mp_source=share', 'https://cdn.worldvectorlogo.com/logos/upwork-1.svg')
}



c1, c2, c3 = st.columns([25, 50, 25])

st.markdown("""
    <style>
    .center-image {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
    </style>
    <div class="center-image">
        <img src="https://i.postimg.cc/BQnYw23B/image.png" alt="Alt Text"/>
    </div>
""", unsafe_allow_html=True)

col12, col22 = st.columns([40, 60])

with col22:
    # Center email and download button
    st.write('📨', EMAIL)
    
    st.download_button(
        label=":blue[Download My Resume]",
        data="Resume data here",
        file_name="Tekano_Resume2023.pdf",
        mime="application/pdf"
    )

    
st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)


cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, (links, img_src)) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"""
    <div style="display: flex; justify-content: center; flex-direction: column; align-items: center;">
        <img src="{img_src}" alt="{platform}" style="width: 40px; height: 40px;"/>
        <a href="{links}" target="_blank" style="text-decoration: none; color: #378cfc; text-decoration: underline;">{platform}</a>
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
        <h1 style="color: dimgrey;">About Me</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

st.info('''
- ✅ Experienced :orange[Data Analyst], :red[Web-app Developer] and :green[Researcher] in data-oriented environment, with passion for delivering insights based on predictive modeling and other statistical methods. 
- ✅ Aspiring Astrophysicist currently with an MSc in Astrophysics.
- ✅ Tutor in programming languages :red[(Python and R)], Mathematics and Physics :red[(Online and Face-to-Face)].
- ✅ Strong verbal and written communication skills.
- ✅ Data Consultant.
''')

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

