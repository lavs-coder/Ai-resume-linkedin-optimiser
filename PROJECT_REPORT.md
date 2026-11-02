# Project Report: AI Resume and LinkedIn Profile Optimiser

## 1. Abstract
The AI Resume and LinkedIn Profile Optimiser is a web-based prototype designed to help students and job seekers compare resume content with a target job description. It identifies skills from a predefined list, estimates overlap, highlights potential skill gaps, extracts frequent keywords, and drafts a LinkedIn headline and About section. The prototype uses Python and Streamlit and can run locally.

## 2. Problem Statement
Applicants often find it difficult to customise a resume and LinkedIn profile for a specific role. Important job-description terms may be overlooked, and profile summaries may be too general. A simple tool can provide an initial checklist and help users review their application materials.

## 3. Objectives
- Compare resume text with a target job description.
- Identify matching skills and possible missing skills.
- Extract useful keywords from the job description.
- Suggest a starting LinkedIn headline and summary.
- Provide a simple interface suitable for beginner users.

## 4. Proposed System
The user pastes resume text and a job description into the web app. The program converts text to lowercase, searches for skills in a predefined list, compares the detected sets, and calculates an approximate overlap percentage. It also counts frequently occurring words and uses the results to generate editable LinkedIn text suggestions.

## 5. Technology Used
- **Language:** Python
- **User interface:** Streamlit
- **Text processing:** Regular expressions
- **Data handling:** Python sets and Counter

## 6. Modules
1. **Input Module:** Accepts resume, job description, and optional LinkedIn text.
2. **Skill Detection Module:** Detects common skills from the predefined vocabulary.
3. **Comparison Module:** Finds matched and missing detected skills.
4. **Keyword Module:** Extracts frequent words from the job description.
5. **Profile Suggestion Module:** Creates editable headline and About-section drafts.
6. **Guidance Module:** Displays a checklist for improving resume quality.

## 7. Algorithm
1. Read resume and job-description text.
2. Check that both required inputs are present.
3. Convert text to lowercase.
4. Detect skills from the built-in skill list.
5. Find the intersection and difference between detected skill sets.
6. Calculate the approximate match percentage as matched detected skills divided by detected job skills, multiplied by 100.
7. Extract frequent job-description words.
8. Generate draft LinkedIn text and display the results.

## 8. Expected Output
The application displays an approximate skill-match percentage, matched skills, potential gaps, job-description keywords, a suggested LinkedIn headline, an editable About-section draft, and a quality checklist.

## 9. Limitations
The current version uses a predefined skill list and simple keyword frequency. It may miss synonyms, context, and skills written in different forms. The percentage is not a prediction of hiring success. The app does not verify user claims, parse uploaded PDF files, call an external AI model, or modify LinkedIn profiles.

## 10. Future Scope
- Add PDF and DOCX text extraction.
- Expand and customise the skill vocabulary.
- Add semantic similarity or an optional language-model API.
- Export results as a downloadable report.
- Add automated tests and multilingual support.

## 11. Conclusion
The prototype demonstrates how basic text processing can help applicants review the relevance of their resume to a target role. It offers transparent, editable suggestions while leaving final decisions and factual accuracy to the user.
