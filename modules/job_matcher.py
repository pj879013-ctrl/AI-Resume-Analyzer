
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Sample job descriptions
JOB_DATABASE = {

    "Python Developer": """
    Python programming Java SQL
    software development Django Flask
    API development debugging
    object oriented programming
    database management Git
    """,

    "Data Analyst": """
    Python SQL Excel
    data analysis data visualization
    statistics Pandas NumPy
    Power BI Tableau
    data cleaning reporting
    """,

    "Machine Learning Engineer": """
    Python Machine Learning
    Deep Learning Artificial Intelligence
    Scikit-learn TensorFlow PyTorch
    Pandas NumPy data science
    model training NLP
    """,

    "Web Developer": """
    HTML CSS JavaScript
    React Angular Node.js
    website development frontend
    backend development database
    responsive web design
    """

}


def match_jobs(resume_text):
    """Compare resume with job descriptions."""

    if not resume_text or not resume_text.strip():
        return []

    job_titles = list(JOB_DATABASE.keys())

    job_descriptions = list(JOB_DATABASE.values())

    # Combine resume and job descriptions
    documents = [resume_text] + job_descriptions

    # Convert text into numerical vectors
    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )[0]

    results = []

    for title, score in zip(job_titles, similarity_scores):

        results.append({
            "job_title": title,
            "match_score": round(float(score) * 100, 2)
        })

    # Sort jobs by highest matching score
    results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return results
