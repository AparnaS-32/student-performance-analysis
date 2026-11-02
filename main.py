
# Student Performance Analysis
# Project 1 - GitHub Portfolio

students = [
    {"name": "Anu", "python": 85, "maths": 90, "data_science": 88},
    {"name": "Rahul", "python": 72, "maths": 78, "data_science": 75},
    {"name": "Meera", "python": 95, "maths": 92, "data_science": 96},
    {"name": "Arjun", "python": 65, "maths": 70, "data_science": 68},
    {"name": "Diya", "python": 88, "maths": 85, "data_science": 91},
]

subjects = ["python", "maths", "data_science"]

print("=" * 55)
print("       STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("=" * 55)

# Calculate each student's average and percentage
for student in students:
    total = sum(student[subject] for subject in subjects)
    average = total / len(subjects)
    percentage = (total / (len(subjects) * 100)) * 100

    student["average"] = average
    student["percentage"] = percentage

    print(f"\nStudent: {student['name']}")
    print(f"Python: {student['python']}")
    print(f"Maths: {student['maths']}")
    print(f"Data Science: {student['data_science']}")
    print(f"Average: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")

# Find the highest-performing student
top_student = max(students, key=lambda student: student["average"])

print("\n" + "=" * 55)
print(f"Top Performer: {top_student['name']}")
print(f"Average Mark: {top_student['average']:.2f}")

# Calculate subject-wise averages
print("\nSUBJECT-WISE AVERAGES")
for subject in subjects:
    average = sum(student[subject] for student in students) / len(students)
    print(f"{subject.replace('_', ' ').title()}: {average:.2f}")

print("\nAnalysis completed successfully!")
print("=" * 55)

import matplotlib.pyplot as plt

# Chart 1: Student Average Marks
student_names = [student["name"] for student in students]
student_averages = [student["average"] for student in students]

plt.figure(figsize=(8, 5))
plt.bar(student_names, student_averages)
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

# Chart 2: Subject-wise Average Marks
subject_averages = [
    sum(student[subject] for student in students) / len(students)
    for subject in subjects
]

plt.figure(figsize=(8, 5))
plt.bar(
    [subject.replace("_", " ").title() for subject in subjects],
    subject_averages
)
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

