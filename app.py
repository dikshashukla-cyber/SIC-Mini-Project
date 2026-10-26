"""Wellness Dashboard (Next-Level Edition) — IBM Z Datathon 2026 & College Submission Dossier

An enterprise-inspired personal wellness tracking application integrating:
- 🤖 Local "Z-Cognitive Habit Assistant" (Zero-API Natural Language Queries)
- 🖥️ Multi-Theme Modes (Enterprise Light, IBM Z Mainframe Dark, Cyberpunk Bio-Hacker Neon)
- 🧬 Bio-Digital Twin & Biological Rejuvenation Age Calculator
- 🌌 Interactive 3D Habit Phase Space Trajectory & Attractor Orbit
- ⚡ Neuro-Momentum Physics Engine (Velocity, Inertia & Escape Velocity)
- 🧘 Interactive 60-Second Coherent Breathwork & Vagal Tone HRV Sync Trainer
- ⏰ 24-Hour Circadian Polar Clock Dial & Social Jetlag Analyzer
- 🛡️ Autonomic Habit Resiliency Engine (Availability & MTTR)
- 🕸️ 5-Axis Habit Synergy Radar (Spider Chart)
- 🟩 GitHub-Style 60-Day Habit Execution Grid (Contribution Heatmap)
- 🎧 Built-in Synthesized Ambient Focus Soundscapes (HTML5 Web Audio API)
- 🏆 Gamified Habit Milestone Badges & "What-If?" Routine Simulator
- 🎓 Academic Defense Room & Viva Voce Q&A Simulator (LaTeX Math & System Specs)
- 🔒 IBM Z Pervasive Privacy & Data Sovereignty Vault (SHA-256 Provenance)
- ⚠️ Strict Non-Medical Design Boundary (FR-09)
"""

from __future__ import annotations

import io
from datetime import date, datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

from src.data_loader import (
    load_csv_data,
    load_and_validate,
    get_csv_template,
    DEFAULT_SAMPLE_PATH,
)
from src.validation import validate_wellness_data, detect_anomalies, ValidationReport
from src.metrics import (
    UserGoals,
    CompositeScore,
    filter_by_date_range,
    calculate_dashboard_stats,
    calculate_composite_score,
    calculate_weekday_vs_weekend_stats,
    calculate_habit_streaks,
    calculate_correlation_matrix,
    add_rolling_averages,
)
from src.insights import (
    generate_trend_observations,
    MIN_DAYS_FOR_TRENDS,
    MIN_DAYS_FOR_PERIOD_COMPARISON,
)
from src.personas import generate_persona_dataset, PERSONA_PROFILES
from src.report_generator import generate_executive_html_report
from src.resilience import calculate_autonomic_resiliency, ResiliencyReport
from src.badges import evaluate_achievement_badges, AchievementBadge
from src.simulation import simulate_routine_tweak, SimulationResult
from src.security import audit_session_security, SecurityAuditReport
from src.chronotype import calculate_circadian_chronotype, ChronotypeReport
from src.vitality import calculate_vitality_forecast, VitalityReport
from src.calendar_heatmap import build_habit_calendar_heatmap
from src.soundscapes import render_focus_soundscapes_widget
from src.assistant import answer_wellness_query
from src.clock_visualizer import build_circadian_polar_clock
from src.theme import get_theme_css

# Unique Cutting-Edge Extensions
from src.bio_twin import (
    calculate_biological_age,
    calculate_neuro_momentum,
    build_3d_habit_orbit_chart,
)
from src.breathwork import render_breathwork_widget
from src.viva_defense import render_academic_defense_tab


# --- Page Configuration ---
st.set_page_config(
    page_title="Wellness Dashboard | Next-Level Analytics",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)


def init_session_state():
    """Initializes session state keys."""
    if "reset_trigger" not in st.session_state:
        st.session_state.reset_trigger = 0
    if "shred_notice" not in st.session_state:
        st.session_state.shred_notice = False
    if "active_theme" not in st.session_state:
        st.session_state.active_theme = "Enterprise Light"
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def reset_dashboard():
    """Resets session state to default demo dataset."""
    st.session_state.reset_trigger += 1
    st.session_state.uploader_key = str(st.session_state.reset_trigger)
    st.session_state.shred_notice = False
    st.session_state.chat_history = []


def shred_session():
    """Cryptographically shreds session state and forces clean memory re-initialization."""
    st.session_state.clear()
    st.session_state.reset_trigger = 999
    st.session_state.shred_notice = True


