
from modules.resume_parser import extract_resume_text
from modules.job_matcher import match_jobs


# Sample resume location
file_path = "sample_resumes/sample_resume.pdf"

# Extract resume text
with open(file_path, "rb") as file:
    resume_text = extract_resume_text(file)

# Compare resume with jobs
results = match_jobs(resume_text)

print("\n========== AI JOB MATCHING RESULTS ==========")

for job in results:

    print("\nJob Role:", job["job_title"])

    print("Match Score:", job["match_score"], "%")

print("\n=============================================")
