
import PyPDF2
import docx
import os


def extract_text_from_pdf(file):
    """Extract text from a PDF resume."""

    text = ""

    try:
        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def extract_text_from_docx(file):
    """Extract text from a Word resume."""

    text = ""

    try:
        document = docx.Document(file)

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    except Exception as e:
        return f"Error reading DOCX: {str(e)}"


def extract_resume_text(file):
    """Identify file type and extract resume text."""

    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif filename.endswith(".docx"):
        return extract_text_from_docx(file)

    else:
        return "Unsupported file format. Upload PDF or DOCX."
