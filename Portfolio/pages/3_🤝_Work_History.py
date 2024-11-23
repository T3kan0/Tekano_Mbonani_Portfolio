#!/usr/bin/env python
# coding: utf-8
import pyreadr
import scipy.stats as stats
from scipy.stats import f_oneway
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import numpy as np
import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="Work",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
    )

# --- LOAD CSS, PDF & PROFIL PIC ---
with open('config.css') as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


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
        <h1 style="color: dimgrey;">Work History</h1>
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
            <h5 style="color: dimgrey;">Officer: Jnr Data Analyst</h5>
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
            <h5 style="color: dimgrey;">Centre for Teaching and Learning (CTL)</h5>
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
            <h5 style="color: dimgrey;">University of the Free State (UFS)</h5>
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
            <h5 style="color: dimgrey;">24/05/01 - Present</h5>
        </div>
    """, unsafe_allow_html=True)

st.write('''
- ✔ Leading a team of at least seven interns and research assistants in :blue[A_STEP] to ensure the building of effective survey forms, and that the tutorial data is collected, processed and stored in\
 the UFS database management systems in place.
- ✔ Developed :blue[5+ Web Applications] that automated and standardized data processes, thus boosted the productivity by several factors.
- ✔ Responsible for managing database management systems and tracking the :blue[data] collected weekly.
- ✔ Responsible for writing tutorial :blue[KPI] measuring reports, such as: _tutorial impact reports on student success, tutor costs, tutor training stats, student demographic_, etc.
- ✔ Built effective dashboards for the visualization of the data using tools such as :blue[_Microsoft Power BI & Excel_].
- ✔ Developed predictive data models on the tutorial attendance data making use of :blue[_Machine Learning & AI_] tools.
- ✔ :blue[Hypothesis Testing]: _Two Sample T-Test, ANOVA Test, Cohen's D, Post-Hoc Analysis, Linear Regression & Correlation Studies_.
- ✔ Research: Presented at the :blue[Siyaphumelela Conference (2024 June)] so far. Topic: :blue[_Evaluating the effectiveness and implementation of skills, principles and strategies in tutor training._

:orange[Skills]: MicroSoft Power BI & Excel, Python & R (programming languages), HTML, CSS, SPSS, NVIVO, Written & Oral Communication,  Automation
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
            <h5 style="color: dimgrey;">Assistant Officer: Data Analysis</h5>
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
            <h5 style="color: dimgrey;">Centre for Teaching and Learning (CTL)</h5>
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
            <h5 style="color: dimgrey;">University of the Free State (UFS)</h5>
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
            <h5 style="color: dimgrey;">24/01/01 - 24/04/31 </h5>
        </div>
    """, unsafe_allow_html=True)

