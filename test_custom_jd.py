
from modules.resume_parser import extract_resume_text

from modules.custom_jd_matcher import (
    analyze_custom_job
)


# --------------------------------
# 1. Read sample resume
# --------------------------------

file_path = "sample_resumes/sample_resume.pdf"

with open(file_path, "rb") as file:

    resume_text = extract_resume_text(file)


# --------------------------------
# 2. Sample company job description
# --------------------------------

company_name = "ABC Technologies"

job_title = "Python Developer"


job_description = """
We are looking for a Python Developer.

Required Skills:

Python programming
Java programming
SQL database management
Django framework
Flask framework
Git and GitHub
REST API development

Candidates should have knowledge of
software development and problem solving.

Freshers with relevant projects can apply.
"""


# --------------------------------
# 3. Analyze resume against JD
# --------------------------------

result = analyze_custom_job(
    resume_text,
    job_description
)


# --------------------------------
# 4. Display results
# --------------------------------

print("\n========================================")
print("       CUSTOM COMPANY JOB ANALYSIS")
print("========================================")

print("\nCompany:", company_name)

print("Job Title:", job_title)

print("\nOverall Match Score:",
      result["overall_score"], "%")

print("Text Similarity:",
      result["similarity_score"], "%")

print("Skill Coverage:",
      result["skill_coverage"], "%")


print("\nMATCHED SKILLS:")

for skill in result["matched_skills"]:
    print("+", skill)


print("\nMISSING SKILLS:")

for skill in result["missing_skills"]:
    print("-", skill)


print("\nAPPLICATION READINESS:")

print(result["readiness"])

print("\nSUGGESTIONS:")

print(result["guidance"])

print("\n========================================")
