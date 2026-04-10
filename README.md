# 🤖 AI Resume Analyzer

An intelligent web application that analyzes resumes against job descriptions using Natural Language Processing (NLP) techniques.  
It helps users understand how well their resume matches a job role and provides actionable suggestions to improve it.

---

## 🚀 Features
- 📂 Upload PDF resume
- 🧾 Extract text using PyPDF2
- 🔍 Compare resume with job description
- 🎯 Calculate match score (%)
- 📊 Visual progress bar for score
- ✅ Detect relevant skills in resume
- ❌ Identify missing skills
- 💡 Provide suggestions for improvement
- 📌 Highlight missing keywords
- 🧠 Smart text cleaning using regex & stopwords

---

## 🛠️ Tech Stack
- **Python** – Core programming
- **Streamlit** – Web UI
- **PyPDF2** – PDF text extraction
- **NLP Techniques** – Regex, Stopword removal, Keyword matching

---

## 🧠 How It Works
1. User uploads a resume (PDF format)
2. Text is extracted from the resume using PyPDF2
3. Job description is input by the user
4. Both texts are cleaned using:
   - Lowercasing
   - Regex (removes punctuation)
   - Stopword filtering
5. Keywords are compared between resume and job description
6. Match score is calculated based on common words
7. Skills are detected from a predefined skills list
8. Missing skills and suggestions are displayed

---

## 📊 Output Example
- 🎯 Match Score: 65%
- ⚠️ Medium Match
- ✅ Skills Found: Python, SQL
- ❌ Missing Skills: Machine Learning, Power BI
- 💡 Suggestions: Add missing skills to improve your resume

---

## 📸 Screenshot
(Add your project screenshot here)

---

## ▶️ Run Locally

bash
git clone https://github.com/aniketrahul203-tech/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
pip install streamlit PyPDF2
streamlit run app.py


# User interface
<img width="753" height="926" alt="Screenshot 2026-04-10 at 6 47 27 PM" src="https://github.com/user-attachments/assets/b029d58d-2b80-4b95-ada5-e7b6c0095b60" />
<img width="351" height="317" alt="Screenshot 2026-04-10 at 6 47 34 PM" src="https://github.com/user-attachments/assets/c52d6078-2ba9-4bee-ad78-6636b230eca0" />




Author: - https://github.com/aniketrahul203-tech