st.write('''
- ✔ Part of a team with at least seven interns and research assistants in :blue[A_STEP] that built effective survey forms for the collection, processing and storage of the tutorial data in\
 the UFS database management systems.
- ✔ Developed :blue[MARS]: The Web Application that merges and processes large tutorial attendance register files collected on a weekly basis.
- ✔ Created trackers for the tutorial and financial data collected on a weekly and/or monthly basis on the UFS :blue[Bloemfontein, Qwa-qwa and South] campuses.
- ✔ Responsible for writing tutorial :blue[KPI] measuring reports, such as tutorial impact reports on student success, student demographics and more.

:orange[Skills]: Excel, Python & R (programming languages), SPSS, Data Analysis, Written Communication
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
            <h5 style="color: dimgrey;">Research Assistant: Data Analysis</h5>
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
            <h5 style="color: dimgrey;">Centre for Teaching and Learning (CTL)</h5>
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
            <h5 style="color: dimgrey;">University of the Free State (UFS)</h5>
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
            <h5 style="color: dimgrey;">22/09/01 - 23/12/31 </h5>
        </div>
    """, unsafe_allow_html=True)
st.write('''
- ✔ Part of a team of at least seven interns and other research assistants in :blue[A_STEP] that built effective survey forms for the collection of the tutorial data.
- ✔ Merged and processed large tutorial attendance register files that were collected on a weekly basis, and stored the files in the UFS :blue[database management systems].
- ✔ Reported weekly :blue[statistics] behind the tutorial data to Teaching and Learning Coordinators (TLCs) on the UFS Bloemfontein & Qwa-qwa campuses.

:orange[Skills]: Excel, Python (programming language), Data Collection & Processing, Building Surveys, Written Communication
''')

st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

c13, c14, c15, c16 = st.columns([31, 20, 35, 15])
with c13:
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
            <h5 style="color: dimgrey;">Teaching Assistant: UFSS1504/22</h5>
        </div>
    """, unsafe_allow_html=True)

with c14:
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
            <h5 style="color: dimgrey;">Centre for Teaching and Learning (CTL)</h5>
        </div>
    """, unsafe_allow_html=True)
with c15:
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
            <h5 style="color: dimgrey;">University of the Free State (UFS)</h5>
        </div>
    """, unsafe_allow_html=True)
with c16:
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
            <h5 style="color: dimgrey;">21/07/01 - 22/08/31 </h5>
        </div>
    """, unsafe_allow_html=True)

st.write('''
- ✔ Tutored, instructed and facillitated tutorials in the first entry level modules :blue[UFSS1504] & :blue[UFSS1522].
- ✔ :blue[Peer mentor] to students enrolled in UFSS1504 & UFSS1522 modules.
- ✔ Graded asssessements with feedback to :blue[students].

:orange[Skills]: Tutoring, Assessment Grading, Oral & Written Communication, Peer Mentoring, Blackboard Collaborate (Online Tutoring)
''')

st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)


c17, c18, c19, c20 = st.columns([31, 20, 35, 15])

with c17:
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
            <h5 style="color: dimgrey;">Research Assistant: Physics</h5>
        </div>
    """, unsafe_allow_html=True)

with c18:
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
            <h5 style="color: dimgrey;">The Department of Physics/Fisika (DoP)</h5>
        </div>
    """, unsafe_allow_html=True)
with c19:
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
            <h5 style="color: dimgrey;">University of the Free State (UFS)</h5>
        </div>
    """, unsafe_allow_html=True)
with c20:
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
            <h5 style="color: dimgrey;">18/01/01 - 21/06/31 </h5>
        </div>
    """, unsafe_allow_html=True)

st.write('''
- ✔ Conducted :blue[research] in Astrophysics topics that included multi-wavelength studies of :blue[Active Galactic Nucleus (AGNs)].
- ✔ Collected observational and archival data using telescopes at the :blue[Boyden observatory (Optical)] & :blue[_FERMI_ - Large Area Telescope (Gamma-ray)].
- ✔ Developed :blue[data analysis] pipelines.

:orange[Skills]: Research (astrophysics), Data Analysis, Python & IRAF (programming languages), Problem Solving, Critical Thinking
''')
st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

c21, c22, c23, c24 = st.columns([31, 20, 35, 15])
with c21:
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
            <h5 style="color: dimgrey;">Presenter & Narrator</h5>
        </div>
    """, unsafe_allow_html=True)

with c22:
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
            <h5 style="color: dimgrey;">The Navil Hill Planetarium</h5>
        </div>
    """, unsafe_allow_html=True)
with c23:
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
            <h5 style="color: dimgrey;">University of the Free State (UFS)</h5>
        </div>
    """, unsafe_allow_html=True)
with c24:
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
            <h5 style="color: dimgrey;">17/01/01 - 21/10/31</h5>
        </div>
    """, unsafe_allow_html=True)

st.write('''
- ✔ Compiling and presenting educational and intriguing programs or shows based on :blue[space science] & :blue[astronomy] topics to the general public.
- ✔ Presented shows in :blue[Sotho] & :blue[English].
- ✔ Operated the complex :blue[planterium] equipment.

:orange[Skills]: Oral Communication, Astronomy, Computer Literacy, Story Telling
''')

st.markdown("""
    <hr style="border: 2px solid dimgrey;">
""", unsafe_allow_html=True)

