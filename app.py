import streamlit as st
import re

# -------------------------------
# PAGE CONFIG (CENTERED)
# -------------------------------
st.set_page_config(page_title="Skill Forge", layout="centered")

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>
.main {
    max-width: 800px;
    margin: auto;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
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

job_desc = st.text_area("📌 Job Description")
resume_text = ""

# -------------------------------
# FILE HANDLING (TXT ONLY)
# -------------------------------
def extract_text(file):
    text = ""

    if file.type == "text/plain":
        try:
            text = str(file.read(), "utf-8")
        except:
            st.error("⚠️ Failed to read TXT file.")
            return ""
    else:
        st.warning("⚠️ Only TXT files are supported in this version.")
        return ""

    return text.lower()

# -------------------------------
# INPUT SECTION
# -------------------------------
if mode == "Paste Resume":
    resume_text = st.text_area("📄 Resume")
else:
    uploaded_file = st.file_uploader(
        "📂 Upload Resume (TXT only)",
        type=["txt"]
    )
    if uploaded_file:
        resume_text = extract_text(uploaded_file)

# -------------------------------
# SKILL EXTRACTION
# -------------------------------
COMMON_SKILLS = [
    "python", "sql", "excel", "power bi", "tableau",
    "machine learning", "nlp", "deep learning",
    "tensorflow", "pytorch", "react", "javascript",
    "html", "css", "node", "aws", "docker", "kubernetes",
    "git", "java", "c", "c++", "node js"
]

def extract_skills(text):
    text = text.lower()
    found = set()

    for skill in COMMON_SKILLS:
        if skill in text:
            found.add(skill.title())

    return list(found)

# -------------------------------
# LEARNING PLAN
# -------------------------------
def generate_learning_plan(skill):
    s = skill.lower()

    if s in ["python", "java", "c++", "c"]:
        return {
            "category": "Programming",
            "learning": [
                "Learn syntax and core concepts",
                "Practice coding problems",
                "Build small applications"
            ],
            "resources": [
                ("YouTube", f"https://www.youtube.com/results?search_query={skill}+tutorial"),
                ("Practice", "https://leetcode.com")
            ],
            "time": "3–5 weeks"
        }

    elif s in ["machine learning", "nlp", "deep learning"]:
        return {
            "category": "AI & Data Science",
            "learning": [
                "Understand concepts",
                "Work on datasets",
                "Build ML models"
            ],
            "resources": [
                ("YouTube", f"https://www.youtube.com/results?search_query={skill}+tutorial"),
                ("Projects", "https://github.com/topics/machine-learning")
            ],
            "time": "6–10 weeks"
        }

    elif s in ["power bi", "tableau"]:
        return {
            "category": "Visualization Tool",
            "learning": [
                "Learn tool interface",
                "Create dashboards",
                "Analyze datasets"
            ],
            "resources": [
                ("YouTube", f"https://www.youtube.com/results?search_query={skill}+dashboard+tutorial")
            ],
            "time": "2–4 weeks"
        }

    else:
        return {
            "category": "General Skill",
            "learning": [
                "Understand fundamentals",
                "Explore use cases"
            ],
            "resources": [
                ("YouTube", f"https://www.youtube.com/results?search_query={skill}+tutorial")
            ],
            "time": "2–3 weeks"
        }

# -------------------------------
# BUTTON (CENTERED)
# -------------------------------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    analyze = st.button("🚀 Analyze Candidate")

# -------------------------------
# ANALYSIS
# -------------------------------
if analyze:

    jd_skills = extract_skills(job_desc)
    resume_skills = extract_skills(resume_text)

    jd_set = set(jd_skills)
    resume_set = set(resume_skills)

    matched = jd_set.intersection(resume_set)
    gaps = jd_set - resume_set

    score = int((len(matched) / max(len(jd_set), 1)) * 100)

    st.subheader("📊 Skill Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Required")
        for s in jd_set:
            st.success(s)

    with col2:
        st.markdown("### Candidate")
        for s in resume_set:
            st.info(s)

    with col3:
        st.markdown("### Gaps")
        if gaps:
            for s in gaps:
                st.error(s)
        else:
            st.success("No major gaps 🎉")

    st.markdown(f"## Match Score: {score}%")

    # ---------------------------
    # LEARNING PLAN
    # ---------------------------
    if gaps:
        st.markdown("## 📘 Personalized Learning Plan")

        for skill in gaps:
            plan = generate_learning_plan(skill)

            with st.expander(f"📌 {skill} Roadmap"):
                st.markdown(f"**Category:** {plan['category']}")

                st.markdown("### Learning Path")
                for step in plan["learning"]:
                    st.write(f"- {step}")

                st.markdown("### Resources")
                for name, link in plan["resources"]:
                    st.markdown(f"- [{name}]({link})")

                st.markdown(f"⏳ **Estimated Time:** {plan['time']}")