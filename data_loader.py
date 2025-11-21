# data_loader.py
import pandas as pd


def row_to_student_dict(row):
    return {
        "name": row["name"],
        "learning_language": row["learning_language"],
        "programming_focus": row["programming_focus"],
        "level": row["level"],
        "hobbies": [h.strip() for h in str(row["hobbies"]).split(",") if h.strip()],
    }


def row_to_tutor_dict(row):
    return {
        "name": row["name"],
        "expertise_languages": [l.strip() for l in str(row["expertise_languages"]).split(",") if l.strip()],
        "programming_specialty": row["programming_specialty"],
        "teaching_style": row["teaching_style"],
        "hobbies": [h.strip() for h in str(row["hobbies"]).split(",") if h.strip()],
    }


def load_students(path: str):
    """Load students from CSV and return as list of dicts."""
    df = pd.read_csv(path)
    return [row_to_student_dict(row) for _, row in df.iterrows()]


def load_tutors(path: str):
    """Load tutors from CSV and return as list of dicts."""
    df = pd.read_csv(path)
    return [row_to_tutor_dict(row) for _, row in df.iterrows()]