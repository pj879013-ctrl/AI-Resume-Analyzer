
from modules.resume_parser import extract_resume_text
from modules.skill_extractor import (
    extract_skills,
    count_total_skills
)

# Resume file location
file_path = "sample_resumes/sample_resume.pdf"

# Extract resume text
with open(file_path, "rb") as file:
    resume_text = extract_resume_text(file)

# Extract skills
skills = extract_skills(resume_text)

# Count skills
total_skills = count_total_skills(skills)

print("\n========== AI RESUME SKILL ANALYSIS ==========")

for category, skill_list in skills.items():

    print(f"\n{category}:")
    for skill in skill_list:
        print("-", skill)

print("\nTotal Skills Found:", total_skills)

print("\n==============================================")
