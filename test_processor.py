
from modules.resume_parser import extract_resume_text
from modules.text_processor import preprocess_resume

file_path = "sample_resumes/sample_resume.pdf"

with open(file_path, "rb") as file:
    resume_text = extract_resume_text(file)

result = preprocess_resume(resume_text)

print("\nORIGINAL RESUME TEXT:")
print(resume_text)

print("\nCLEANED RESUME TEXT:")
print(result["cleaned_text"])

print("\nTOKENS:")
print(result["tokens"])

print("\nFILTERED TOKENS:")
print(result["filtered_tokens"])
