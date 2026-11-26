
from modules.skill_extractor import extract_skills


# Learning suggestions for commonly missing skills
SKILL_LEARNING_PATHS = {
    "Python": [
        "Python basics and syntax",
        "Functions and OOP",
        "File handling and libraries"
    ],
    "SQL": [
        "SQL fundamentals",
        "Joins and subqueries",
        "Database management"
    ],
    "Machine Learning": [
        "Machine learning fundamentals",
        "Supervised and unsupervised learning",
        "Model training and evaluation"
    ],
    "Pandas": [
        "DataFrames and Series",
        "Data cleaning",
        "Data analysis"
    ],
    "NumPy": [
        "NumPy arrays",
        "Array operations",
        "Numerical computing"
    ],
    "Django": [
        "Django fundamentals",
        "Models and views",
        "Building web applications"
    ],
    "Flask": [
        "Flask basics",
        "Routes and templates",
        "Building APIs"
    ],
    "Git": [
        "Git basics",
        "Commits and branches",
        "Version control workflows"
    ],
    "GitHub": [
        "Creating repositories",
        "Pushing projects",
        "Managing project documentation"
    ],
    "HTML": [
        "HTML structure",
        "Forms and tables",
        "Semantic HTML"
    ],
    "CSS": [
        "CSS selectors",
        "Flexbox and Grid",
        "Responsive web design"
    ],
    "Java": [
        "Java fundamentals",
        "Object-oriented programming",
        "Collections and exception handling"
    ]
}


def analyze_skill_gap(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    candidate_set = {
        skill.lower()
        for skills in resume_skills.values()
        for skill in skills
    }

    required_list = list(dict.fromkeys(
        skill
        for skills in required_skills.values()
        for skill in skills
    ))

    matched_skills = [
        skill for skill in required_list
        if skill.lower() in candidate_set
    ]

    missing_skills = [
        skill for skill in required_list
        if skill.lower() not in candidate_set
    ]

    learning_roadmap = {}

    for skill in missing_skills:
        learning_roadmap[skill] = SKILL_LEARNING_PATHS.get(
            skill,
            [
                f"Learn the fundamentals of {skill}",
                f"Practice {skill} with examples",
                f"Build a small project using {skill}"
            ]
        )

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "learning_roadmap": learning_roadmap,
        "total_required": len(required_list),
        "total_matched": len(matched_skills)
    }
