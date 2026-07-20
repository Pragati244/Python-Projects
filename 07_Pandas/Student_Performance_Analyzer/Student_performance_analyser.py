import pandas as pd
import numpy as np
df = pd.read_csv('07_Pandas\\students.csv')


Total_students = print(f'Total students: {df.shape[0]}\n')

Math_average = print(f'Math marks average: {df["Maths"].mean()}\n')

English_average = print(f'English marks average: {df["English"].mean()}\n')

Science_average = print(f'Science marks average: {df["Science"].mean()}\n')

Highest_Math = print(f'Highest math score: {df["Maths"].max()}\n')

lowest_Math = print(f'Lowest math score: {df["Maths"].min()}\n')

df["Average"] = df[["Maths", "English", "Science"]].mean(axis=1)

df["Result"] = np.where(df["Average"] >=40, "Pass", "Fail")

print(f'Number of students with Science marks > 80: {df["Science"][df["Science"] > 80].count()}')

print(f'Student with highest average: {df["Name"][df["Average"] == df["Average"].max()].iloc[0]}')
print(df.sort_values(by="Average", ascending=False))