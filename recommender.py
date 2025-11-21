# recommender.py

def recommend_tutors(student, tutors, top_k=3):
    """
    student: dict with keys:
        - name
        - learning_language
        - programming_focus
        - level
        - hobbies (list)

    tutors: list of tutor dicts with keys:
        - name
        - expertise_languages (list)
        - programming_specialty
        - teaching_style
        - hobbies (list)

    returns: list of top_k tutor dicts
    """

    def score(student, tutor):
        total = 0

        # 1. Language match
        if student["learning_language"].lower() in [
            lang.lower() for lang in tutor["expertise_languages"]
        ]:
            total += 3

        # 2. Programming match
        if student["programming_focus"].lower() == tutor["programming_specialty"].lower():
            total += 2

        # 3. Level → teaching style match
        beginner_styles = {
            "structured",
            "visual",
            "interactive",
            "project-based",
            "hands-on",
        }
        intermediate_styles = {
            "interactive",
            "conversational",
            "project-based",
            "hands-on",
            "analytical",
            "visual",
            "structured",
        }
        advanced_styles = {"advanced-concepts", "analytical", "hands-on"}

        level = student["level"].lower()
        style = tutor["teaching_style"].lower()

        if (
            (level == "beginner" and style in beginner_styles)
            or (level == "intermediate" and style in intermediate_styles)
            or (level == "advanced" and style in advanced_styles)
        ):
            total += 1

        # 4. Hobby overlap
        s_hobbies = {h.lower() for h in student["hobbies"]}
        t_hobbies = {h.lower() for h in tutor["hobbies"]}
        overlap = s_hobbies & t_hobbies
        total += len(overlap)

        return total

    # Score all tutors
    scored = [(score(student, tutor), tutor) for tutor in tutors]

    # Sort by highest score first
    scored.sort(key=lambda x: x[0], reverse=True)

    # Return only tutor dicts
    return [tutor for _, tutor in scored[:top_k]]