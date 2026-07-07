# Student Performance Analysis using Pandas

## Overview

This project demonstrates how to analyze student performance data using Python and the Pandas library.

The program reads student records from a CSV file, performs statistical analysis, calculates averages, and identifies the top-performing student.

This project was created as part of my Data Science learning journey.


## Objectives

- Learn how to read CSV files using Pandas
- Perform basic data analysis
- Calculate subject-wise averages
- Find highest and lowest scores
- Create new calculated columns
- Identify the best-performing student

---

##  Technologies Used

- Python 3
- Pandas
- VS Code
- Git & GitHub

---

##  Project Structure

```
07_Pandas/
│
├── student_performance_analysis.py
├── students.csv
└── README.md
```

---

## Dataset

The dataset contains marks of students in three subjects:

- Maths
- Science
- English

Example:

| Name | Maths | Science | English |
|------|-------|---------|----------|
| Rahul | 78 | 85 | 67 |
| Priya | 92 | 90 | 95 |
| Amit | 45 | 56 | 60 |

---

## Features

The program:

- Reads student data from a CSV file
- Displays the first five records
- Calculates:
  - Total number of students
  - Average Maths marks
  - Average Science marks
  - Average English marks
- Finds:
  - Highest Maths score
  - Lowest Maths score
- Creates a new **Average** column
- Identifies the top-performing student
- Displays a summary report

---

## Pandas Functions Used

- `pd.read_csv()`
- `head()`
- `mean()`
- `max()`
- `min()`
- `idxmax()`
- DataFrame column selection
- Creating new columns

---

## What I Learned

Through this project I learned:

- Reading CSV files using Pandas
- Working with DataFrames
- Selecting rows and columns
- Performing statistical calculations
- Creating calculated columns
- Organizing a data analysis project

---

##  How to Run

1. Clone the repository

```bash
git clone https://github.com/Pragati244/Python-Projects.git
```

2. Navigate to the project folder

```bash
cd Python-Projects/07_Pandas
```

3. Install Pandas

```bash
pip install pandas
```

4. Run the program

```bash
python student_performance_analysis.py
```

---

## Future Improvements

- Add data visualization using Matplotlib
- Export the analysis to a new CSV file
- Add grade calculation
- Create subject-wise graphs
- Build an interactive dashboard

---

## Author

**Pragati**

GitHub: https://github.com/Pragati244

This project is part of my Data Science learning portfolio.