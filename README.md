Tutor Recommendation System

A simple rule-based recommendation engine that matches students to the best tutors based on:
	1	Language compatibility
	2	Programming subject match
	3	Teaching style fit
	4	Shared hobbies

The system reads student/tutor data from CSV files, processes them, applies the matching rules, and outputs the top 3 tutors per student — both in the console and in a recommendations.csv file.

tutor-recommender/
├─ data_loader.py        
├─ recommender.py        
├─ main.py              
├─ requirements.txt      
├─ README.md             
└─ studentscsv.csv       
└─ tutorscsv.csv 


How It Works

The system matches students to tutors using four rules:
1.	Language Match
Tutor speaks the student’s learning language → strong match
2.	Programming Match
Tutor teaches the student’s programming focus → strong match
3.	Teaching Style Fit
Beginner / intermediate / advanced levels influence tutor suitability
4.	Hobby Overlap
More shared hobbies = better personal compatibility

Each match contributes points to a score, and the highest scoring tutors are recommended.

This makes it a rule-based, content-based recommender system.

Install dependencies
pip install -r requirements.txt

Running the Recommender
python main.py

output format/ it writes directly into a csv file
===== STUDENT 1 (Daniel) =====
1. Mr. Smith
2. Linda
3. Yvonne


student_name,rank_1,rank_2,rank_3
Daniel,Mr. Smith,Linda,Yvonne
Aisha,Ms. Claire,Pierre,Yvonne

Why a Rule-Based Recommendation System?

A rule-based recommendation system was chosen because it is simple, transparent, and effective for small datasets. Unlike machine-learning recommenders, a rule-based system does not require historical interaction data (ratings, bookings, clicks). Instead, it directly uses the attributes of students and tutors such as language, programming focus, level, and hobbies to compute compatibility scores.

This approach is ideal for scenarios with limited or no training data, because the logic can be manually defined and easily understood. It allows full explainability (“This tutor was selected because they speak English and teach Python”), is easy to maintain, and avoids unnecessary model complexity. Therefore, a rule-based recommender provides an appropriate and reliable solution for this task.