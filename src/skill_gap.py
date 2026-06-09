def analyze_skill_gap(user_skills, required_skills):

    matched = []

    missing = []

    for skill in required_skills:

        if skill in user_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    if len(required_skills) == 0:
        readiness = 0

    else:
        readiness = (
            len(matched) /
            len(required_skills)
        ) * 100

    return readiness, matched, missing