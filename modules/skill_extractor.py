
import re


# Skill database organized by category
SKILL_DATABASE = {

    "Programming Languages": [
        "Python",
        "Java",
        "C",
        "C++",
        "C#",
        "JavaScript",
        "R",
        "PHP"
    ],

    "Web Development": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Angular",
        "Node.js",
        "Django",
        "Flask"
    ],

    "Database Management": [
        "SQL",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "Oracle"
    ],

    "Data Science": [
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "SciPy",
        "Data Analysis"
    ],

    "AI and Machine Learning": [
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "TensorFlow",
        "PyTorch",
        "Scikit-learn",
        "NLP",
        "Natural Language Processing"
    ],

    "Tools and Technologies": [
        "Git",
        "GitHub",
        "VS Code",
        "Jupyter Notebook",
        "Excel",
        "Power BI",
        "Tableau"
    ]
}


def extract_skills(resume_text):
    """Extract skills from resume text."""

    text = re.sub(r"\s+", " ", resume_text.lower())

    extracted_skills = {}

    for category, skills in SKILL_DATABASE.items():

        found_skills = []

        for skill in skills:

            pattern = (
                r"(?<![a-z0-9])"
                + re.escape(skill.lower())
                + r"(?![a-z0-9])"
            )

            if re.search(pattern, text):
                found_skills.append(skill)

        if found_skills:
            extracted_skills[category] = found_skills

    return extracted_skills


def count_total_skills(extracted_skills):
    """Count all extracted skills."""

    total = sum(
        len(skills)
        for skills in extracted_skills.values()
    )

    return total
