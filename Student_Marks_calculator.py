print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter student name: ")

m1 = int(input("Enter marks in English (out of 100): "))
m2 = int(input("Enter marks in Maths (out of 100): "))
m3 = int(input("Enter marks in Python (out of 100): "))
m4 = int(input("Enter marks in Physics (out of 100): "))
m5 = int(input("Enter marks in Chemistry (out of 100): "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Needs Improvement")
