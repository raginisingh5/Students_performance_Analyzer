print("========================================")
print("      STUDENT PERFORMANCE ANALYZER      ")
print("========================================")

# 1. Get student details and marks
name = input("Enter student name: ").strip()
maths = int(input("Enter Maths marks (0-100): "))
science = int(input("Enter Science marks (0-100): "))
english = int(input("Enter English marks (0-100): "))

# 2. Calculate total and rounded average
total = maths + science + english
average = round(total / 3, 2)

# 3. Determine Pass/Fail status and Letter Grade
if maths < 35 or science < 35 or english < 35:
    status = "FAIL (Scored below 35 in one or more subjects)"
    grade = "F"
else:
    status = "PASS"
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "E"

# 4. Build the formatted report
report = (
    "\n----- STUDENT REPORT -----\n"
    f"Student Name  : {name}\n"
    f"Maths Marks   : {maths}\n"
    f"Science Marks : {science}\n"
    f"English Marks : {english}\n"
    f"Total Marks   : {total} / 300\n"
    f"Average Marks : {average}%\n"
    f"Grade         : {grade}\n"
    f"Result Status : {status}\n"
    "--------------------------\n"
)

# 5. Display and save the report
print(report)

with open("student_reports.txt", "a") as file:
    file.write(report)

print("Report saved to student_reports.txt!")