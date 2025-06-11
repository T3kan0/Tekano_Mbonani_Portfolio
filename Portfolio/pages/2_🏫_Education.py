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

st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

# ADD this instead
st.markdown("""
    <style>
    .edu-card {
        background-color: #f5f7fa;
        border-left: 6px solid #a4c330;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .edu-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
    }
    .edu-subtitle {
        font-size: 1rem;
        color: #7f8c8d;
    }
    .edu-date {
        float: right;
        font-weight: 600;
        color: #a4c330;
    }
    </style>

    <div class="edu-card">
        <div class="edu-title">🎓 Master of Science <span class="edu-subtitle">(Astrophysics)</span> 
            <span class="edu-date">2018 – 2024</span>
        </div>
        <div class="edu-subtitle">University of the Free State</div>
        <ul>
            <li><b>Thesis:</b> Probing the inner jet regions and emission mechanisms of the flat spectrum radio quasars 3C 279 and PKS 1510-089 through temporal and spectral variability studies</li>
            <li><b>GPA:</b> 3.5 / 82.00%</li>
            <li><b>Conferences:</b> 4 presented</li>
            <li><b>Publications:</b> 2 in Proceedings of Sciences</li>
        </ul>
        <div><b>Skills:</b> Astrophysics, Python, IRAF, Data Analysis, Communication</div>
    </div>
""", unsafe_allow_html=True)


#st.write('''
#- ✔ :blue[Research Thesis Title]: _Probing the inner jet regions and emission mechanisms of the flat
#spectrum radio quasar 3C 279 and PKS 1510-089 through temporal and spectral variability studies_.
#- ✔ GPA/Mean: :blue[3.5/82.00%].
#- ✔ Presented research in at least :blue[_four conferences_].
#- ✔ Two :blue[_Proceedings of Sciences_] Published.

#:orange[Skills]: Astrophysics, Research, Python & IRAF (Programmming Languages), Data Analysis, Oral & Written Communication
#''')
st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

c5, c6, c7, c8 = st.columns([31, 20, 35, 15])

with c5:
    st.markdown("""
        <style>
        .left {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100px;
        }
        </style>
        <div class="left">
            <h4 style="color: dimgrey;">Bachelor of Science: Honours</h4>
        </div>
    """, unsafe_allow_html=True)    

with c6:
    st.markdown("""
        <style>
        .left {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100px;
        }
        </style>
        <div class="left">
            <h4 style="color: dimgrey;">(Astrophysics)</h4>
        </div>
    """, unsafe_allow_html=True)
with c7:
    st.markdown("""
        <style>
        .left {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100px;
        }
        </style>
        <div class="left">
            <h4 style="color: dimgrey;">University of the Free State</h4>
        </div>
    """, unsafe_allow_html=True)

with c8:
    st.markdown("""
        <style>
        .left {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100px;
        }
        </style>
        <div class="left">
            <h4 style="color: dimgrey;">2017 - 2017</h4>
        </div>
    """, unsafe_allow_html=True)


st.write('''
- ✔ :blue[Research Topics]: _Optical, X-ray & Gamma-ray Photometry and Spectroscopy_.
- ✔ GPA/Mean: :blue[3.0/70.44%].
- ✔ Observations at the Boyden Observatory: :blue[_The Watcher and 1.5m Telescopes_].

:orange[Skills]: Astrophysics, Research, Python & IRAF (Programmming Languages), Data Analysis
''')

st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

c9, c10, c11, c12 = st.columns([31, 20, 35, 15])

with c9:
    st.markdown("""
        <style>
        .left {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100px;
        }
        </style>
        <div class="left">
            <h4 style="color: dimgrey;">Bachelor of Science</h4>
        </div>
    """, unsafe_allow_html=True)

with c10:
    st.markdown("""
        <style>
        .left {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100px;
        }
        </style>
        <div class="left">
            <h4 style="color: dimgrey;">(Physics)</h4>
        </div>
    """, unsafe_allow_html=True)
with c11:
    st.markdown("""
        <style>
        .left {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100px;
        }
        </style>
        <div class="left">
            <h4 style="color: dimgrey;">University of the Free State</h4>
        </div>
    """, unsafe_allow_html=True)

with c12:
    st.markdown("""
        <style>
        .left {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100px;
        }
        </style>
        <div class="left">
            <h4 style="color: dimgrey;">2014 - 2016</h4>
        </div>
    """, unsafe_allow_html=True)


st.write('''
- ✔ University of the Free State: :blue[_8 Graduate Attributes_].
- ✔ GPA/Mean: :blue[2.0/68.35%].

:orange[Skills]: Physics, Astronomy, Calculus, Differential Equations, IRAF (Programming Language)
''')
st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)
