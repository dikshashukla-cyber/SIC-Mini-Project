# Implementation & Setup Guide
### Personal Wellness Dashboard (Single-User Analytics) — Project 2
**Artifact ID:** DOC-03 | **Version:** 1.0 (College Submission Ready) | **Academic Session:** 2026–2027

---

### Project & Student Identification Block
| Field | Value | Field | Value |
| :--- | :--- | :--- | :--- |
| **Project Name** | Single-User Personal Wellness Dashboard | **Document ID** | DOC-03 |
| **Student Name** | `[Student Name]` | **Roll Number / Student ID** | `[Roll Number / Student ID]` |
| **College / University** | `[College / University Name]` | **Department** | `[Department of Computer Science / Data Science]` |
| **Faculty Guide / Mentor**| `[Faculty Guide / Mentor Name]` | **Submission Date** | `[Submission Date]` |
| **Project Status** | Approved for Review | **Review Level** | Undergraduate Capstone / Project 2 |

---

> ⚠️ **ACADEMIC & NON-MEDICAL DISCLAIMER:**  
> This project is developed solely for undergraduate data analytics and software engineering academic evaluation. It is **NOT** a medical device, clinical diagnostic tool, or medical treatment system. All baseline demonstration records are **synthetic**.

---

## 1. Prerequisites & Environment Setup

### 1.1 Hardware & Software Requirements
* **Operating System:** Windows 10/11, macOS (Monterey+), or Linux (Ubuntu 20.04+).
* **Python Interpreter:** Python 3.9, 3.10, 3.11, 3.12, 3.13, or 3.14 installed.
* **Terminal / Shell:** PowerShell, Command Prompt, or bash/zsh.
* **Browser:** Chrome, Firefox, Edge, or Safari.

### 1.2 Step-by-Step Installation Commands

```powershell
# 1. Navigate to your project directory
cd "C:\Users\DIKSHA SHUKLA\.gemini\antigravity\scratch\wellness_project_submission"

# 2. (Optional but recommended) Create virtual environment
python -m venv venv

# Windows activate:
.\venv\Scripts\Activate.ps1
# macOS/Linux activate:
# source venv/bin/activate

# 3. Install required Python packages
pip install pandas numpy matplotlib seaborn plotly streamlit openpyxl python-docx python-pptx
```

## 2. Project Directory Layout

```
wellness_project_submission/
├── sample_wellness_data.csv                    <- 60-day baseline synthetic dataset
├── wellness_dashboard_notebook.ipynb           <- Core Jupyter Notebook dashboard
├── dashboard_app.py                            <- Interactive Streamlit web application
├── Document_1_PRD_Wellness_Dashboard.docx       <- Product Requirements Document
├── Document_2_TRD_Wellness_Dashboard.docx       <- Technical Requirements Document
├── Document_3_Implementation_Guide.docx        <- Setup & Run Guide
├── Document_4_Project_Checklist.docx           <- Evaluation Tick-Box Checklist
├── Document_5_Presentation_and_Demo_Guide.docx <- Viva Voce & Live Demo Script
├── Document_6_Test_Plan_Wellness_Dashboard.docx<- 20 Verified Test Cases & Log
├── Document_7_Dataset_and_Data_Dictionary.xlsx <- 4-Sheet Excel Workbook
├── Presentation_Wellness_Dashboard.pptx        <- 9-Slide Review Presentation Deck
└── README.md                                   <- Master Quickstart Guide
```

## 3. How to Run the Deliverables

### Option A: Running the Jupyter Notebook
1. In your terminal, run:
   ```bash
   jupyter notebook wellness_dashboard_notebook.ipynb
   ```
2. Once the notebook opens in your browser, click **Kernel** -> **Restart & Run All**.
3. Inspect data tables, statistical summaries, 4-panel time series plots, and correlation heatmaps.

### Option B: Running the Streamlit Web Application
1. In your terminal, run:
   ```bash
   streamlit run dashboard_app.py
   ```
2. The interactive dashboard will automatically open at `http://localhost:8501`.
3. Use the sidebar to filter date ranges and adjust habit target sliders.

## 4. Replacing Synthetic Data with Real Data

1. Open `sample_wellness_data.csv` in Excel or a text editor.
2. Delete rows 2 through 61, keeping the column headers intact:
   `date,sleep_hours,steps,water_glasses,activity_minutes,mood_score`
3. Enter your actual daily measurements:
   * `date`: YYYY-MM-DD
   * `sleep_hours`: e.g. 7.5
   * `steps`: e.g. 8420
   * `water_glasses`: e.g. 8
   * `activity_minutes`: e.g. 45
   * `mood_score`: 1 to 5
4. Save the file as `my_wellness_data.csv`.
5. Update `DATA_PATH = "my_wellness_data.csv"` in the notebook or app, and re-run!

## 5. Troubleshooting Guide

| Error | Cause | Remediation |
| :--- | :--- | :--- |
| `FileNotFoundError` | Terminal not in project folder | Run `cd` into the folder containing `sample_wellness_data.csv`. |
| `ModuleNotFoundError: streamlit` | Package missing in active venv | Run `pip install streamlit plotly pandas`. |
| `Port 8501 already in use` | Background instance running | Run `streamlit run dashboard_app.py --server.port 8502`. |
| `ValueError: date format` | Date strings not YYYY-MM-DD | Ensure date strings match ISO standard `YYYY-MM-DD`. |