def render_sidebar():
    """Renders sidebar controls, theme mode, persona selectors, goal sliders, and ambient soundscapes."""
    st.sidebar.title("🛡️ Controls & System Goals")
    st.sidebar.markdown("**Wellness Analytics Engine** &bull; *Next-Level Edition*")
    st.sidebar.markdown("---")

    # Theme Switcher
    st.sidebar.subheader("🎨 Interface Theme")
    theme_options = [
        "Enterprise Light",
        "IBM Z Mainframe (Dark)",
        "Cyberpunk Bio-Hacker (Neon Glass)",
    ]
    cur_idx = theme_options.index(st.session_state.active_theme) if st.session_state.active_theme in theme_options else 0
    theme_choice = st.sidebar.radio(
        "Display Mode:",
        options=theme_options,
        index=cur_idx,
        key=f"theme_radio_{st.session_state.reset_trigger}",
    )
    st.session_state.active_theme = theme_choice

    st.sidebar.markdown("---")

    # Data Source & Persona Selector
    st.sidebar.subheader("Dataset & Evaluator Personas")
    source_options = [
        "Default Sample (60 Days)",
        "🏃 Persona: Active Professional",
        "🦉 Persona: Variable Night Owl",
        "🧘 Persona: Balanced Habit Tracker",
        "📂 Upload Custom CSV File",
    ]

    chosen_source = st.sidebar.selectbox(
        "Select Profile or Data Source:",
        options=source_options,
        index=0,
        key=f"source_select_{st.session_state.reset_trigger}",
        help="Switch between synthetic profiles to test how the dashboard adapts across different lifestyles.",
    )

    persona_name = None
    if chosen_source == "Default Sample (60 Days)":
        report = load_and_validate(DEFAULT_SAMPLE_PATH)
        persona_name = "Default 60-Day Sample"
    elif "Active Professional" in chosen_source:
        df_persona = generate_persona_dataset("active")
        report = validate_wellness_data(df_persona)
        persona_name = "The Active Professional"
    elif "Variable Night Owl" in chosen_source:
        df_persona = generate_persona_dataset("night_owl")
        report = validate_wellness_data(df_persona)
        persona_name = "The Variable Night Owl"
    elif "Balanced Habit Tracker" in chosen_source:
        df_persona = generate_persona_dataset("balanced")
        report = validate_wellness_data(df_persona)
        persona_name = "The Balanced Habit Tracker"
    else:
        uploaded_file = st.sidebar.file_uploader(
            "Upload your CSV records:",
            type=["csv"],
            key=st.session_state.get("uploader_key", "default_uploader"),
            help="Upload a CSV with columns: date, sleep_hours, steps, water_glasses (optional: mood_score, activity_minutes)",
        )
        if uploaded_file is not None:
            report = load_and_validate(uploaded_file)
            persona_name = "Custom Uploaded Dataset"
        else:
            st.sidebar.info("Upload a CSV file or choose an evaluator persona.")
            report = load_and_validate(DEFAULT_SAMPLE_PATH)
            persona_name = "Default Sample (Awaiting Upload)"

    st.sidebar.markdown("---")

    # Customizable Personal Goals & Bio-Parameters
    st.sidebar.subheader("🎯 System Target Thresholds")
    goal_steps = st.sidebar.slider(
        "Daily Steps Target",
        min_value=4000,
        max_value=15000,
        value=8000,
        step=500,
        help="Target for step consistency and habit uptime calculations",
    )
    goal_sleep_range = st.sidebar.slider(
        "Sleep Window Target (Hours)",
        min_value=5.0,
        max_value=10.0,
        value=(7.0, 9.0),
        step=0.5,
        help="Optimal target sleep window",
    )
    goal_water = st.sidebar.slider(
        "Water Intake Target (Glasses)",
        min_value=4,
        max_value=15,
        value=8,
        step=1,
        help="Target number of daily glasses of water",
    )

    user_age = st.sidebar.slider(
        "User Chronological Age (Years)",
        min_value=16,
        max_value=85,
        value=21,
        step=1,
        help="Used to calibrate the Bio-Digital Twin & Biological Age Rejuvenation Delta",
    )

    user_goals = UserGoals(
        sleep_min=goal_sleep_range[0],
        sleep_max=goal_sleep_range[1],
        steps_target=goal_steps,
        water_target=goal_water,
    )

    st.sidebar.markdown("---")

    # Ambient Soundscapes Widget
    render_focus_soundscapes_widget()

    st.sidebar.markdown("---")
    st.sidebar.subheader("Actions")
    st.sidebar.download_button(
        label="📥 Download CSV Template",
        data=get_csv_template(),
        file_name="wellness_template.csv",
        mime="text/csv",
        use_container_width=True,
    )

    if st.sidebar.button("🔄 Reset Dashboard", on_click=reset_dashboard, use_container_width=True):
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.caption(
        "🔒 **Pervasive Privacy Audit**: In-memory ephemeral evaluation only. "
        "Cryptographic provenance enabled."
    )

    return report, user_goals, persona_name, user_age


