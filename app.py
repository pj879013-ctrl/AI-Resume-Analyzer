from modules.custom_jd_matcher import analyze_custom_job
import streamlit as st
import pandas as pd
from modules.skill_gap import analyze_skill_gap
from modules.resume_parser import extract_resume_text
from modules.skill_extractor import extract_skills, count_total_skills
from modules.job_matcher import match_jobs
from modules.recommendation import (
    recommend_jobs,
    get_recommendation_message
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM CSS - MODERN UI
# ==========================================

st.markdown("""
<style>

/* Main background */

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #25204b 0%, transparent 38%),
        radial-gradient(ellipse at 90% 20%, #172c50 0%, transparent 35%),
        #0b1020;
    color: #f5f7ff;
}

/* Main container */

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #17152e,
        #111a32,
        #101629
    );
    border-right: 1px solid #34365c;
}

/* Headings */

h1, h2, h3 {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* Hero section */

.hero {
    background: linear-gradient(
        120deg,
        #292052,
        #17335a,
        #38235c
    );
    background-size: 200% 200%;
    animation: gradientMove 9s ease infinite;
    border: 1px solid #6254a8;
    border-radius: 22px;
    padding: 35px;
    margin-bottom: 28px;
    box-shadow: 0 12px 40px rgba(90, 65, 190, 0.18);
    animation: fadeIn 0.8s ease, gradientMove 9s ease infinite;
}

.hero h1 {
    font-size: 42px !important;
    background: linear-gradient(90deg, #ffffff, #b7a5ff, #80d9ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #d2d8f5;
    font-size: 16px;
}

/* Glass cards */

.glass-card {
    background: rgba(34, 43, 76, 0.78);
    border: 1px solid rgba(147, 135, 220, 0.28);
    border-radius: 18px;
    padding: 23px;
    margin-bottom: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeIn 0.7s ease;
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(117, 69, 232, 0.22);
}

/* Metric cards */

.metric-card {
    background: linear-gradient(135deg, #222d50, #302653);
    border: 1px solid #57508b;
    border-radius: 18px;
    padding: 22px;
    min-height: 125px;
    transition: all 0.3s ease;
    animation: fadeIn 0.8s ease;
}

.metric-card:hover {
    transform: translateY(-6px);
    border-color: #a58aff;
    box-shadow: 0 10px 30px rgba(128, 95, 255, 0.22);
}

.metric-label {
    color: #c2c8e4;
    font-size: 14px;
}

.metric-value {
    font-size: 29px;
    font-weight: 800;
    color: #71e6bd;
    margin-top: 12px;
    overflow-wrap: anywhere;
}

/* Skill badges */

.skill-chip {
    display: inline-block;
    background: linear-gradient(135deg, #493b88, #27517b);
    border: 1px solid #7770c7;
    color: white;
    padding: 8px 14px;
    border-radius: 30px;
    margin: 5px 5px 5px 0;
    font-size: 13px;
    transition: all 0.25s ease;
}

.skill-chip:hover {
    background: linear-gradient(135deg, #7956db, #347bc1);
    transform: scale(1.06);
}

/* Buttons */

.stButton > button {
    background: linear-gradient(110deg, #7951e8, #4169e1);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 24px;
    font-weight: 700;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(115, 78, 235, 0.45);
}

/* Upload section */

[data-testid="stFileUploader"] {
    background: rgba(42, 48, 82, 0.6);
    border: 1px dashed #8874dc;
    border-radius: 16px;
    padding: 15px;
}

/* Progress bars */

.stProgress > div > div > div {
    background: linear-gradient(90deg, #8c5cff, #48d9cf);
}

/* Animation */

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Download button */

.stDownloadButton > button {
    background: linear-gradient(110deg, #167e78, #2563a5);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown(
    """
    <div style="text-align:center; padding:20px 5px;">
        <div style="font-size:45px;">🤖</div>
        <h2 style="color:#ffffff;">AI Resume Analyzer</h2>
        <p style="color:#aeb8dc;">Smart Career Intelligence</p>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Analyze Resume",
        "Custom Job Match",
        "About Project"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style="color:#aeb8dc; font-size:13px;">
        <b>POWERED BY</b><br><br>
        🐍 Python<br>
        🧠 Machine Learning<br>
        📊 NLP Technology<br>
        ⚡ Streamlit
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">
    <h1>AI Resume Analyzer</h1>
    <p>
        Analyze your resume. Discover your skills.
        Find career opportunities with AI and Machine Learning.
    </p>
    <div style="margin-top:18px;">
        <span class="skill-chip">AI Powered</span>
        <span class="skill-chip">Smart Job Matching</span>
        <span class="skill-chip">Resume Intelligence</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":

    st.subheader("Welcome to your career intelligence dashboard")

    st.write(
        "Upload your resume and let our AI/ML system "
        "analyze your skills and discover relevant job opportunities."
    )

    col1, col2, col3 = st.columns(3)

    cards = [
        ("📄", "Resume Analysis", "Extract useful resume information"),
        ("🧠", "AI Skill Detection", "Discover technical skills"),
        ("💼", "Job Matching", "Compare your resume with job roles")
    ]

    for col, card in zip([col1, col2, col3], cards):

        with col:
            st.markdown(f"""
            <div class="glass-card">
                <div style="font-size:35px;">{card[0]}</div>
                <h3>{card[1]}</h3>
                <p style="color:#bdc7e9;">{card[2]}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("How it works")

    st.info(
        "Upload Resume → Extract Skills → ML Job Matching "
        "→ Career Recommendations"
    )


# ==========================================
# ANALYZE RESUME PAGE
# ==========================================

elif page == "Analyze Resume":

    st.subheader("📤 Upload and Analyze Your Resume")

    uploaded_file = st.file_uploader(
        "Choose your resume",
        type=["pdf", "docx"],
        help="Upload a text-based PDF or DOCX resume."
    )

    if uploaded_file is not None:

        st.success(f"Uploaded successfully: {uploaded_file.name}")

        if st.button("✨ Analyze My Resume", use_container_width=True):

            with st.spinner("AI is analyzing your resume..."):

                resume_text = extract_resume_text(uploaded_file)

                if (
                    not resume_text
                    or resume_text.startswith("Error")
                    or resume_text.startswith("Unsupported")
                ):
                    st.error("Unable to read the uploaded resume.")

                elif not resume_text.strip():
                    st.error("No readable text found in the resume.")

                else:

                    skills = extract_skills(resume_text)

                    total_skills = count_total_skills(skills)

                    results = match_jobs(resume_text)

                    recommendations = recommend_jobs(
                        results,
                        top_n=3
                    )

                    st.session_state["resume_text"] = resume_text
                    st.session_state["skills"] = skills
                    st.session_state["total_skills"] = total_skills
                    st.session_state["results"] = results
                    st.session_state["recommendations"] = recommendations

                    st.success("Resume analysis completed successfully!")

    # ======================================
    # DISPLAY ANALYSIS RESULTS
    # ======================================

    if "results" in st.session_state:

        skills = st.session_state["skills"]
        results = st.session_state["results"]
        recommendations = st.session_state["recommendations"]
        total_skills = st.session_state["total_skills"]

        st.markdown("---")

        st.subheader("📊 Your Resume Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Skills Identified</div>
                <div class="metric-value">{total_skills}</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Job Roles Compared</div>
                <div class="metric-value">{len(results)}</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Top Matching Role</div>
                <div class="metric-value" style="font-size:21px;">
                    {results[0]["job_title"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Results tabs

        tab1, tab2, tab3, tab4 = st.tabs([
            "🧠 Extracted Skills",
            "📈 Job Matching",
            "💼 Recommendations",
            "📥 Download Report"
        ])

        # ==================================
        # SKILLS TAB
        # ==================================

        with tab1:

            st.subheader("Your Technical Skills")

            if skills:

                for category, skill_list in skills.items():

                    st.markdown(f"**{category}**")

                    chips = "".join(
                        f'<span class="skill-chip">{skill}</span>'
                        for skill in skill_list
                    )

                    st.markdown(
                        chips,
                        unsafe_allow_html=True
                    )

                    st.markdown("")

            else:
                st.warning("No matching skills were identified.")

        # ==================================
        # JOB MATCHING TAB
        # ==================================

        with tab2:

            st.subheader("Job Compatibility Analysis")

            chart_data = pd.DataFrame(results)

            chart_data = chart_data.set_index("job_title")

            st.bar_chart(
                chart_data[["match_score"]],
                horizontal=True
            )

            for job in results:

                st.markdown(
                    f"**{job['job_title']} — {job['match_score']}%**"
                )

                st.progress(
                    min(job["match_score"] / 100, 1.0)
                )

            st.caption(
                "Scores represent text similarity, not hiring probability."
            )

        # ==================================
        # RECOMMENDATIONS TAB
        # ==================================

        with tab3:

            st.subheader("Recommended Career Opportunities")

            for index, job in enumerate(recommendations, start=1):

                st.markdown(f"""
                <div class="glass-card">
                    <h3>#{index} {job['job_title']}</h3>
                    <h2 style="color:#70e7ba;">
                        {job['match_score']}% Similarity
                    </h2>
                    <p style="color:#cbd3f0;">
                        {job['suitability']}
                    </p>
                </div>
                """, unsafe_allow_html=True)

                st.info(
                    get_recommendation_message(
                        job["match_score"]
                    )
                )

        # ==================================
        # DOWNLOAD TAB
        # ==================================

        with tab4:

            st.subheader("Download Your Analysis")

            report = pd.DataFrame(results)

            csv_data = report.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                "⬇ Download Job Matching Report",
                data=csv_data,
                file_name="AI_Resume_Analysis.csv",
                mime="text/csv",
                use_container_width=True
            )

            st.caption(
                "Your report contains job titles and text similarity scores."
            )

# ==========================================
# CUSTOM JOB DESCRIPTION MATCHING
# ==========================================

elif page == "Custom Job Match":

    st.subheader("🏢 Custom Company Job Matching")

    st.write(
        "Compare your resume with any company's job description "
        "and discover your matching skills and skill gaps."
    )

    st.markdown("---")

    company_name = st.text_input(
        "Company Name",
        placeholder="Example: TCS, Infosys, Cognizant"
    )

    job_title = st.text_input(
        "Job Title",
        placeholder="Example: Python Developer"
    )

    job_description = st.text_area(
        "Paste Company Job Description",
        placeholder=(
            "Paste the complete job description here...\n\n"
            "Required skills:\n"
            "Python, SQL, Django, Flask, Git..."
        ),
        height=220
    )

    st.info(
        "Upload the resume you want to compare against "
        "this company's job requirements."
    )

    jd_resume = st.file_uploader(
        "Upload Resume for Company Matching",
        type=["pdf", "docx"],
        key="custom_jd_resume"
    )

    if st.button(
        "🚀 Analyze Company Job Match",
        use_container_width=True
    ):

        if not company_name.strip():
            st.warning("Please enter the company name.")

        elif not job_title.strip():
            st.warning("Please enter the job title.")

        elif not job_description.strip():
            st.warning("Please paste the job description.")

        elif jd_resume is None:
            st.warning("Please upload your resume.")

        else:

            with st.spinner("Comparing resume with job requirements..."):

                resume_text = extract_resume_text(jd_resume)

                if (
                    not resume_text
                    or resume_text.startswith("Error")
                    or resume_text.startswith("Unsupported")
                ):
                    st.error("Unable to read the uploaded resume.")

                elif not resume_text.strip():

                    st.error("No readable text found in the resume.")

                else:

                    try:

                        result = analyze_custom_job(
                            resume_text,
                            job_description
                        )

                        st.session_state["custom_jd_result"] = result
                        st.session_state["custom_resume_text"] = resume_text
                        st.session_state["custom_job_description"] = job_description
                        st.session_state["custom_company"] = company_name
                        st.session_state["custom_title"] = job_title

                        st.success("Company job analysis completed!")

                    except ValueError as error:

                        st.error(str(error))

    # Display analysis report

    if "custom_jd_result" in st.session_state:

        result = st.session_state["custom_jd_result"]

        st.markdown("---")

        st.header("📊 Company Job Match Report")

        st.caption(
            f"{st.session_state['custom_company']} | "
            f"{st.session_state['custom_title']}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Overall Match",
                f"{result['overall_score']}%"
            )

        with col2:
            st.metric(
                "Text Similarity",
                f"{result['similarity_score']}%"
            )

        with col3:
            st.metric(
                "Skill Coverage",
                f"{result['skill_coverage']}%"
            )

        st.subheader("🎯 Application Alignment")

        st.progress(
            min(result["overall_score"] / 100, 1.0)
        )

        st.info(
            f"Assessment: {result['readiness']}"
        )

        st.write(result["guidance"])

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Matched Skills")

            if result["matched_skills"]:

                for skill in result["matched_skills"]:
                    st.success(skill)

            else:
                st.write("No matching skills identified.")

        with col2:

            st.subheader("📚 Missing Skills")

            if result["missing_skills"]:

                for skill in result["missing_skills"]:
                    st.warning(skill)

            else:
                st.success("All recognized required skills matched!")

        # Download company-specific report

        report = pd.DataFrame([
            {
                "Company": st.session_state["custom_company"],
                "Job Title": st.session_state["custom_title"],
                "Overall Match": result["overall_score"],
                "Text Similarity": result["similarity_score"],
                "Skill Coverage": result["skill_coverage"],
                "Readiness": result["readiness"],
                "Matched Skills": ", ".join(
                    result["matched_skills"]
                ),
                "Missing Skills": ", ".join(
                    result["missing_skills"]
                )
            }
        ])

        st.download_button(
            "⬇ Download Company Job Analysis",
            data=report.to_csv(index=False).encode("utf-8"),
            file_name="company_job_analysis.csv",
            mime="text/csv"
        )
        # SKILL GAP ANALYSIS AND LEARNING ROADMAP

        st.markdown("---")
        st.subheader("🎯 Skill Gap Analysis & Learning Roadmap")

        if st.button("Generate Learning Roadmap", use_container_width=True):

            gap_result = analyze_skill_gap(
                st.session_state["custom_resume_text"],
                st.session_state["custom_job_description"]
            )

            st.session_state["skill_gap_result"] = gap_result

       
        if "skill_gap_result" in st.session_state:

            gap_result = st.session_state["skill_gap_result"]

            st.write("### 📊 Skill Gap Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Required Skills", gap_result["total_required"])

            with col2:
                st.metric("Matched Skills", gap_result["total_matched"])

            st.write("### 📚 Your Personalized Learning Roadmap")

            if gap_result["learning_roadmap"]:

                for skill, topics in gap_result["learning_roadmap"].items():

                    with st.expander(f"📖 Learn {skill}"):

                        for number, topic in enumerate(topics, start=1):
                            st.write(f"{number}. {topic}")

            else:
                st.success("No missing skills were identified among the recognized skills.")


        st.caption(
            "This is an automated preliminary assessment. "
            "It does not verify experience, education, or "
            "all mandatory company requirements."
        )


# ==========================================
# ABOUT PAGE
# ==========================================

elif page == "About Project":

    st.subheader("About AI Resume Analyzer")

    st.markdown("""
    <div class="glass-card">
        <h2>🚀 Project Overview</h2>
        <p>
            AI Resume Analyzer is an intelligent resume analysis
            and job recommendation application developed using Python,
            Natural Language Processing and Machine Learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Technologies Used")

    technologies = [
        "Python",
        "Streamlit",
        "Scikit-learn",
        "TF-IDF",
        "Cosine Similarity",
        "Natural Language Processing",
        "Pandas",
        "PyPDF2",
        "Python-docx"
    ]

    cols = st.columns(3)

    for index, technology in enumerate(technologies):

        with cols[index % 3]:

            st.markdown(
                f'<div class="glass-card">{technology}</div>',
                unsafe_allow_html=True
            )

    st.markdown("---")

    st.caption(
        "AI Resume Analyzer | Resume Intelligence and Career Matching"
    )
