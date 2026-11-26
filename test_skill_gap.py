
from modules.skill_gap import analyze_skill_gap

resume_text = """
I know Python, Java, SQL, HTML and CSS.
I have basic programming knowledge.
"""

job_description = """
We are looking for a Python Developer.
Required skills: Python, SQL, Django, Flask, Git and GitHub.
"""

result = analyze_skill_gap(resume_text, job_description)

print("\n========== SKILL GAP ANALYSIS ==========")

print("\nMatched Skills:")
print(result["matched_skills"])

print("\nMissing Skills:")
print(result["missing_skills"])

print("\nLearning Roadmap:")
for skill, topics in result["learning_roadmap"].items():
    print(f"\n{skill}:")
    for topic in topics:
        print("-", topic)

print("\nTotal Required:", result["total_required"])
print("Total Matched:", result["total_matched"])
