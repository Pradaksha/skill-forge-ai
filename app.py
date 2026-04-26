import streamlit as st
import re

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Skill Forge", layout="centered")

# Center entire app
st.markdown("""
<style>
.block-container {
    max-width: 700px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<h1 style='text-align: center;'>Skill Forge</h1>
<p style='text-align: center;'>AI-powered skill gap analysis & learning recommendations</p>
""", unsafe_allow_html=True)

st.info("""
1. Paste or upload a resume  
2. Enter a job description  
3. Click Analyze Candidate  
4. View skill gaps and learning roadmap  
""")

# -------------------------------
# INPUT MODE
# -------------------------------
mode = st.radio("Choose Resume Input Method", ["Paste Resume", "Upload Resume"])

job_desc = st.text_area("Job Description")

resume_text = ""

# -------------------------------
# TEXT EXTRACTION (TXT ONLY)
# -------------------------------
def extract_text(file):
    text = ""

    if file.type == "text/plain":
        try:
            text = file.read().decode("utf-8")
        except:
            st.error("Failed to read TXT file.")
            return ""
    else:
        st.error("Only TXT files are supported.")
        return ""

    return text


# -------------------------------
# HANDLE INPUT
# -------------------------------
if mode == "Paste Resume":
    resume_text = st.text_area("Resume")

else:
    uploaded_file = st.file_uploader("Upload Resume (TXT only)", type=["txt"])
    if uploaded_file:
        resume_text = extract_text(uploaded_file)

# -------------------------------
# SKILL LIST
# -------------------------------
skills_list = [
    "python", "sql", "excel", "machine learning",
    "data analysis", "pandas", "numpy", "java"
]

# -------------------------------
# ANALYSIS
# -------------------------------
if st.button("Analyze Candidate"):
    if not job_desc or not resume_text:
        st.warning("Please provide both job description and resume.")
    else:
        job_skills = [skill for skill in skills_list if skill in job_desc.lower()]
        resume_skills = [skill for skill in skills_list if skill in resume_text.lower()]

        matched = list(set(job_skills) & set(resume_skills))
        missing = list(set(job_skills) - set(resume_skills))

        score = int((len(matched) / len(job_skills)) * 100) if job_skills else 0

        # -------------------------------
        # DISPLAY RESULTS
        # -------------------------------
        st.markdown("## Analysis Result")

        st.markdown("### Required Skills")
        for skill in job_skills:
            st.write(f"- {skill}")

        st.markdown("### Candidate Skills")
        for skill in resume_skills:
            st.write(f"- {skill}")

        st.markdown("### Missing Skills")
        if missing:
            for skill in missing:
                st.write(f"- {skill}")
        else:
            st.success("No missing skills")

        # -------------------------------
        # MATCH SCORE
        # -------------------------------
        st.markdown("### Match Score")
        st.progress(score / 100)
        st.write(f"Score: {score}%")

        # -------------------------------
        # LEARNING ROADMAP
        # -------------------------------
        if missing:
            st.markdown("## Learning Roadmap")

            for skill in missing:
                st.markdown(f"### {skill.upper()}")

                if skill == "python":
                    st.write("- Practice Python basics and projects")
                    st.write("- Learn libraries like Pandas and NumPy")

                elif skill == "sql":
                    st.write("- Learn SELECT, JOIN, GROUP BY")
                    st.write("- Practice SQL queries")

                elif skill == "excel":
                    st.write("- Learn formulas and pivot tables")
                    st.write("- Practice dashboards")

                elif skill == "java":
                    st.write("- Learn OOP concepts")
                    st.write("- Practice coding problems")

                elif skill == "machine learning":
                    st.write("- Learn ML algorithms")
                    st.write("- Build ML projects")

                else:
                    st.write(f"- Start learning {skill}")