
from modules.resume_parser import extract_resume_text
from modules.job_matcher import match_jobs
from modules.recommendation import (
    recommend_jobs,
    get_recommendation_message
)

# Read sample resume
file_path = "sample_resumes/sample_resume.pdf"

with open(file_path, "rb") as file:
    resume_text = extract_resume_text(file)

# Calculate job matching scores
results = match_jobs(resume_text)

# Generate recommendations
recommendations = recommend_jobs(results, top_n=3)

print("\n========== JOB RECOMMENDATIONS ==========")

for job in recommendations:

    print("\nJob Role:", job["job_title"])

    print("Match Score:", job["match_score"], "%")

    print("Suitability:", job["suitability"])

    print(
        "Suggestion:",
        get_recommendation_message(job["match_score"])
    )

print("\n=========================================")
