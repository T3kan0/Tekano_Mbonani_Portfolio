#!/usr/bin/env python
# coding: utf-8
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
        <div class="header-title">💼 Work History</div>
    </div>
""", unsafe_allow_html=True)

#### Header
def display_work_card(title, organization, date_range, details_markdown, skills_markdown):
    with st.container():
        # Job header styled like a card
        st.markdown(
            f"""
            <div style="border-left: 6px solid #004080; background-color: #f9f9f9;
                        padding: 16px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.05);
                        margin-bottom: 8px;">
                <h4 style="margin: 0; color: #004080;">{title}</h4>
                <div style="display: flex; justify-content: space-between; font-size: 14px; color: #555;">
                    <span><em>{organization}</em></span>
                    <span>{date_range}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("See job details"):
            st.write(details_markdown)
            st.markdown(skills_markdown)

# Job details and skills
data_analyst = '''
-  Supervises a team of seven interns and research assistants, ensuring the effective design of survey instruments and the systematic collection, processing, and secure storage of tutorial data within UFS database systems.  
-  Engineered :blue[+5 web-based applications] to automate and standardize data workflows, significantly increasing operational efficiency.  
-  Oversaw database management systems and maintained weekly tracking of critical tutorial program data.  
-  Authored tutorial :blue[KPI] reports, including: _impact analyses on student performance, tutor cost assessments, training participation metrics, and demographic breakdowns_.  
-  Designed dynamic dashboards for data visualization using :blue[_Microsoft Power BI_], :blue[_Excel_], and related tools to support strategic decision-making.  
-  Built predictive models using :blue[_Machine Learning and AI_] techniques to analyze tutorial attendance patterns and forecast student engagement.  
-  Applied rigorous :blue[statistical testing] methods, including: _Two-Sample T-Test, ANOVA, Cohen’s D, Post-Hoc Analysis, Linear Regression, and Correlation Studies_.  
-  Presented research findings at the :blue[Siyaphumelela Conference (June 2024, July 2025)], focusing on: :blue[_Evaluating the implementation and effectiveness of skills, principles, and strategies in tutor training._]
'''

skills_1 = ":orange[Skills]: Microsoft Power BI, Excel, Python, R, HTML, CSS, SPSS, NVivo, Data Automation, Technical Writing, and Oral Communication"

# Display the card
display_work_card(
    title="Officer: Jnr Data Analyst",
    organization="Centre for Teaching and Learning (CTL), University of the Free State (UFS)",
    date_range="May 2024 – Present",
    details_markdown=data_analyst,
    skills_markdown=skills_1
)


# Job details and skills
a_officer = '''
- Collaborated with a team of seven interns and research assistants to design effective survey instruments and ensure the accurate collection, processing, and storage of tutorial data within UFS database systems.  
- Developed :blue[MARS], a web-based application for merging and processing large-scale tutorial attendance registers collected weekly.  
- Built data trackers to monitor tutorial and financial metrics across UFS _Bloemfontein_, _QwaQwa_, and _South_ campuses on a weekly and monthly basis.  
- Authored tutorial :blue[KPI] reports, including analyses of student success, demographic distributions, and program performance indicators.  
'''


skills_2 = ":orange[Skills]: Excel, Python, R, SPSS, Data Analysis, Technical Writing"

# Display the card
display_work_card(
    title="Assistant Officer: Data Analysis",
    organization="Centre for Teaching and Learning (CTL), University of the Free State (UFS)",
    date_range="24/01/01 - 24/04/31",
    details_markdown=a_officer,
    skills_markdown=skills_2
)


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

