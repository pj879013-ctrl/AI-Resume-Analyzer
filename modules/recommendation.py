
def recommend_jobs(results, top_n=3):
    """
    Recommend the best matching job roles.
    """

    recommendations = []

    # Sort jobs by matching score
    sorted_results = sorted(
        results,
        key=lambda x: x["match_score"],
        reverse=True
    )

    # Select top matching jobs
    for job in sorted_results[:top_n]:

        score = job["match_score"]

        # Determine suitability level
        if score >= 50:
            suitability = "Strong Similarity"

        elif score >= 30:
            suitability = "Moderate Similarity"

        else:
            suitability = "Low Similarity"

        recommendations.append({

            "job_title": job["job_title"],

            "match_score": score,

            "suitability": suitability

        })

    return recommendations


def get_recommendation_message(score):
    """
    Generate suggestions based on matching score.
    """

    if score >= 50:
        return "Your resume has good keyword similarity with this role."

    elif score >= 30:
        return "Improve your resume by adding relevant skills and projects."

    else:
        return "Consider developing more relevant skills for this role."
