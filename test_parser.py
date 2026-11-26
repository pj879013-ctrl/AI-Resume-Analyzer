
from modules.resume_parser import extract_resume_text

file_path = "sample_resumes/sample_resume.pdf"

with open(file_path, "rb") as file:
    resume_text = extract_resume_text(file)

print("RESUME TEXT:")
print(resume_text)
