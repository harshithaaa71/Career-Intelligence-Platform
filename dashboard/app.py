import streamlit as st
from pathlib import Path
import PyPDF2

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Career Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
def load_css():

    css_path = Path(__file__).parent.parent / "assets" / "style.css"

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -----------------------------
# SIDEBAR
# -----------------------------
st.markdown("# 🚀 Career Intelligence Platform")

page = st.radio(
    "",
    [
        "🏠 Home",
        "📄 Resume Analyzer",
        "📊 Job Match",
        "⚠ Skill Gap Analysis",
        "🎯 Career Recommendations",
        "📈 Market Insights"
    ],
    horizontal=True
)

# =============================
# HOME PAGE
# =============================
if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero">
            <h1>🚀 Career Intelligence & Opportunity Analytics Platform</h1>
            <p>
                AI-Powered Resume Analysis, Skill Gap Detection,
                Career Recommendations, and Application Readiness Insights
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("## 🎯 What This Platform Does")

    st.markdown("""
    ✅ Analyze resumes

    ✅ Match resumes with job requirements

    ✅ Identify missing skills

    ✅ Recommend suitable career paths

    ✅ Evaluate application readiness

    ✅ Provide career intelligence insights
    """)

    st.write("")

    st.markdown("## 📊 Quick Insights")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Match Score",
            value="50%"
        )

    with col2:
        st.metric(
            label="Missing Skills",
            value="1"
        )

    with col3:
        st.metric(
            label="Recommended Career",
            value="Data Analyst"
        )

    st.write("")

    st.markdown("## 🚀 Platform Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
📄 Resume Analyzer

Upload resumes and automatically extract skills.
""")

        st.info("""
⚠ Skill Gap Analysis

Identify missing skills required for target roles.
""")

    with col2:

        st.info("""
🎯 Career Recommendation Engine

Recommend suitable career paths based on skills.
""")

        st.info("""
📈 Application Readiness

Understand how prepared you are for opportunities.
""")

# =============================
# RESUME ANALYZER
# =============================
elif page == "📄 Resume Analyzer":

    import sys
    from pathlib import Path
    import PyPDF2

    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))

    from src.skill_extractor import extract_skills

    st.title("📄 Resume Analyzer")

    st.write(
        "Upload your resume PDF or paste resume text below."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    resume_text = ""

    if uploaded_file is not None:

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        for page in pdf_reader.pages:

            text = page.extract_text()

            if text:
                resume_text += text

    resume_text = st.text_area(
        "Or Paste Resume Content",
        value=resume_text,
        height=250
    )

    skill_list = [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Tableau",
        "Pandas",
        "NumPy",
        "Communication",
        "Reporting",
        "Statistics",
        "Machine Learning",
        "Data Analysis",
        "Business Analysis",
        "Git",
        "Streamlit"
    ]

    if st.button("Analyze Resume"):

        skills = extract_skills(
            resume_text,
            skill_list
        )

        st.success(
            "Resume analyzed successfully!"
        )

        st.subheader(
            "🎯 Extracted Skills"
        )

        if skills:

            for skill in skills:
                st.write(f"✅ {skill}")

        else:

            st.warning(
                "No matching skills found."
            )
# =============================
# JOB MATCH
# =============================
elif page == "📊 Job Match":

    from src.job_matcher import calculate_match

    st.title("📊 Job Match Engine")

    st.write(
        "Compare your skills against a target role."
    )

    resume_input = st.text_input(
        "Resume Skills (comma separated)"
    )

    job_input = st.text_input(
        "Job Skills (comma separated)"
    )

    if st.button("Calculate Match"):

        resume_skills = [
            skill.strip()
            for skill in resume_input.split(",")
        ]

        job_skills = [
            skill.strip()
            for skill in job_input.split(",")
        ]

        score, matched, missing = calculate_match(
            resume_skills,
            job_skills
        )

        st.subheader("📈 Match Results")

        # Match Score
        st.metric(
            label="Match Score",
            value=f"{score:.0f}%"
        )

        # Matched Skills
        st.markdown("### ✅ Matched Skills")

        matched_html = ""

        for skill in matched:
            matched_html += f"""
            <span class='skill-tag-green'>
                {skill}
            </span>
            """

        st.markdown(
            matched_html,
            unsafe_allow_html=True
        )

        # Missing Skills
        st.markdown("### ⚠ Missing Skills")

        missing_html = ""

        for skill in missing:
            missing_html += f"""
            <span class='skill-tag-red'>
                {skill}
            </span>
            """

        st.markdown(
            missing_html,
            unsafe_allow_html=True
        )

# =============================
# SKILL GAP
# =============================
elif page == "⚠ Skill Gap Analysis":

    import sys
    from pathlib import Path

    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))

    from src.skill_gap import analyze_skill_gap

    st.title("⚠ Skill Gap Analysis")

    st.write(
        "Compare your skills against a target role."
    )

    user_input = st.text_input(
        "Your Skills (comma separated)"
    )

    role = st.radio(
        "Target Role",
        [
            "Data Analyst",
            "Business Analyst",
            "Data Scientist"
        ]
    )

    role_skills = {

        "Data Analyst": [
            "Python",
            "SQL",
            "Excel",
            "Power BI",
            "Statistics",
            "Reporting",
            "Communication"
        ],

        "Business Analyst": [
            "Excel",
            "SQL",
            "Communication",
            "Reporting",
            "Business Analysis"
        ],

        "Data Scientist": [
            "Python",
            "Machine Learning",
            "Statistics",
            "Pandas",
            "NumPy",
            "SQL"
        ]
    }

    if st.button("Analyze Skill Gap"):

        user_skills = [
            skill.strip()
            for skill in user_input.split(",")
        ]

        readiness, matched, missing = analyze_skill_gap(
            user_skills,
            role_skills[role]
        )

        st.metric(
            label="Readiness Score",
            value=f"{readiness:.0f}%"
        )

        st.markdown("### ✅ Skills You Have")

        for skill in matched:
            st.success(skill)

        st.markdown("### ⚠ Missing Skills")

        for skill in missing:
            st.error(skill)


# =============================
# CAREER RECOMMENDATIONS
# =============================
elif page == "🎯 Career Recommendations":

    import sys
    from pathlib import Path

    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))

    from src.career_recommender import recommend_careers

    st.title("🎯 Career Recommendation Engine")

    st.write(
        "Get career recommendations based on your skills."
    )

    user_input = st.text_input(
        "Enter your skills (comma separated)"
    )

    if st.button("Recommend Career"):

        user_skills = [
            skill.strip()
            for skill in user_input.split(",")
        ]

        recommendations = recommend_careers(user_skills)

        top_career = recommendations[0][0]
        top_score = recommendations[0][1]

        st.success(
            f"🎯 Recommended Career: {top_career} ({top_score:.0f}% Match)"
        )

        st.markdown("## 🏆 Top Career Matches")

        for career, score in recommendations:

            st.metric(
                label=career,
                value=f"{score:.0f}%"
            )

# =============================
# MARKET INSIGHTS
# =============================
# =============================
# MARKET INSIGHTS
# =============================
elif page == "📈 Market Insights":

    import sys
    from pathlib import Path

    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))

    from src.market_insights import get_market_data

    st.title("📈 Market Insights")

    st.write(
        "Current demand for popular data careers skills."
    )

    df = get_market_data()

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader(
        "🔥 Skill Demand Trends"
    )

    st.bar_chart(
        df.set_index("Skill")
    )
