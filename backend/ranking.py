job_skills = {
    "Web Developer": ["html","css","javascript"],
    "AI Engineer": ["python","machine learning","ai"],
    "Data Analyst": ["sql","excel","python"]
}

def rank(text):
    result = {}
    for job, skills in job_skills.items():
        score = sum(1 for s in skills if s in text) * 20
        result[job] = score
    return result
