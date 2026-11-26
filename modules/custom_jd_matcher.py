
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from modules.skill_extractor import extract_skills


def flatten_skills(skill_dictionary):
    """Convert categorized skills into a simple list."""

    skills = []

    for category_skills in skill_dictionary.values():
        skills.extend(category_skills)

    return skills


def analyze_custom_job(resume_text, job_description):
    """
    Compare a resume with a custom company job description.
    """

    if not resume_text or not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not job_description or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    # --------------------------------
    # 1. Calculate TF-IDF similarity
    # --------------------------------

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    similarity_score = round(
        float(similarity) * 100, 2
    )

    # --------------------------------
    # 2. Extract resume skills
    # --------------------------------

    resume_skills = extract_skills(resume_text)

    candidate_skills = flatten_skills(
        resume_skills
    )

    # --------------------------------
    # 3. Extract job description skills
    # --------------------------------

    jd_skills = extract_skills(job_description)

    required_skills = flatten_skills(
        jd_skills
    )

    candidate_set = {
        skill.lower() for skill in candidate_skills
    }

    required_set = {
        skill.lower() for skill in required_skills
    }

    # --------------------------------
    # 4. Compare skills
    # --------------------------------

    matched_skills = [
        skill for skill in required_skills
        if skill.lower() in candidate_set
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in candidate_set
    ]

    # --------------------------------
    # 5. Calculate skill coverage
    # --------------------------------

    if required_skills:

        skill_coverage = round(
            len(matched_skills) /
            len(required_skills) * 100,
            2
        )

        # Combined heuristic score
        overall_score = round(
            (similarity_score * 0.5) +
            (skill_coverage * 0.5),
            2
        )

    else:

        skill_coverage = 0

        # Do not invent a skill match when
        # no recognized skills exist in the JD.
        overall_score = similarity_score

    # --------------------------------
    # 6. Generate application guidance
    # --------------------------------

    if overall_score >= 70:

        readiness = "Strong Alignment"

        guidance = (
            "Your resume shows strong alignment "
            "with this job description. Review "
            "the remaining requirements before applying."
        )

    elif overall_score >= 40:

        readiness = "Partial Alignment"

        guidance = (
            "Your resume matches some requirements. "
            "Consider addressing the missing skills "
            "and improving relevant project descriptions."
        )

    else:

        readiness = "Needs Improvement"

        guidance = (
            "Your resume currently shows limited alignment. "
            "Review the job requirements and identify "
            "relevant skills and experience to develop."
        )

    return {

        "similarity_score": similarity_score,

        "skill_coverage": skill_coverage,

        "overall_score": overall_score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "required_skills": required_skills,

        "readiness": readiness,

        "guidance": guidance

    }
