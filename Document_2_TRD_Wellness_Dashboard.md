# Technical Requirements Document (TRD)
### Personal Wellness Dashboard (Single-User Analytics) — Project 2
**Artifact ID:** DOC-02 | **Version:** 1.0 (College Submission Ready) | **Academic Session:** 2026–2027

---

### Project & Student Identification Block
| Field | Value | Field | Value |
| :--- | :--- | :--- | :--- |
| **Project Name** | Single-User Personal Wellness Dashboard | **Document ID** | DOC-02 |
| **Student Name** | `[Student Name]` | **Roll Number / Student ID** | `[Roll Number / Student ID]` |
| **College / University** | `[College / University Name]` | **Department** | `[Department of Computer Science / Data Science]` |
| **Faculty Guide / Mentor**| `[Faculty Guide / Mentor Name]` | **Submission Date** | `[Submission Date]` |
| **Project Status** | Approved for Review | **Review Level** | Undergraduate Capstone / Project 2 |

---

> ⚠️ **ACADEMIC & NON-MEDICAL DISCLAIMER:**  
> This project is developed solely for undergraduate data analytics and software engineering academic evaluation. It is **NOT** a medical device, clinical diagnostic tool, or medical treatment system. All baseline demonstration records are **synthetic**.

---

## 1. System Architecture & High-Level Design

The Personal Wellness Dashboard is built using a clean, 4-tier modular architecture designed for local execution.

```
┌────────────────────────────────────────────────────────┐
│             LAYER 4: AI COLLABORATION LAYER             │
│   Google Gemini (Prompt Design, Code Co-pilot, Docs)    │
└───────────────────────────┬────────────────────────────┘
                            │ (Offline Design Phase)
┌───────────────────────────▼────────────────────────────┐
│          LAYER 3: PRESENTATION & VISUALIZATION         │
│   • Jupyter Notebook (Static Matplotlib / Seaborn)     │
│   • Streamlit Web UI (Interactive Plotly Visuals)      │
└───────────────────────────▲────────────────────────────┘
                            │ (Cleaned DataFrames & Metrics)
┌───────────────────────────┴────────────────────────────┐
│        LAYER 2: PROCESSING & ANALYTICS ENGINE          │
│   • Pandas (Vectorized Time-Series, 7-Day Moving Avg)  │
│   • NumPy (Mathematical Formulations & Pearson r)      │
│   • Data Quality Rules Engine (DQR-01 to DQR-09)       │
└───────────────────────────▲────────────────────────────┘
                            │ (Raw Ingestion)
┌───────────────────────────┴────────────────────────────┐
│             LAYER 1: DATA PERSISTENCE LAYER            │
│   • sample_wellness_data.csv (60 Synthetic Days)       │
│   • Document_7_Dataset_and_Data_Dictionary.xlsx        │
│   • Consented Personal Logs (User Replaced)            │
└────────────────────────────────────────────────────────┘
```

## 2. Technology Stack & Technical Rationale

| Technology | Version | System Role | Selection Rationale |
| :--- | :--- | :--- | :--- |
| **Python** | 3.10 - 3.14 | Core Language | Dominant language for data science; vast ecosystem; rapid prototyping. |
| **Jupyter Notebook** | 7.0+ | Interactive Environment | Enables narrative-driven analysis combining code, mathematical formulas, and charts. |
| **Pandas** | 2.0+ | Data Manipulation | Vectorized DataFrame operations optimized for rolling time-series calculations. |
| **NumPy** | 1.24+ | Numerical Mathematics | High-speed array operations, clipping, and statistical derivations. |
| **Matplotlib / Seaborn** | 3.8+ / 0.13+ | Static Visualization | Produces publication-grade, deterministic figures for academic evaluation. |
| **Plotly** | 5.18+ | Interactive Charts | Rich HTML5 interactive tooltips, panning, and zoom features in Streamlit. |
| **Streamlit** | 1.30+ | Local Web UI | Converts analytical scripts into interactive web dashboards in pure Python. |
| **openpyxl / python-docx**| 3.1+ / 1.1+ | Dossier Automation | Enables automated generation of multi-sheet Excel workbooks and Word dossiers. |

