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
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    </style>
    <div class="center">
        <h1 style="color: dimgrey;">EDUCATION</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns([31, 20, 35, 15])
with c1:
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
            <h4 style="color: dimgrey;">Master of Science</h4>
        </div>
    """, unsafe_allow_html=True)
with c2:
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
with c3:
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
with c4:
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
            <h4 style="color: dimgrey;">2018 - 2024</h4>
        </div>
    """, unsafe_allow_html=True)

st.write('''
- ✔ :blue[Research Thesis Title]: _Probing the inner jet regions and emission mechanisms of the flat
spectrum radio quasar 3C 279 and PKS 1510-089 through temporal and spectral variability studies_.
- ✔ GPA/Mean: :blue[XX].
- ✔ Presented research in at least :blue[_four conferences_].
- ✔ Two :blue[_Proceedings of Sciences_] Published.

:orange[Skills]: Astrophysics, Research, Python & IRAF (Programmming Languages), Data Analysis, Oral & Written Communication
''')
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
