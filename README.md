# Personal Wellness Dashboard: Single-User Analytics
## Project 2 — College Project Submission Dossier
**Academic Session:** 2026–2027 | **Status:** College-Submission-Ready (Final Release v1.0)

---

### Candidate & Project Metadata Block
* **Project Title:** Personal Wellness Dashboard (Single-User Analytics)
* **Student Name:** `[Student Name]`
* **Roll Number / Student ID:** `[Roll Number / Student ID]`
* **Department:** `[Department of Computer Science / Data Science]`
* **College / University:** `[College / University Name]`
* **Faculty Project Guide / Mentor:** `[Faculty Guide / Mentor Name]`
* **Submission Date:** `[Submission Date]`

---

> ⚠️ **ACADEMIC & NON-MEDICAL DISCLAIMER:**  
> This project is developed strictly for educational analytics evaluation (Project 2: Wellness Dashboard). It is **NOT** a medical diagnostic tool or healthcare monitoring system. All baseline demonstration records are **synthetic**.

---

## 1. Project Overview & Deliverables Catalog

This repository and dossier package contains the complete, professional deliverables for **Project 2: Wellness Dashboard**:

| File Name | Deliverable Format | Description |
| :--- | :--- | :--- |
| **`Document_1_PRD_Wellness_Dashboard.docx`** / `.md` | PRD (Word / Markdown) | Product Requirements Document: problem statement, persona "Alex", user stories, functional & non-functional requirements, scope boundaries. |
| **`Document_2_TRD_Wellness_Dashboard.docx`** / `.md` | TRD (Word / Markdown) | Technical Requirements Document: 4-tier architecture, tech stack rationale, mathematical formulas, DQR rules engine, security. |
| **`Document_3_Implementation_Guide_Wellness_Dashboard.docx`** / `.md` | Guide (Word / Markdown) | Implementation Guide: environment setup, folder layout, milestone instructions, real personal data replacement guide, troubleshooting. |
| **`Document_4_Project_Checklist_Wellness_Dashboard.docx`** / `.md` | Checklist (Word / Markdown) | Quality Assurance Checklist: 9-phase tick-box table covering requirements, testing, privacy, and college defense readiness. |
| **`Document_5_Presentation_and_Demo_Guide_Wellness_Dashboard.docx`** / `.md` | Guide (Word / Markdown) | Presentation & Demo Guide: 9-slide presentation guide, 5-minute live demo script, 12 viva voce Q&As with model student answers. |
| **`Document_6_Test_Plan_Wellness_Dashboard.docx`** / `.md` | Test Plan (Word / Markdown)| Software Test Plan: 20 verified test cases (TC-01 to TC-20), test execution log template, release acceptance sign-off criteria. |
| **`Document_7_Dataset_and_Data_Dictionary.xlsx`** | Excel Workbook (.xlsx) | 4-Tab Excel Workbook: (1) Data Dictionary, (2) 60-Day Synthetic Dataset, (3) Data Quality Rules, (4) Metric Definitions. |
| **`Presentation_Wellness_Dashboard.pptx`** | PowerPoint Deck (.pptx) | Polished 9-slide widescreen (16:9) presentation deck with card layout, visual hierarchy, and complete speaker notes on every slide. |
| **`wellness_dashboard_notebook.ipynb`** | Jupyter Notebook (.ipynb) | Fully documented academic Jupyter Notebook with narrative markdown, data cleaning, KPIs, 4-panel figures, and correlation heatmaps. |
| **`dashboard_app.py`** | Streamlit Web App (.py) | Interactive web dashboard featuring Plotly graphs, reactive date filters, habit goal sliders, and CSV download capabilities. |
| **`sample_wellness_data.csv`** | CSV Data File (.csv) | Standalone 60-day baseline demonstration dataset for direct consumption. |
| **`Wellness_Dashboard_College_Project_Dossier.zip`** | ZIP Archive (.zip) | Unified master package containing all project deliverables. |

---

## 2. Quickstart Execution Guide

### Step 1: Environment Setup
```powershell
# Navigate to the project directory
cd "C:\Users\DIKSHA SHUKLA\.gemini\antigravity\scratch\wellness_project_submission"

# Install dependencies
pip install pandas numpy matplotlib seaborn plotly streamlit openpyxl python-docx python-pptx
```

### Step 2: Running the Jupyter Notebook
```bash
jupyter notebook wellness_dashboard_notebook.ipynb
```
Select **Kernel** -> **Restart & Run All** to generate all calculations and static charts.

### Step 3: Launching the Interactive Streamlit Web App
```bash
streamlit run dashboard_app.py
```
The dashboard will open automatically in your default browser at `http://localhost:8501`.

---

## 3. How to Replace Synthetic Data with Real Data
1. Open `sample_wellness_data.csv` in Excel or VS Code.
2. Clear rows 2 through 61, keeping row 1 headers intact (`date,sleep_hours,steps,water_glasses,activity_minutes,mood_score`).
3. Enter your own daily records in ISO format (`YYYY-MM-DD`).
4. Save the file and reload the Jupyter Notebook or Streamlit application.
