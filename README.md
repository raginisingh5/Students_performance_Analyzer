# Student Performance Analyzer

A beginner-friendly Python command-line application that calculates a student's total marks, average percentage, pass/fail status, and letter grade, then saves the report to a local text file.

## Features
- Calculates total marks and rounded average percentage
- Checks subject-wise pass criteria (minimum 35 marks per subject)
- Assigns letter grades (`A+`, `A`, `B`, `C`, `D`, `E`, `F`)
- Automatically saves and appends reports to `student_reports.txt`

## How to Run
1. Make sure Python 3 is installed on your computer.
2. Clone this repository or download `student_analyzer.py`.
3. Open a terminal in the project folder and run:
   ```bash
   python student_analyzer.py
   ```

## Example Output
```text
----- STUDENT REPORT -----
Student Name  : Ragi
Maths Marks   : 35
Science Marks : 95
English Marks : 90
Total Marks   : 220 / 300
Average Marks : 73.33%
Grade         : B
Result Status : PASS
--------------------------
```
