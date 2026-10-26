# Project Verification Checklist
### Personal Wellness Dashboard (Single-User Analytics) — Project 2
**Artifact ID:** DOC-04 | **Version:** 1.0 (College Submission Ready) | **Academic Session:** 2026–2027

---

### Project & Student Identification Block
| Field | Value | Field | Value |
| :--- | :--- | :--- | :--- |
| **Project Name** | Single-User Personal Wellness Dashboard | **Document ID** | DOC-04 |
| **Student Name** | `[Student Name]` | **Roll Number / Student ID** | `[Roll Number / Student ID]` |
| **College / University** | `[College / University Name]` | **Department** | `[Department of Computer Science / Data Science]` |
| **Faculty Guide / Mentor**| `[Faculty Guide / Mentor Name]` | **Submission Date** | `[Submission Date]` |
| **Project Status** | Approved for Review | **Review Level** | Undergraduate Capstone / Project 2 |

---

> ⚠️ **ACADEMIC & NON-MEDICAL DISCLAIMER:**  
> This project is developed solely for undergraduate data analytics and software engineering academic evaluation. It is **NOT** a medical device, clinical diagnostic tool, or medical treatment system. All baseline demonstration records are **synthetic**.

---

## Quality Assurance & Evaluation Verification Checklist

| Phase / Item ID | Checklist Item Description | Verification Criteria | Status | Sign-Off Date |
| :--- | :--- | :--- | :---: | :---: |
| **PH1-01** | Scope Boundary Definition | Single-user model strictly confirmed; no multi-tenant complexity. | [x] Completed | 2026-10-21 |
| **PH1-02** | Non-Medical Disclaimer | Prominently embedded across all docs, notebooks, and web app headers. | [x] Completed | 2026-10-21 |
| **PH1-03** | AI Role Clarification | Gemini explicitly documented as offline developer co-pilot, not live API. | [x] Completed | 2026-10-21 |
| **PH2-01** | Python Environment Setup | Tested under Python 3.10+; virtualenv requirements documented. | [x] Completed | 2026-10-21 |
| **PH2-02** | Dependency Verification | Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit install cleanly. | [x] Completed | 2026-10-21 |
| **PH3-01** | Synthetic Dataset Labeling | Explicitly labeled synthetic; no clinical patient data fabricated. | [x] Completed | 2026-10-21 |
| **PH3-02** | Data Dictionary Completeness | 4-sheet Excel workbook generated covering schema, sample, rules, metrics. | [x] Completed | 2026-10-21 |
| **PH3-03** | Data Quality Rules (DQR) | 9 integrity checks defined (bounds, uniqueness, missing value handling). | [x] Completed | 2026-10-21 |
| **PH3-04** | Personal Data Replacement | Step-by-step guide provided to replace sample CSV with personal data. | [x] Completed | 2026-10-21 |
| **PH4-01** | 7-Day Moving Averages | Rolling means computed for sleep, steps, and water without lookahead bias. | [x] Completed | 2026-10-21 |
| **PH4-02** | Goal Compliance Calculation | Adherence percentage calculated against 8,000 steps, 7.5h sleep, 8 glasses. | [x] Completed | 2026-10-21 |
| **PH4-03** | Social Jetlag Calculation | Weekend sleep shift computed and interpreted accurately (+0.7 hrs). | [x] Completed | 2026-10-21 |
| **PH4-04** | Correlation Heatmap | Pearson r matrix computed across all continuous variables. | [x] Completed | 2026-10-21 |
| **PH5-01** | Jupyter Notebook Execution | Executes from top to bottom ('Restart & Run All') without error. | [x] Completed | 2026-10-21 |
| **PH5-02** | Streamlit Web Application | Launches via 'streamlit run dashboard_app.py' with responsive layout. | [x] Completed | 2026-10-21 |
| **PH5-03** | Interactive Filtering | Date range selectors and habit target sliders update charts dynamically. | [x] Completed | 2026-10-21 |
| **PH6-01** | Zero Telemetry Audit | Code verified to execute 100% offline with zero outbound HTTP requests. | [x] Completed | 2026-10-21 |
| **PH6-02** | PII Sanitization | No personal names, GPS, or contact records stored in sample data. | [x] Completed | 2026-10-21 |
| **PH7-01** | 7 Required Deliverables | PRD, TRD, Guide, Checklist, Demo, Test Plan, Excel all present. | [x] Completed | 2026-10-21 |
| **PH7-02** | PowerPoint Presentation | 9-slide widescreen PPTX deck with speaker notes generated. | [x] Completed | 2026-10-21 |
| **PH7-03** | Unified ZIP Archive | All project assets packaged into a clean, single downloadable ZIP archive. | [x] Completed | 2026-10-21 |
