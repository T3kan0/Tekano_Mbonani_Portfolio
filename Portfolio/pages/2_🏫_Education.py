import scipy.stats as stats
from scipy.stats import f_oneway
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="EDU",
    page_icon="🎓",
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
        <div class="header-title">🎓 EDUCATION</div>
    </div>
""", unsafe_allow_html=True)

#st.markdown("""
#    <hr style="border: 2px solid #6497b1;">
#""", unsafe_allow_html=True)

# MSc
st.markdown("""
    <style>
    .edu-card {
        background-color: #f5f7fa;
        border-left: 6px solid #6497b1;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .edu-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #011f4b;
    }
    .edu-subtitle {
        font-size: 1rem;
        color: #7f8c8d;
    }
    .edu-date {
        float: right;
        font-weight: 600;
        color: #011f4b;
    }
    </style>

    <div class="edu-card">
        <div class="edu-title">🎓 Master of Science <span class="edu-subtitle">(Astrophysics)</span> 
            <span class="edu-date">2018 – 2024</span>
        </div>
        <div class="edu-subtitle">University of the Free State</div>
        <ul>
            <li><b>Thesis:</b> Probing the inner jet regions and emission mechanisms of the flat spectrum radio quasars 3C 279 and PKS 1510-089 through temporal and spectral variability studies</li>
            <li><b>GPA:</b> <strong style="color:#011f4b;">3.5 / 82.00%</strong></li>
            <li><b>Conferences:</b> 4 presented</li>
            <li><b>Publications:</b> 2 in Proceedings of Sciences</li>
        </ul>
        <div><b><strong style="color:#FFA500;">Skills:</strong></b> Astrophysics, Python, IRAF, Data Analysis, Oral and Written Communication</div>
    </div>
""", unsafe_allow_html=True)


# BSc H
st.markdown("""
    <style>
    .edu-card {
        background-color: #f5f7fa;
        border-left: 6px solid #6497b1;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .edu-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #011f4b;
    }
    .edu-subtitle {
        font-size: 1rem;
        color: #7f8c8d;
    }
    .edu-date {
        float: right;
        font-weight: 600;
        color: #011f4b;
    }
    </style>

    <div class="edu-card">
        <div class="edu-title">🎓 Bachelor of Science: Honours <span class="edu-subtitle">(Astrophysics)</span> 
            <span class="edu-date">2017 - 2017</span>
        </div>
        <div class="edu-subtitle">University of the Free State</div>
        <ul>
            <li><b>Research Topics:</b> Optical, X-ray & Gamma-ray Photometry and Spectroscopy</li>
            <li><b>GPA:</b><strong style="color:#011f4b;">3.0/70.44%</strong></li>
            <li><b>Observations at the Boyden Observatory:</b> The Watcher and 1.5m Telescopes</li>
        </ul>
        <div><b><strong style="color:#FFA500;">Skills:</strong></b> Astrophysics, Research, Python & IRAF (Programmming Languages), Data Analysis</div>
    </div>
""", unsafe_allow_html=True)


# BSc
st.markdown("""
    <style>
    .edu-card {
        background-color: #f5f7fa;
        border-left: 6px solid #6497b1;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .edu-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #011f4b;
    }
    .edu-subtitle {
        font-size: 1rem;
        color: #7f8c8d;
    }
    .edu-date {
        float: right;
        font-weight: 600;
        color: #011f4b;
    }
    </style>

    <div class="edu-card">
        <div class="edu-title">🎓 Bachelor of Science <span class="edu-subtitle">(Astrophysics)</span> 
            <span class="edu-date">2014 - 2016</span>
        </div>
        <div class="edu-subtitle">University of the Free State</div>
        <ul>
            <li><b>University of the Free State:</b> 8 Graduate Attributes</li>
            <li><b>GPA:</b><strong style="color:#011f4b;">2.0/68.35%</strong></li>
        </ul>
        <div><b><strong style="color:#FFA500;">Skills:</strong></b> Physics, Astronomy, Calculus, Differential Equations, IRAF (Programming Language)</div>
    </div>
""", unsafe_allow_html=True)
