# Project 01 - CGPA to Percentage and Grade Checker

print("--- VIT AP CGPA Checker ---")

# Input - remember input is always string, so convert
name = input("Enter your name: ")
cgpa = float(input("Enter your CGPA (0-10): "))

# Calculation
percentage = cgpa * 9.5

# Logic - if elif else
if cgpa >= 9:
    grade = "O - Outstanding"
elif cgpa >= 8:
    grade = "A+ - Excellent"
elif cgpa >= 7:
    grade = "A - Very Good"
elif cgpa >= 6:
    grade = "B - Good"
elif cgpa >= 5:
    grade = "C - Pass"
else:
    grade = "F - Fail, work harder"

# Output - the pro way with f-string
print(f"\nHello {name}!")
print(f"Your CGPA is {cgpa}")
print(f"Your Percentage is {percentage}%")
print(f"Your Grade is {grade}")

# Bonus - check scholarship
if cgpa >= 9.0:
    print("You are eligible for merit scholarship!")