
# AI Resume Analyzer & Job Recommendation System

An AI-powered web application that analyzes resumes, extracts skills, matches candidates with job roles, and identifies skill gaps using Python, NLP, and Machine Learning.

## Live Demo

[Open AI Resume Analyzer](https://ai-resume-analyzer-ymsoeznywgagyppjrgvndb.streamlit.app)

## GitHub Repository

https://github.com/pj879013-ctrl/AI-Resume-Analyzer

## Features

- Resume Upload: Supports PDF and DOCX files.
- Resume Parsing: Extracts text from uploaded resumes.
- Skill Extraction: Identifies technical skills and categorizes them.
- Job Matching: Recommends suitable job roles.
- Custom Job Matching: Compares resumes with company-specific job descriptions.
- Skill Gap Analysis: Identifies missing skills.
- Learning Roadmap: Suggests topics to develop missing skills.
- Report Download: Downloads company job analysis as CSV.

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NLP
- TF-IDF
- Cosine Similarity
- PyPDF2
- python-docx

## Project Structure

```text
AI-Resume-Analyzer/
│
├── modules/
│   ├── resume_parser.py
│   ├── text_processor.py
│   ├── skill_extractor.py
│   ├── job_matcher.py
│   ├── recommendation.py
│   ├── custom_jd_matcher.py
│   └── skill_gap.py
│
├── sample_resumes/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/pj879013-ctrl/AI-Resume-Analyzer.git
```

2. Open the project folder:

```bash
cd AI-Resume-Analyzer
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate it on Windows:

```powershell
.venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
streamlit run app.py
```

## Disclaimer

This application provides preliminary resume and skill matching based on text similarity and a predefined skills dictionary. It does not guarantee job eligibility or hiring outcomes.

## Developed With

Python | Machine Learning | NLP | Streamlit