## 3. Data Schema & Dataset Assumptions

Three distinct data categories are recognized within this system:
1. **Synthetic Sample Dataset:** 60 daily records (August 1 to September 29, 2026) generated using Gaussian distributions to simulate realistic human behavioral variance for persona 'Alex'.
2. **User-Supplied Consented Data:** Real personal records collected via spreadsheet to replace demonstration records.
3. **Proposed Sensor Feeds (Heart Rate / Biometrics):** Wearable sensor feeds classified as future extensions; excluded from baseline demo.

### 3.1 Data Schema Table
* `date` (string/date): YYYY-MM-DD, Primary Key, Range: 2026-01-01 to 2026-12-31.
* `sleep_hours` (float): nocturnal sleep duration, 3.0 to 14.0 hours.
* `steps` (integer): daily ambulatory step count, 0 to 35,000 steps.
* `water_glasses` (integer): glasses consumed (250ml each), 0 to 25 glasses.
* `activity_minutes` (integer): workout minutes, 0 to 240 minutes.
* `mood_score` (integer): self-reported mood, discrete set {1, 2, 3, 4, 5}.
* `heart_rate_bpm` (integer, optional): resting heart rate (proposed future feed).

## 4. Mathematical Formulations & Metric Derivations

### 4.1 7-Day Rolling Moving Average (SMA)
$$	ext{SMA}_7(t) = rac{1}{7} \sum_{i=0}^{6} 	ext{Metric}(t-i)$$
Smoothes day-to-day volatility to highlight medium-term habit trends.

### 4.2 Habit Goal Compliance Rate (%)
$$	ext{Compliance Rate} = \left( rac{\sum_{t=1}^{N} \mathbb{I}(	ext{Metric}_t \ge 	ext{Target})}{N} ight) 	imes 100$$
Where $\mathbb{I}$ is the indicator function returning 1 if true, 0 otherwise.

### 4.3 Social Jetlag (Circadian Schedule Shift)
$$\Delta_{	ext{Sleep}} = \overline{	ext{Sleep}}_{	ext{Weekend}} - \overline{	ext{Sleep}}_{	ext{Weekday}}$$
Measures sleep debt accumulation and weekend recovery patterns.

### 4.4 Pearson Correlation Coefficient ($r$)
$$r_{XY} = rac{\sum (X_i - ar{X})(Y_i - ar{Y})}{\sqrt{\sum (X_i - ar{X})^2 \sum (Y_i - ar{Y})^2}}$$
Measures linear association between wellness dimensions (e.g., Sleep vs Mood).

### 4.5 Composite Daily Wellness Score (0 to 100 Index)
$$	ext{Wellness Score} = 25 	imes \left( rac{\min(	ext{Sleep}, 8)}{8} ight) + 25 	imes \left( rac{\min(	ext{Steps}, 10000)}{10000} ight) + 25 	imes \left( rac{\min(	ext{Water}, 8)}{8} ight) + 25 	imes \left( rac{	ext{Mood}}{5} ight)$$

## 5. Data Quality Rules (DQR Engine)
* **DQR-01 (Format & Uniqueness):** Enforces ISO-8601 YYYY-MM-DD date format and uniqueness.
* **DQR-02 (Temporal Boundary):** Rejects future-dated records.
* **DQR-03 (Sleep Range):** Clamps sleep hours within [3.0, 14.0].
* **DQR-04 (Step Range):** Enforces 0 <= steps <= 35,000.
* **DQR-05 (Hydration Range):** Warns if water < 3 or > 20 glasses.
* **DQR-06 (Activity Range):** Enforces 0 <= activity <= 240 mins.
* **DQR-07 (Mood Range):** Enforces discrete integer set {1, 2, 3, 4, 5}.
* **DQR-08 (Missing Data):** Forward-fills single missing days; median-imputes multi-day gaps.

## 6. Security, Privacy & Constraints
* **100% Local Execution:** Operates entirely offline with zero outbound network calls.
* **Zero Personally Identifiable Information (PII):** Schema excludes names, emails, IPs, or location data.
* **Deterministic Reproducibility:** Random seeds are fixed (`seed=42`) for demonstration consistency.
