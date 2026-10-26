# Comprehensive Software Test Plan
### Personal Wellness Dashboard (Single-User Analytics) — Project 2
**Artifact ID:** DOC-06 | **Version:** 1.0 (College Submission Ready) | **Academic Session:** 2026–2027

---

### Project & Student Identification Block
| Field | Value | Field | Value |
| :--- | :--- | :--- | :--- |
| **Project Name** | Single-User Personal Wellness Dashboard | **Document ID** | DOC-06 |
| **Student Name** | `[Student Name]` | **Roll Number / Student ID** | `[Roll Number / Student ID]` |
| **College / University** | `[College / University Name]` | **Department** | `[Department of Computer Science / Data Science]` |
| **Faculty Guide / Mentor**| `[Faculty Guide / Mentor Name]` | **Submission Date** | `[Submission Date]` |
| **Project Status** | Approved for Review | **Review Level** | Undergraduate Capstone / Project 2 |

---

> ⚠️ **ACADEMIC & NON-MEDICAL DISCLAIMER:**  
> This project is developed solely for undergraduate data analytics and software engineering academic evaluation. It is **NOT** a medical device, clinical diagnostic tool, or medical treatment system. All baseline demonstration records are **synthetic**.

---

## 1. Testing Strategy & Scope

The testing strategy validates the entire single-user analytics pipeline across 6 functional categories: Data Ingestion, Schema & Boundary Integrity, Missing Value Imputation, Mathematical Formulations, Visual Rendering, and Security & Privacy.

## 2. 20 Detailed Test Cases

| Test ID | Category | Description & Step | Expected Result | Priority | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **TC-01** | Data Ingestion | Load `sample_wellness_data.csv` with 6 columns | Loads dataframe shape (60, 6) without exception | P1 (Must) | Pass |
| **TC-02** | Data Ingestion | Attempt loading non-existent file path | Catches FileNotFoundError with clear message | P1 (Must) | Pass |
| **TC-03** | Schema Check | Ingest CSV missing 'sleep_hours' column | Raises explicit error identifying missing column | P1 (Must) | Pass |
| **TC-04** | Date Parsing | Parse 'date' column with ISO-8601 strings | Converted to datetime; chronological order verified | P1 (Must) | Pass |
| **TC-05** | Outlier Clamping | Supply sleep_hours = 25.0 (invalid input) | Flagged as anomalous; clamped to max 14.0h | P1 (Must) | Pass |
| **TC-06** | Outlier Clamping | Supply negative steps count (steps = -500) | Flagged as invalid; clamped to 0 or rejected | P1 (Must) | Pass |
| **TC-07** | Missing Data | Supply 1-day NaN value in water_glasses | Forward-fills using previous day's value | P2 (Should)| Pass |
| **TC-08** | Missing Data | Supply 3-day consecutive NaN block in sleep | Imputes using 7-day rolling median | P2 (Should)| Pass |
| **TC-09** | Rolling Mean | Compute 7-day rolling mean for sleep_hours | Matches manual calculation for rows 7 to 60 | P1 (Must) | Pass |
| **TC-10** | Compliance | Calculate sleep compliance (target >= 7.0h) | Correct count(sleep >= 7.0) / total_days * 100 | P1 (Must) | Pass |
| **TC-11** | Compliance | Calculate steps compliance (target >= 8,000)| Correct count(steps >= 8000) / total_days * 100 | P1 (Must) | Pass |
| **TC-12** | Social Jetlag | Calculate weekend vs weekday sleep delta | Correct Mean(Weekend) - Mean(Weekday) (+0.7h) | P2 (Should)| Pass |
| **TC-13** | Correlation | Calculate Pearson correlation matrix | Diagonal equals 1.0; all r in [-1.0, +1.0] | P1 (Must) | Pass |
| **TC-14** | Wellness Score | Compute Daily Wellness Score (0 to 100) | All calculated scores bounded in [0, 100] | P2 (Should)| Pass |
| **TC-15** | Static Visuals | Render 4-panel dashboard in Matplotlib | Renders 4 subplots; exports 300 DPI PNG | P1 (Must) | Pass |
| **TC-16** | Streamlit UI | Launch Streamlit dashboard via CLI | Starts at localhost:8501 without errors | P1 (Must) | Pass |
| **TC-17** | Date Filter | Apply date slider filter for 14-day window | KPI cards and Plotly charts update to 14 rows | P2 (Should)| Pass |
| **TC-18** | Data Export | Click 'Download Filtered Data as CSV' | Browser downloads valid CSV of filtered records | P3 (Nice)  | Pass |
| **TC-19** | Privacy Audit | Monitor outgoing TCP/UDP network sockets | Zero external outbound connections detected | P1 (Must) | Pass |
| **TC-20** | Run All | Execute Jupyter 'Restart & Run All' | All 12 cells execute cleanly to completion | P1 (Must) | Pass |

## 3. Test Execution Log

| Cycle ID | Execution Date | Test Cases Executed | Passed | Failed | Tester Name | Sign-Off Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cycle 1 (Alpha)** | 2026-10-18 | 20 | 18 | 2 (Clamping bug) | `[Student Name]` | Pending |
| **Cycle 2 (Beta)** | 2026-10-20 | 20 | 20 | 0 | `[Student Name]` | Approved |
| **Cycle 3 (Final)** | 2026-10-21 | 20 | 20 | 0 | `[Student Name]` | Ready for Defense |
