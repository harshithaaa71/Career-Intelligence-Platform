def recommend_careers(user_skills):

    careers = {

        "Data Analyst": [
            "Python",
            "SQL",
            "Excel",
            "Power BI",
            "Statistics"
        ],

        "Business Analyst": [
            "Excel",
            "SQL",
            "Communication",
            "Reporting",
            "Business Analysis"
        ],

        "Data Scientist": [
            "Python",
            "Machine Learning",
            "Statistics",
            "Pandas",
            "NumPy"
        ],

        "Machine Learning Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "Git"
        ]
    }

    results = []

    for career, skills in careers.items():

        matches = len(
            set(user_skills).intersection(skills)
        )

        score = (
            matches / len(skills)
        ) * 100

        results.append(
            (career, score)
        )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results[:3]