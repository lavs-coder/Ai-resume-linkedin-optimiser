import re
import streamlit as st
from collections import Counter

st.set_page_config(page_title="AI Resume & LinkedIn Optimiser", page_icon="🧑‍💻", layout="wide")

SKILLS = [
    "python", "java", "c++", "c", "sql", "excel", "power bi", "tableau",
    "machine learning", "data analysis", "data analytics", "html", "css",
    "javascript", "react", "communication", "teamwork", "leadership",
    "project management", "problem solving", "critical thinking", "cloud",
    "aws", "azure", "git", "github", "pandas", "numpy", "statistics",
    "deep learning", "artificial intelligence", "ai", "cybersecurity",
    "networking", "ui/ux", "figma", "testing", "agile"
]

STOPWORDS = {
    "the", "and", "for", "with", "from", "this", "that", "you", "your",
    "are", "was", "were", "will", "have", "has", "had", "our", "their",
    "they", "them", "into", "about", "using", "use", "work", "working",
    "job", "role", "team", "skills", "ability", "experience", "required",
    "preferred", "candidate", "responsibilities", "responsibility"
}

def clean_words(text):
    return re.findall(r"[a-zA-Z][a-zA-Z+#./-]*", text.lower())

def find_skills(text):
    lower = text.lower()
    found = []
    for skill in SKILLS:
        if skill in lower:
            found.append(skill)
    return sorted(set(found))

def important_keywords(text, limit=12):
    words = [w for w in clean_words(text) if len(w) > 3 and w not in STOPWORDS]
    counts = Counter(words)
    return [word for word, _ in counts.most_common(limit)]

st.title("🧑‍💻 AI Resume & LinkedIn Profile Optimiser")
st.write("A beginner-friendly prototype that compares resume text with a job description and suggests profile improvements.")
st.info("Privacy note: This demo analyses text entered in this page. It does not upload your resume to an external AI service.")

with st.sidebar:
    st.header("How to use")
    st.markdown("1. Paste your resume text.\n2. Paste the target job description.\n3. Add your current LinkedIn headline and summary (optional).\n4. Select **Optimise my profile**.")
    st.caption("Prototype note: suggestions are rule-based and should be reviewed for accuracy.")

left, right = st.columns(2)
with left:
    resume = st.text_area("Resume text", height=260, placeholder="Paste the text from your resume here...")
with right:
    job = st.text_area("Target job description", height=260, placeholder="Paste the job description here...")

headline = st.text_input("Current LinkedIn headline (optional)", placeholder="e.g., B.Tech IT Student | Python | Data Analytics")
summary = st.text_area("Current LinkedIn About/Summary (optional)", height=120, placeholder="Paste your current LinkedIn summary...")

if st.button("✨ Optimise my profile", type="primary", use_container_width=True):
    if not resume.strip() or not job.strip():
        st.warning("Please enter both resume text and job description.")
    else:
        resume_skills = set(find_skills(resume))
        job_skills = set(find_skills(job))
        matched = sorted(resume_skills & job_skills)
        missing = sorted(job_skills - resume_skills)
        keywords = important_keywords(job)
        score = round((len(matched) / len(job_skills)) * 100) if job_skills else 0

        st.subheader("📊 Resume–Job Match")
        c1, c2, c3 = st.columns(3)
        c1.metric("Skill match estimate", f"{score}%")
        c2.metric("Matched skills", len(matched))
        c3.metric("Potential gaps", len(missing))
        st.progress(score / 100)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### ✅ Skills found in both")
            st.write(", ".join(matched) if matched else "No listed skills matched. Try checking the wording.")
        with col2:
            st.markdown("#### 🔎 Job skills not found in resume")
            st.write(", ".join(missing) if missing else "No gaps found among the built-in skill list.")
            if missing:
                st.caption("Only add a skill if you genuinely have it; otherwise consider learning it.")

        st.markdown("#### 🗝️ Suggested job-description keywords")
        st.write(", ".join(keywords) if keywords else "No keywords found.")

        st.subheader("💼 LinkedIn headline suggestion")
        top_skills = matched[:3] if matched else sorted(resume_skills)[:3]
        focus = " | ".join(s.title() for s in top_skills)
        suggested_headline = f"Student / Early-Career Candidate | {focus}" if focus else "Student / Early-Career Candidate | Add your genuine key skills"
        st.code(suggested_headline, language=None)

        st.subheader("✍️ LinkedIn About section draft")
        first_sentence = "I am a student / early-career professional interested in building practical skills and contributing to meaningful projects."
        skill_sentence = f"My current focus areas include {', '.join(s.title() for s in top_skills)}." if top_skills else "My current focus is developing role-relevant technical and professional skills."
        keyword_sentence = f"I am particularly interested in opportunities involving {', '.join(keywords[:5])}." if keywords else "I am interested in learning and applying skills relevant to my target role."
        about = f"{first_sentence}\n\n{skill_sentence} {keyword_sentence}\n\nI value continuous learning, collaboration, and solving problems through practical projects. I am looking forward to connecting with professionals and exploring opportunities where I can learn and contribute."
        st.text_area("Copy and edit this draft before using it", value=about, height=180)

        st.subheader("📝 Improvement checklist")
        checklist = [
            "Use clear action verbs and measurable results where truthful.",
            "Tailor project descriptions to the target role.",
            "Add relevant keywords naturally; do not keyword-stuff.",
            "Check spelling, dates, links, and consistent formatting.",
            "Never claim skills, certificates, or achievements you do not have."
        ]
        for item in checklist:
            st.markdown(f"- {item}")

st.divider()
st.caption("This tool gives an approximate, rule-based match score. It is not a hiring decision, does not verify qualifications, and does not connect to LinkedIn.")