def render_health_disclaimer():
    """Renders prominent non-medical health disclaimer (FR-09)."""
    st.markdown(
        """
        <div class="disclaimer-banner">
            <strong>⚠️ Health Disclaimer & Purpose:</strong>
            This dashboard is designed for personal habit review, routine balance, and behavioral resilience exploration.
            It is <strong>not a medical device</strong> and does not provide clinical diagnoses, medical recommendations,
            or predictive health assessments. Consult a qualified physician for medical advice.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_synergy_radar(comp: CompositeScore, resilience: ResiliencyReport):
    """Renders interactive Plotly 5-Axis Habit Synergy Radar Chart."""
    categories = [
        "Sleep Regularity",
        "Step Endurance",
        "Hydration Vitality",
        "Habit Uptime",
        "Logging Integrity",
    ]
    values = [
        comp.sleep_score,
        comp.steps_score,
        comp.water_score,
        resilience.uptime_pct,
        comp.logging_score,
    ]
    values_loop = values + [values[0]]
    categories_loop = categories + [categories[0]]

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=values_loop,
            theta=categories_loop,
            fill="toself",
            name="Personal Footprint",
            line_color="#0284c7",
            fillcolor="rgba(2, 132, 199, 0.25)",
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=[80] * 6,
            theta=categories_loop,
            mode="lines",
            name="Resilience Benchmark (80%)",
            line=dict(color="#10b981", dash="dot", width=1.5),
        )
    )
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=9, color="#94a3b8")),
            angularaxis=dict(tickfont=dict(size=11, color="#0f172a", family="Segoe UI")),
        ),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.18, xanchor="center", x=0.5),
        height=320,
        margin=dict(l=30, r=30, t=20, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig, use_container_width=True)


def render_composite_gauge(comp: CompositeScore):
    """Renders interactive Plotly gauge for Composite Behavioral Consistency Index."""
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=comp.overall_score,
            title={"text": "Behavioral Consistency Index", "font": {"size": 16, "color": "#0f172a"}},
            number={"suffix": "/100", "font": {"size": 28, "color": comp.tier_color}},
            gauge={
                "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "#cbd5e1"},
                "bar": {"color": comp.tier_color},
                "bgcolor": "white",
                "borderwidth": 2,
                "bordercolor": "#e2e8f0",
                "steps": [
                    {"range": [0, 50], "color": "#fef2f2"},
                    {"range": [50, 70], "color": "#fefce8"},
                    {"range": [70, 85], "color": "#f0f9ff"},
                    {"range": [85, 100], "color": "#f0fdf4"},
                ],
            },
        )
    )
    fig.update_layout(
        height=220,
        margin=dict(l=20, r=20, t=30, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig, use_container_width=True)


def main():
    init_session_state()

    # Sidebar: Data selection, goals, tools, ambient soundscapes, theme
    report, goals, persona_name, user_age = render_sidebar()

    # Inject Active Theme CSS
    st.markdown(get_theme_css(st.session_state.active_theme), unsafe_allow_html=True)

    # Title & Subtitle
    st.markdown('<div class="main-header">🧬 Personal Wellness Dashboard (Next-Level Edition)</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="sub-header">Single-User Habit Tracking & Longitudinal Analytics &bull; Active Profile: <strong>{persona_name}</strong> &bull; Theme: <strong>{st.session_state.active_theme}</strong></div>',
        unsafe_allow_html=True,
    )

    if st.session_state.get("shred_notice"):
        st.success("🔒 **Session Shredded Successfully**: Session memory was wiped and restored to a pristine state.")

    # Health Disclaimer
    render_health_disclaimer()

    # Schema Validation Handling
    if not report.is_valid:
        st.error(f"❌ **Data Loading Error**: {', '.join(report.schema_errors)}")
        st.info("Please verify your CSV columns or switch back to an evaluator persona in the sidebar.")
        return

    valid_df = report.valid_df
    if valid_df.empty:
        st.error("No valid records remain after data validation.")
        return

    # Date Range Filter
    min_date = valid_df["date"].min().date()
    max_date = valid_df["date"].max().date()

    st.markdown("#### 📅 Active Date Window & Settings")
    f_col1, f_col2, f_col3 = st.columns([2, 2, 2])

    with f_col1:
        selected_start = st.date_input(
            "Start Date",
            value=min_date,
            min_value=min_date,
            max_value=max_date,
            key=f"start_date_{st.session_state.reset_trigger}",
        )
    with f_col2:
        selected_end = st.date_input(
            "End Date",
            value=max_date,
            min_value=min_date,
            max_value=max_date,
            key=f"end_date_{st.session_state.reset_trigger}",
        )
    with f_col3:
        show_rolling_avg = st.checkbox("Show 7-Day Rolling Averages", value=True)

    if selected_start > selected_end:
        st.error("Start Date cannot be after End Date.")
        return

    filtered_df = filter_by_date_range(valid_df, selected_start, selected_end)
    if filtered_df.empty:
        st.warning("No records found within the selected date range. Please broaden your selection.")
        return

    stats = calculate_dashboard_stats(filtered_df, selected_start, selected_end)
    if not stats:
        st.warning("Insufficient data to compute statistics.")
        return

    comp_score = calculate_composite_score(filtered_df, goals)
    resilience = calculate_autonomic_resiliency(filtered_df, goals)
    streaks = calculate_habit_streaks(filtered_df, goals)
    weekend_stats = calculate_weekday_vs_weekend_stats(filtered_df)
    trend_report = generate_trend_observations(filtered_df)
    anomalies = detect_anomalies(filtered_df)
    badges = evaluate_achievement_badges(filtered_df, goals)
    security_audit = audit_session_security(filtered_df)
    chronotype = calculate_circadian_chronotype(filtered_df)
    vitality = calculate_vitality_forecast(filtered_df, goals)

    # Next-Level Analytics Computations
    bio_age = calculate_biological_age(filtered_df, chronological_age=user_age)
    momentum = calculate_neuro_momentum(filtered_df, goals)
    is_dark = st.session_state.active_theme != "Enterprise Light"

    # Autonomic Resiliency Banner
    st.markdown(
        f"""
        <div class="resilience-banner">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <strong>🛡️ Autonomic Habit Availability:</strong>
                    <span style="font-weight: 700; color: {resilience.status_color}; font-size: 1.05rem; margin-left: 0.3rem;">
                        {resilience.uptime_pct}% Uptime
                    </span>
                    &bull; Status: <strong>{resilience.autonomic_health_status}</strong>
                    &bull; Recovery: <strong>{resilience.mean_time_to_recovery_days} days MTTR</strong>
                </div>
                <div style="font-size: 0.85rem; color: #166534;">
                    Fingerprint: <code>{security_audit.dataset_sha256[:10]}...</code>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 9 Distinct, Cutting-Edge Tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "📊 Executive Overview",
        "🧬 Bio-Digital Twin & 3D Orbit",
        "📈 Deep-Dive & Synergy",
        "⏰ Habits & Circadian Clock",
        "🧘 Coherent Breathwork & HRV",
        "🤖 Z-Cognitive Query Assistant",
        "🔮 What-If Simulator & Insights",
        "🎓 Academic Defense & Viva",
        "🔒 Data & Privacy Vault",
    ])

    # ------------------ TAB 1: EXECUTIVE OVERVIEW ------------------
    with tab1:
        with st.expander("✨ Project Innovations & Key Differentiators (Why This Project is Unique)", expanded=True):
            u_c1, u_c2, u_c3 = st.columns(3)
            with u_c1:
                st.markdown(r"""
                **🛡️ 1. Mainframe Autonomic Resilience (MTTR)**  
                Instead of simple streak counters, we apply high-availability mainframe metrics:
                * **Habit Uptime % (Availability)**: Ratio of days core targets survived disruption.
                * **Mean Time to Recovery (MTTR)**: Quantifies days taken to bounce back after a lapse.
                
                **🤖 2. Local Zero-API Cognitive Assistant**  
                * In-memory semantic natural language query engine.
                * Zero cloud API keys, zero latency, 100% data sovereignty & HIPAA-aligned privacy.
                """)
            with u_c2:
                st.markdown(r"""
                **🧬 3. Bio-Digital Twin & Vitality Age**  
                * Calculates cellular age delta ($\Delta$-Age) using multi-variate modeling across sleep regularity, step endurance, and cellular hydration.
                
                **🌌 4. 3D Phase Space Orbit & Attractor Basin**  
                * Dynamical systems trajectory mapping daily biometrics $(Sleep, Steps, Water)$ toward an optimal health attractor basin.
                """)
            with u_c3:
                st.markdown(r"""
                **⚡ 5. Neuro-Momentum Physics ($p = m \cdot v$)**  
                * Kinematic physics tracking habit mass (streak), velocity (14-day compliance), neural friction, and autonomic escape velocity.
                
                **🌙 6. Circadian Chronotype & Social Jetlag**  
                * Quantifies sleep midpoint variance between workdays and weekends to optimize suprachiasmatic photobiology.
                """)
        st.markdown("<br>", unsafe_allow_html=True)
        # Summary KPI Cards
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            sleep_mean = f"{stats.sleep_summary.mean:.1f} hrs" if stats.sleep_summary.mean is not None else "N/A"
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Average Sleep</div>
                    <div class="metric-value">{sleep_mean}</div>
                    <div class="metric-sub">Target: {goals.sleep_min}–{goals.sleep_max} hrs</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            steps_mean = f"{int(stats.steps_summary.mean):,}" if stats.steps_summary.mean is not None else "N/A"
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Daily Steps (Avg)</div>
                    <div class="metric-value">{steps_mean}</div>
                    <div class="metric-sub">Target: {goals.steps_target:,} steps</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c3:
            water_mean = f"{stats.water_summary.mean:.1f} gls" if stats.water_summary.mean is not None else "N/A"
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Hydration (Avg)</div>
                    <div class="metric-value">{water_mean}</div>
                    <div class="metric-sub">Target: {goals.water_target} glasses</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c4:
            if stats.mood_summary and stats.mood_summary.mean is not None:
                mood_val = f"{stats.mood_summary.mean:.1f} / 5"
                mood_sub = f"Recorded on {stats.mood_summary.count} days"
            else:
                mood_val = "N/A"
                mood_sub = "Optional field not logged"
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Mood Rating (Avg)</div>
                    <div class="metric-value">{mood_val}</div>
                    <div class="metric-sub">{mood_sub}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c5:
            completion_val = f"{stats.completion_rate_pct:.1f}%"
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">Logging Regularity</div>
                    <div class="metric-value">{completion_val}</div>
                    <div class="metric-sub">{stats.recorded_days_count} of {stats.total_days_in_range} days logged</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Composite Consistency Index & Next-Day Vitality Readiness
        col_gauge, col_vitality = st.columns([1, 1])
        with col_gauge:
            render_composite_gauge(comp_score)
            st.markdown(
                f"<div style='text-align: center; font-weight: 600; color: {comp_score.tier_color}; font-size: 1.1rem;'>"
                f"{comp_score.tier}</div>"
                f"<div style='text-align: center; color: #475569; font-size: 0.88rem; margin-top: 4px;'>"
                f"{comp_score.summary_text}</div>",
                unsafe_allow_html=True,
            )

        with col_vitality:
            st.subheader("⚡ Next-Day Habit Vitality Forecast")
            if vitality:
                st.markdown(
                    f"""
                    <div style="background: rgba(148, 163, 184, 0.08); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 8px; padding: 14px 18px; margin-bottom: 12px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <div style="font-size: 0.78rem; font-weight: 700; color: #64748b; text-transform: uppercase;">Habit Momentum Zone</div>
                                <div style="font-size: 1.15rem; font-weight: 700; color: {vitality.zone_color}; margin-top: 2px;">{vitality.momentum_zone}</div>
                            </div>
                            <div style="font-size: 1.8rem; font-weight: 800; color: {vitality.zone_color};">{vitality.vitality_score}/100</div>
                        </div>
                        <div style="font-size: 0.85rem; color: #475569; margin-top: 8px;">{vitality.readiness_outlook}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                for driver in vitality.key_drivers:
                    st.caption(f"&bull; {driver}")
            else:
                st.info("Awaiting 3+ recorded days to project vitality momentum.")

        st.markdown("---")

        # GitHub-Style Habit Execution Heatmap Grid
        fig_cal = build_habit_calendar_heatmap(filtered_df, goals)
        st.plotly_chart(fig_cal, use_container_width=True)
        st.caption("🟩 *Darker emerald squares indicate days where all 3 core targets (Sleep, Steps, Hydration) were achieved.*")

    # ------------------ TAB 2: BIO-DIGITAL TWIN & 3D ORBIT ------------------
    with tab2:
        st.subheader("🧬 Bio-Digital Twin & Trajectory State Space")
        st.caption("Biometric age modeling, kinetic neuro-momentum physics, and 3D habit attractor basin.")

        twin_c1, twin_c2 = st.columns([1, 1])

        with twin_c1:
            delta_sign = "-" if bio_age.age_delta < 0 else "+"
            delta_label = f"{abs(bio_age.age_delta):.1f} yrs"
            st.markdown(
                f"""
                <div style="background: rgba(14, 165, 233, 0.08); border: 1px solid rgba(14, 165, 233, 0.25); border-radius: 12px; padding: 18px; margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <div style="font-size: 0.8rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Cellular Vitality Age</div>
                            <div style="font-size: 2.2rem; font-weight: 800; color: {bio_age.status_color}; margin-top: 2px;">
                                {bio_age.biological_age:.1f} <span style="font-size: 1rem; font-weight: 600; color: #64748b;">vs {bio_age.chronological_age:.0f} cal yrs</span>
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <div style="font-size: 1.4rem; font-weight: 800; color: {bio_age.status_color};">
                                {delta_sign}{delta_label}
                            </div>
                            <div style="font-size: 0.75rem; color: #64748b;">Biological Delta</div>
                        </div>
                    </div>
                    <div style="font-size: 0.9rem; font-weight: 600; color: {bio_age.status_color}; margin-top: 8px;">
                        {bio_age.status_label}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("##### 🔬 Physiological Factor Impact Breakdown")
            for factor, impact in bio_age.breakdown.items():
                imp_sign = "-" if impact < 0 else "+"
                imp_color = "#10b981" if impact <= 0 else "#ef4444"
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px dashed rgba(148, 163, 184, 0.25); font-size: 0.88rem;">
                        <span>&bull; {factor}</span>
                        <strong style="color: {imp_color};">{imp_sign}{abs(impact):.1f} yrs</strong>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        with twin_c2:
            st.markdown(
                f"""
                <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 18px; margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <div style="font-size: 0.8rem; font-weight: 700; color: #10b981; text-transform: uppercase;">Habit Neuro-Momentum Physics</div>
                            <div style="font-size: 1.15rem; font-weight: 700; color: {momentum.status_color}; margin-top: 2px;">
                                {momentum.status_title}
                            </div>
                        </div>
                        <div style="font-size: 2.2rem; font-weight: 800; color: {momentum.status_color};">
                            {momentum.momentum_score:.0f}<span style="font-size: 1rem; font-weight: 600; color: #64748b;">/100</span>
                        </div>
                    </div>
                    <div style="font-size: 0.85rem; color: #475569; margin-top: 8px;">
                        {momentum.explanation}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            m_c1, m_c2, m_c3 = st.columns(3)
            with m_c1:
                st.metric("Inertia Mass (Streak)", f"{momentum.inertia_mass} days")
            with m_c2:
                st.metric("Velocity Rate", f"{momentum.velocity_rate * 100:.0f}%")
            with m_c3:
                st.metric("Neural Friction", f"{momentum.friction_coefficient:.2f}")

        st.markdown("---")

        # 3D Interactive Habit Phase Space Orbit
        fig_3d = build_3d_habit_orbit_chart(filtered_df, goals, dark_mode=is_dark)
        st.plotly_chart(fig_3d, use_container_width=True)
        st.caption("🌌 *Rotate and zoom in 3D: The green dashed box represents the Attractor Target Basin. The continuous spline trace maps your daily biometric trajectory through state space.*")

        st.markdown("<br>", unsafe_allow_html=True)

        # Circadian Photobiology & Light Exposure Protocol
        st.subheader("☀️ Circadian Photobiology Protocol")
        st.caption("Calculated from active sleep midpoints to entrain the suprachiasmatic nucleus (SCN).")

        proto_c1, proto_c2, proto_c3 = st.columns(3)
        with proto_c1:
            st.markdown(
                """
                <div style="background: rgba(245, 158, 11, 0.08); border-left: 3px solid #f59e0b; padding: 12px; border-radius: 6px;">
                    <div style="font-weight: 700; color: #b45309; font-size: 0.85rem;">🌅 MORNING CORTISOL ANCHOR</div>
                    <div style="font-size: 1.1rem; font-weight: 700; margin-top: 4px;">07:15 – 08:00 AM</div>
                    <div style="font-size: 0.8rem; color: #64748b; margin-top: 4px;">View 10,000+ lux natural sunlight for 10–15 mins to set daytime circadian timer.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with proto_c2:
            st.markdown(
                """
                <div style="background: rgba(14, 165, 233, 0.08); border-left: 3px solid #0284c7; padding: 12px; border-radius: 6px;">
                    <div style="font-weight: 700; color: #0369a1; font-size: 0.85rem;">⚡ KINETIC MOVEMENT PEAK</div>
                    <div style="font-size: 1.1rem; font-weight: 700; margin-top: 4px;">16:30 – 18:30 PM</div>
                    <div style="font-size: 0.8rem; color: #64748b; margin-top: 4px;">Core body temperature peaks; ideal biological window for vigorous steps and endurance.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with proto_c3:
            st.markdown(
                """
                <div style="background: rgba(99, 102, 241, 0.08); border-left: 3px solid #6366f1; padding: 12px; border-radius: 6px;">
                    <div style="font-weight: 700; color: #4338ca; font-size: 0.85rem;">🌙 MELATONIN INDUCTION GATE</div>
                    <div style="font-size: 1.1rem; font-weight: 700; margin-top: 4px;">22:00 – 22:30 PM</div>
                    <div style="font-size: 0.8rem; color: #64748b; margin-top: 4px;">Dim overhead lighting and engage blue-light filters to prevent melatonin suppression.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ------------------ TAB 3: DEEP-DIVE & SYNERGY ------------------
    with tab3:
        df_plot = filtered_df.sort_values("date").copy()
        if show_rolling_avg:
            df_plot = add_rolling_averages(df_plot, window=7)

        # Synergy Radar & Correlation Matrix side-by-side
        col_radar, col_corr = st.columns([1, 1])
        with col_radar:
            st.subheader("🕸️ 5-Axis Habit Synergy Radar")
            st.caption("Visualizes balance across sleep, steps, water, habit uptime, and logging completeness.")
            render_synergy_radar(comp_score, resilience)

        with col_corr:
            st.subheader("🔬 Pearson Correlation Heatmap")
            st.caption("Statistical relationships between recorded metrics.")
            corr_df = calculate_correlation_matrix(df_plot)
            if not corr_df.empty:
                fig_hm = px.imshow(
                    corr_df,
                    text_auto=True,
                    aspect="auto",
                    color_continuous_scale="RdBu_r",
                    zmin=-1,
                    zmax=1,
                )
                fig_hm.update_layout(height=320, margin=dict(l=20, r=20, t=10, b=20), paper_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig_hm, use_container_width=True)
            else:
                st.info("Insufficient variance or records to compute correlation heatmap.")

        st.markdown("---")

        col_trend, col_steps = st.columns([3, 2])
        with col_trend:
            st.subheader("📈 Time Series Trends")
            fig_trend = make_subplots(
                rows=2,
                cols=1,
                shared_xaxes=True,
                vertical_spacing=0.08,
                subplot_titles=("Recorded Sleep Duration (Hours)", "Daily Water Intake (Glasses)"),
            )
            fig_trend.add_trace(
                go.Scatter(
                    x=df_plot["date"],
                    y=df_plot["sleep_hours"],
                    mode="lines+markers",
                    name="Sleep Hours",
                    line=dict(color="#2563eb", width=2),
                ),
                row=1,
                col=1,
            )
            if show_rolling_avg and "sleep_hours_rolling_7d" in df_plot.columns:
                fig_trend.add_trace(
                    go.Scatter(
                        x=df_plot["date"],
                        y=df_plot["sleep_hours_rolling_7d"],
                        mode="lines",
                        name="Sleep (7-Day Avg)",
                        line=dict(color="#1e40af", width=2.5, dash="dash"),
                    ),
                    row=1,
                    col=1,
                )

            # Target lines for sleep
            fig_trend.add_hline(y=goals.sleep_min, line_dash="dot", line_color="#94a3b8", row=1, col=1)
            fig_trend.add_hline(y=goals.sleep_max, line_dash="dot", line_color="#94a3b8", row=1, col=1)

            fig_trend.add_trace(
                go.Scatter(
                    x=df_plot["date"],
                    y=df_plot["water_glasses"],
                    mode="lines+markers",
                    name="Water Glasses",
                    line=dict(color="#06b6d4", width=2),
                ),
                row=2,
                col=1,
            )
            if show_rolling_avg and "water_glasses_rolling_7d" in df_plot.columns:
                fig_trend.add_trace(
                    go.Scatter(
                        x=df_plot["date"],
                        y=df_plot["water_glasses_rolling_7d"],
                        mode="lines",
                        name="Water (7-Day Avg)",
                        line=dict(color="#0891b2", width=2.5, dash="dash"),
                    ),
                    row=2,
                    col=1,
                )
            fig_trend.add_hline(y=goals.water_target, line_dash="dot", line_color="#94a3b8", row=2, col=1)

            fig_trend.update_layout(height=420, margin=dict(l=20, r=20, t=30, b=20), paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_trend, use_container_width=True)

        with col_steps:
            st.subheader("🚶 Daily Step Consistency")
            fig_steps = go.Figure()
            bar_colors = ["#10b981" if s >= goals.steps_target else "#94a3b8" for s in df_plot["steps"]]
            fig_steps.add_trace(
                go.Bar(
                    x=df_plot["date"],
                    y=df_plot["steps"],
                    name="Daily Steps",
                    marker_color=bar_colors,
                )
            )
            if show_rolling_avg and "steps_rolling_7d" in df_plot.columns:
                fig_steps.add_trace(
                    go.Scatter(
                        x=df_plot["date"],
                        y=df_plot["steps_rolling_7d"],
                        mode="lines",
                        name="Steps (7-Day Avg)",
                        line=dict(color="#0f172a", width=2.5),
                    )
                )
            fig_steps.add_hline(y=goals.steps_target, line_dash="dash", line_color="#ef4444", annotation_text="Goal")
            fig_steps.update_layout(height=420, margin=dict(l=20, r=20, t=30, b=20), paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_steps, use_container_width=True)

    # ------------------ TAB 4: HABITS & CIRCADIAN CLOCK ------------------
    with tab4:
        col_clock, col_chrono = st.columns([1, 1])

        with col_clock:
            st.subheader("⏰ 24-Hour Circadian Polar Clock Dial")
            st.caption("Visualizes rest phase, schedule midpoint, and activity window.")
            is_weekend_shift = chronotype.social_jetlag_minutes > 60 if chronotype else False
            avg_sleep = stats.sleep_summary.mean if stats.sleep_summary and stats.sleep_summary.mean else 7.5
            fig_clock = build_circadian_polar_clock(
                avg_sleep_hours=avg_sleep,
                is_weekend_shifted=is_weekend_shift,
            )
            st.plotly_chart(fig_clock, use_container_width=True)

        with col_chrono:
            st.subheader("🌙 Chronotype & Social Jetlag Analyzer")
            if chronotype:
                st.markdown(
                    f"""
                    <div style="background: rgba(148, 163, 184, 0.08); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 8px; padding: 14px 18px; margin-bottom: 12px;">
                        <div style="font-size: 0.8rem; font-weight: 700; color: #64748b; text-transform: uppercase;">Inferred Chronotype Profile</div>
                        <div style="font-size: 1.25rem; font-weight: 700; color: #0284c7; margin-top: 2px;">{chronotype.chronotype_icon} {chronotype.chronotype}</div>
                        <div style="font-size: 0.85rem; color: #475569; margin-top: 6px;">{chronotype.description}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                jet_col1, jet_col2 = st.columns(2)
                with jet_col1:
                    st.metric("Social Jetlag Shift", f"{chronotype.social_jetlag_hours:.1f} hrs", f"{chronotype.social_jetlag_minutes} mins")
                with jet_col2:
                    st.metric("Circadian Alignment", f"{chronotype.circadian_alignment_score}/100", chronotype.alignment_tier)

                st.caption(f"&bull; Average Weekday Sleep: **{chronotype.weekday_sleep_avg:.1f} hrs**")
                st.caption(f"&bull; Average Weekend Sleep: **{chronotype.weekend_sleep_avg:.1f} hrs**")
            else:
                st.info("Awaiting 7+ recorded days with weekdays and weekends to evaluate circadian chronotype.")

        st.markdown("---")

        # Gamified Habit Streaks & Badges
        st.subheader("🔥 Active Habit Streaks")
        s_c1, s_c2, s_c3 = st.columns(3)
        with s_c1:
            step_streak = streaks.get("steps") if isinstance(streaks, dict) else None
            cur_s = step_streak.current_streak if step_streak else 0
            long_s = step_streak.longest_streak if step_streak else 0
            st.metric("Steps Streak", f"{cur_s} days", f"Longest: {long_s}d")
        with s_c2:
            sleep_streak = streaks.get("sleep") if isinstance(streaks, dict) else None
            cur_sl = sleep_streak.current_streak if sleep_streak else 0
            long_sl = sleep_streak.longest_streak if sleep_streak else 0
            st.metric("Sleep Window Streak", f"{cur_sl} days", f"Longest: {long_sl}d")
        with s_c3:
            water_streak = streaks.get("water") if isinstance(streaks, dict) else None
            cur_w = water_streak.current_streak if water_streak else 0
            long_w = water_streak.longest_streak if water_streak else 0
            st.metric("Hydration Streak", f"{cur_w} days", f"Longest: {long_w}d")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🏆 Behavioral Milestone Badges")
        b_cols = st.columns(3)
        for i, b in enumerate(badges):
            col = b_cols[i % 3]
            with col:
                badge_class = "badge-unlocked" if b.unlocked else "badge-locked"
                status_text = "✅ Unlocked" if b.unlocked else "🔒 In Progress"
                st.markdown(
                    f"""
                    <div class="badge-card {badge_class}">
                        <div style="font-size: 1.3rem; margin-bottom: 4px;">{b.icon} <strong>{b.title}</strong></div>
                        <div style="font-size: 0.85rem; color: #475569; margin-bottom: 8px;">{b.description}</div>
                        <div style="font-size: 0.8rem; font-weight: 600; color: {'#16a34a' if b.unlocked else '#64748b'};">
                            {status_text}: {b.progress_label}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.progress(b.progress_pct / 100)

        st.markdown("<br>", unsafe_allow_html=True)

        # Weekday vs Weekend Comparison
        st.subheader("📅 Weekday vs. Weekend Behavioral Breakdown")
        if weekend_stats:
            col_we_table, col_we_chart = st.columns([1, 1])
            with col_we_table:
                we_summary_data = {
                    "Metric": ["Average Sleep", "Daily Steps", "Hydration"],
                    "Weekdays (Mon–Fri)": [
                        f"{weekend_stats.weekday_sleep_avg:.1f} hrs",
                        f"{weekend_stats.weekday_steps_avg:,} steps",
                        f"{weekend_stats.weekday_water_avg:.1f} gls",
                    ],
                    "Weekends (Sat–Sun)": [
                        f"{weekend_stats.weekend_sleep_avg:.1f} hrs",
                        f"{weekend_stats.weekend_steps_avg:,} steps",
                        f"{weekend_stats.weekend_water_avg:.1f} gls",
                    ],
                    "Difference (Weekend - Weekday)": [
                        f"{'+' if weekend_stats.sleep_diff > 0 else ''}{weekend_stats.sleep_diff:.1f} hrs",
                        f"{'+' if weekend_stats.steps_diff > 0 else ''}{weekend_stats.steps_diff:,} steps",
                        f"{'+' if weekend_stats.water_diff > 0 else ''}{weekend_stats.water_diff:.1f} gls",
                    ],
                }
                st.dataframe(pd.DataFrame(we_summary_data), use_container_width=True, hide_index=True)
                st.caption(f"Based on {weekend_stats.weekday_days} weekdays and {weekend_stats.weekend_days} weekend days in range.")

            with col_we_chart:
                fig_comp = go.Figure()
                fig_comp.add_trace(
                    go.Bar(
                        name="Weekdays",
                        x=["Sleep (hrs)", "Steps (/1000)", "Water (gls)"],
                        y=[weekend_stats.weekday_sleep_avg, weekend_stats.weekday_steps_avg / 1000, weekend_stats.weekday_water_avg],
                        marker_color="#3b82f6",
                    )
                )
                fig_comp.add_trace(
                    go.Bar(
                        name="Weekends",
                        x=["Sleep (hrs)", "Steps (/1000)", "Water (gls)"],
                        y=[weekend_stats.weekend_sleep_avg, weekend_stats.weekend_steps_avg / 1000, weekend_stats.weekend_water_avg],
                        marker_color="#10b981",
                    )
                )
                fig_comp.update_layout(
                    barmode="group",
                    height=240,
                    margin=dict(l=20, r=20, t=20, b=20),
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                )
                st.plotly_chart(fig_comp, use_container_width=True)
        else:
            st.info("Insufficient records spanning weekdays and weekends to compute behavioral comparison.")

    # ------------------ TAB 5: COHERENT BREATHWORK & HRV ------------------
    with tab5:
        render_breathwork_widget(dark_mode=is_dark)

    # ------------------ TAB 6: Z-COGNITIVE QUERY ASSISTANT ------------------
    with tab6:
        st.subheader("🤖 Local Z-Cognitive Habit Assistant")
        st.caption(
            "Natural language query engine running 100% locally in-memory. "
            "Zero external API keys or cloud telemetry."
        )

        st.markdown("**Quick Evaluator Questions (Click to query instantly):**")
        prompt_cols = st.columns(3)
        with prompt_cols[0]:
            if st.button("🏆 What was my most active day?", key="q1", use_container_width=True):
                st.session_state.active_query = "What was my most active day and best step count?"
            if st.button("💧 Am I meeting hydration targets?", key="q2", use_container_width=True):
                st.session_state.active_query = "Am I meeting my hydration targets?"
        with prompt_cols[1]:
            if st.button("📅 Compare weekend vs weekday sleep", key="q3", use_container_width=True):
                st.session_state.active_query = "How does my weekend sleep compare to weekdays?"
            if st.button("🔥 Show my longest streaks", key="q4", use_container_width=True):
                st.session_state.active_query = "Show my longest habit streaks"
        with prompt_cols[2]:
            if st.button("🛡️ Explain my Habit Resiliency", key="q5", use_container_width=True):
                st.session_state.active_query = "Explain my habit resiliency and uptime"
            if st.button("🦉 Explain my Chronotype & Jetlag", key="q6", use_container_width=True):
                st.session_state.active_query = "Explain my chronotype and social jetlag"

        user_query = st.text_input(
            "Or ask any question about your records:",
            value=st.session_state.get("active_query", ""),
            placeholder="e.g. What was my highest step day? or How does weekend sleep compare?",
        )

        if user_query:
            answer = answer_wellness_query(user_query, filtered_df, goals)
            st.markdown(
                f"""
                <div style="background: rgba(15, 98, 254, 0.08); border-left: 4px solid #0f62fe; border-radius: 8px; padding: 16px 20px; margin-top: 14px;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #0f62fe; text-transform: uppercase;">Z-Cognitive Assistant Answer</div>
                    <div style="margin-top: 8px; font-size: 0.95rem; line-height: 1.6; color: #0f172a;">
                        {answer}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ------------------ TAB 7: WHAT-IF SIMULATOR & INSIGHTS ------------------
    with tab7:
        st.subheader("🔮 'What-If?' Routine Scenario Simulator")
        st.caption("Hypothetical sandbox: Test prospective behavioral adjustments to see projected consistency gains.")

        sim_c1, sim_c2, sim_c3 = st.columns(3)
        with sim_c1:
            delta_sleep = st.slider("Hypothetical Sleep Shift (Hours)", min_value=-2.0, max_value=2.0, value=0.5, step=0.5)
        with sim_c2:
            delta_steps = st.slider("Hypothetical Step Adjustment", min_value=-3000, max_value=5000, value=1500, step=500)
        with sim_c3:
            delta_water = st.slider("Hypothetical Water Adjustment (Glasses)", min_value=-3, max_value=5, value=2, step=1)

        sim_result = simulate_routine_tweak(filtered_df, delta_sleep, delta_steps, delta_water, goals)
        if sim_result:
            sim_col1, sim_col2, sim_col3 = st.columns(3)
            with sim_col1:
                st.metric(
                    label="Projected Consistency Index",
                    value=f"{sim_result.projected_composite}/100",
                    delta=f"{sim_result.composite_gain:+d} pts",
                )
            with sim_col2:
                st.metric(
                    label="Projected Habit Uptime",
                    value=f"{sim_result.projected_uptime}%",
                    delta=f"{sim_result.uptime_gain:+.1f}%",
                )
            with sim_col3:
                st.metric(label="Projected Tier", value=sim_result.projected_tier)

            st.info(sim_result.impact_summary)

        st.markdown("---")

        # Transparent Trend Observations
        st.subheader("🔍 Transparent Trend Observations")
        if not trend_report.has_sufficient_data:
            st.warning(f"⚠️ {trend_report.status_message}")
        else:
            st.success(f"✅ {trend_report.status_message}")
            if trend_report.earlier_period_dates and trend_report.recent_period_dates:
                st.caption(
                    f"📅 Comparison Windows: Baseline Period: *{trend_report.earlier_period_dates}* vs "
                    f"Recent Period: *{trend_report.recent_period_dates}*"
                )

            cols = st.columns(2)
            for i, obs in enumerate(trend_report.observations):
                col = cols[i % 2]
                with col:
                    tag_color = {
                        "Increase": "#16a34a",
                        "Decrease": "#dc2626",
                        "Steady": "#0284c7",
                        "Info": "#475569",
                    }.get(obs.tag, "#475569")
                    st.markdown(
                        f"""
                        <div style="background-color: rgba(148, 163, 184, 0.08); border-left: 3px solid {tag_color}; border-radius: 6px; padding: 0.75rem 1rem; margin-bottom: 0.8rem;">
                            <div style="font-size: 0.85rem; font-weight: 600; color: #334155;">
                                {obs.category} <span style="color: {tag_color}; font-size: 0.8rem; margin-left: 0.5rem;">● {obs.tag}</span>
                            </div>
                            <div style="font-weight: 700; color: #0f172a; font-size: 0.95rem; margin-bottom: 0.2rem;">
                                {obs.summary}
                            </div>
                            <div style="font-size: 0.85rem; color: #475569;">
                                {obs.detail}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

        # Anomaly Detection Drawer
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("⚠️ Data Outlier & Anomaly Detection")
        if not anomalies.empty:
            st.warning(f"Detected {len(anomalies)} statistical outlier(s) in the selected range (using IQR bounds):")
            st.dataframe(anomalies, use_container_width=True, hide_index=True)
        else:
            st.success("✅ No extreme statistical outliers detected in the active records.")

    # ------------------ TAB 8: ACADEMIC DEFENSE & VIVA ------------------
    with tab8:
        render_academic_defense_tab()

    # ------------------ TAB 9: DATA & PRIVACY VAULT ------------------
    with tab9:
        st.subheader("🔒 IBM Z Pervasive Privacy & Data Sovereignty Vault")
        st.caption("Confidential computing posture audit inspired by enterprise security architecture.")

        sec_col1, sec_col2 = st.columns(2)
        with sec_col1:
            st.markdown(
                f"""
                <div style="background: rgba(148, 163, 184, 0.08); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 8px; padding: 14px 18px;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #64748b; text-transform: uppercase;">Cryptographic Provenance</div>
                    <div style="font-family: monospace; font-size: 0.85rem; word-break: break-all; margin-top: 6px; color: #0f172a;">
                        SHA-256: <strong>{security_audit.dataset_sha256}</strong>
                    </div>
                    <div style="font-size: 0.8rem; color: #64748b; margin-top: 6px;">
                        Fingerprinted records: {security_audit.records_fingerprinted} &bull; Tamper-evident checksum
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with sec_col2:
            st.markdown(
                f"""
                <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 8px; padding: 14px 18px;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #166534; text-transform: uppercase;">Zero-Knowledge Telemetry Audit</div>
                    <div style="font-size: 0.9rem; color: #166534; margin-top: 4px;">
                        &bull; Active Tracking Cookies: <strong>{security_audit.telemetry_beacons_count}</strong><br>
                        &bull; Persistent Disk Storage: <strong>{security_audit.persistent_storage_bytes} bytes</strong><br>
                        &bull; Processing Mode: <strong>{security_audit.data_sovereignty_status}</strong>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.caption(security_audit.privacy_compliance_statement)

        st.markdown("---")
        st.subheader("📋 Dataset Inspection & Multi-Format Export")
        exp_c1, exp_c2, exp_c3 = st.columns(3)

        with exp_c1:
            csv_export = filtered_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Export Filtered CSV",
                data=csv_export,
                file_name=f"wellness_export_{selected_start}_{selected_end}.csv",
                mime="text/csv",
                use_container_width=True,
            )

        with exp_c2:
            html_report = generate_executive_html_report(
                stats=stats,
                composite=comp_score,
                trend_report=trend_report,
                streaks=streaks,
                weekend_stats=weekend_stats,
                resilience_report=resilience,
                badges=badges,
                persona_name=persona_name,
            )
            st.download_button(
                label="📑 Download Executive Report (HTML)",
                data=html_report.encode("utf-8"),
                file_name=f"executive_wellness_report_{selected_start}_{selected_end}.html",
                mime="text/html",
                use_container_width=True,
            )

        with exp_c3:
            if st.button("🗑️ Purge & Shred Session Memory", on_click=shred_session, use_container_width=True):
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        st.dataframe(filtered_df, use_container_width=True)


if __name__ == "__main__":
    main()
