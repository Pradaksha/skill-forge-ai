# Skill Forge – AI Skill Gap Analyzer

## Overview

Skill Forge is an AI-powered system that analyzes job descriptions and resumes to identify skill gaps and generate personalized learning plans.

It helps job seekers understand what skills they need to improve for specific roles.

---

## Features

* Resume input (Paste / Upload)
* Upload support (TXT, DOCX)
* Smart skill extraction
* Skill matching and scoring
* Personalized learning roadmap
* Clean and interactive UI (Streamlit)

---

## Tech Stack

* Python
* Streamlit
* python-docx

---

## Supported File Types

* TXT
* DOCX

---

## Note

PDF and image support are limited in cloud deployment to ensure stability.

---

## Architecture

User Input → Skill Extraction → Skill Matching → Gap Analysis → Learning Plan → UI Output

---

## Scoring Logic

Match Score = (Matched Skills / Required Skills) × 100

---

## Sample Input

Job Description:
Data Analyst with Python, SQL, Excel

Resume:
Worked on Excel dashboards

---

## Sample Output

Required Skills:

* Python
* SQL
* Excel

Candidate Skills:

* Excel

Skill Gaps:

* Python
* SQL

Match Score:
33%

---

## Live Application

https://skill-forge-ai-mk8pj7a5hjzazfbyx27hp3.streamlit.app/

---

## Demo Video

https://drive.google.com/file/d/1rou6548kYvHMPJUbG8g2EUyONX4KfFVo/view?usp=sharing

---

## How to Run Locally

pip install -r requirements.txt
streamlit run app.py

---

## Use Case

This system helps students and job seekers identify missing skills and build a structured learning path to achieve their career goals.
