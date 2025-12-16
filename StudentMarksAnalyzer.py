students = {
    "Zaid": 80,
    "Fatima": 92,
    "Ahmed": 89,
    "Hafsa": 84,
    "Bilal": 93,
    "Maryam": 78,
    "Omar": 90,
    "Aisha": 87,
    "Ali": 85,
    "Zainab": 88,
    "Hassan": 77,
    "Ibrahim": 86,
    "Sami": 87,
    "Khadija": 95,
    "Usman": 81,
    "Tariq": 83,
    "Yusuf": 79,
    "Hussain": 82,
    "Amina": 91,
    "Omarah": 84
}

marks = [num for name, num in students.items()]

total_students = 0
total_marks = 0
for mark in marks:
    total_students += 1
    total_marks += mark

avg_marks = total_marks / total_students

max_marks = max(marks)
min_marks = min(marks)

top_students = [name for name, mark in students.items() if mark == max_marks]
bottom_students = [name for name, mark in students.items() if mark == min_marks]

print("Total students:", total_students)
print("Average marks:", round(avg_marks, 2))
print("Highest marks:", max_marks)
print("Student(s) with highest marks:", top_students)
print("Lowest marks:", min_marks)
print("Student(s) with lowest marks:", bottom_students)
