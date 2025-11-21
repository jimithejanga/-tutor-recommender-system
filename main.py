
import pandas as pd
from data_loader import load_students, load_tutors
from recommender import recommend_tutors

def main():
    # Load data
    students = load_students("studentscsv.csv")
    tutors = load_tutors("tutorscsv.csv")

    # List to store output rows
    output_rows = []

    for idx, student in enumerate(students, start=1):
        print(f"\n===== STUDENT {idx} ({student['name']}) =====")
        top_tutors = recommend_tutors(student, tutors, top_k=3)

        # Print to console
        for rank, tutor in enumerate(top_tutors, start=1):
            print(f"{rank}. {tutor['name']}")

        # Add row to results list
        output_rows.append({
            "student_name": student["name"],
            "rank_1": top_tutors[0]["name"] if len(top_tutors) > 0 else "",
            "rank_2": top_tutors[1]["name"] if len(top_tutors) > 1 else "",
            "rank_3": top_tutors[2]["name"] if len(top_tutors) > 2 else "",
        })

    # Convert results to a DataFrame
    df = pd.DataFrame(output_rows)

    # Write to CSV
    df.to_csv("recommendations.csv", index=False)
    print("\nSaved recommendations to recommendations.csv")

if __name__ == "__main__":
    main()