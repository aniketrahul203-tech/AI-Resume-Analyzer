import streamlit as st
from PyPDF2 import PdfReader
import re

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("🤖 AI Resume Analyzer")
st.markdown("### 📄 Upload Resume & Compare with Job Description")

# -----------------------------
# Stopwords
# -----------------------------
STOPWORDS = {
    "the","is","and","in","to","of","for","on","with","a","an","by","at","from",
    "this","that","it","as","are","was","be"
}

# -----------------------------
# Skills List
# -----------------------------
SKILLS = [
    "python","java","c++","sql","machine learning","data analysis",
    "excel","powerbi","tableau","html","css","javascript","react",
    "node","django","flask","mongodb","mysql"
]

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader("📂 Upload Resume (PDF)", type=["pdf"])

# Job Description
jd = st.text_area("📝 Paste Job Description")

# -----------------------------
# Extract Text
# -----------------------------
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_file and jd:

    resume_text = extract_text(uploaded_file).lower()
    jd_text = jd.lower()

    # Clean words using regex
    resume_words = set(re.findall(r'\b\w+\b', resume_text))
    jd_words = set(re.findall(r'\b\w+\b', jd_text))

    # Remove stopwords
    resume_words = {w for w in resume_words if w not in STOPWORDS}
    jd_words = {w for w in jd_words if w not in STOPWORDS}

    # Match Score
    match_score = len(resume_words & jd_words) / len(jd_words) * 100

    # -----------------------------
    # Display Score
    # -----------------------------
    st.subheader(f"🎯 Match Score: {match_score:.2f}%")
    st.progress(int(match_score))

    # Match Quality
    if match_score > 70:
        st.success("🔥 Strong Match")
    elif match_score > 40:
        st.warning("⚠️ Medium Match")
    else:
        st.error("❌ Low Match")

    # -----------------------------
    # Skills Detection
    # -----------------------------
    found_skills = [skill for skill in SKILLS if skill in resume_text]
    missing_skills = [skill for skill in SKILLS if skill in jd_text and skill not in resume_text]

    st.write("### ✅ Skills Found:")
    st.write(found_skills if found_skills else "No major skills detected")

    st.write("### ❌ Missing Skills:")
    st.write(missing_skills if missing_skills else "No missing skills 🎉")

    # -----------------------------
    # Suggestions (🔥 important)
    # -----------------------------
    if missing_skills:
        st.write("### 💡 Suggestions:")
        for skill in missing_skills[:5]:
            st.write(f"- Try adding **{skill}** to your resume")

    # -----------------------------
    # Missing Keywords
    # -----------------------------
    missing_keywords = jd_words - resume_words
    st.write("### 📌 Missing Keywords:")
    st.write(", ".join(list(missing_keywords)[:15]))

    # -----------------------------
    # Score Interpretation
    # -----------------------------
    st.write("### 📊 Analysis:")
    if match_score > 70:
        st.write("You are a strong candidate for this role.")
    elif match_score > 40:
        st.write("You meet some requirements, but can improve.")
    else:
        st.write("You need to improve your resume for this job.")
