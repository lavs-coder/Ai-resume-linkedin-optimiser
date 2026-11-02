# AI Resume and LinkedIn Profile Optimiser

## Project overview
A beginner-friendly web app that helps a student or job seeker tailor resume content and LinkedIn profile text to a target job description.

## Features
- Compares resume text with a pasted job description.
- Estimates overlap among a built-in list of common skills.
- Lists skills present in the job description but not detected in the resume.
- Extracts frequently repeated keywords from the job description.
- Suggests a LinkedIn headline and a starter About section.
- Provides a resume improvement checklist.

## Technology stack
- Python
- Streamlit
- Regular expressions and Python collections

## Important limitation
This is a rule-based prototype, not a connected large-language-model service. The match percentage is an approximate skill-list overlap, not a real hiring score. It does not connect to or edit LinkedIn automatically. Users should only include skills and achievements that are true.

## Run locally
1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python -m streamlit run app.py
   ```
6. Open the local URL shown in the terminal (usually `http://localhost:8501`).

## GitHub upload
Create a public or private repository named `ai-resume-linkedin-optimiser`, then upload `app.py`, `requirements.txt`, and `README.md`.

## Suggested future enhancements
- PDF/DOCX resume text extraction.
- More comprehensive skill taxonomy.
- Optional AI API integration with user consent.
- Downloadable analysis report.
- Unit tests and accessibility improvements.
