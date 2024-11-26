import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data2.csv')

print(df.head())
print(df.describe())
mv = df.isnull().sum()
print("missing values in each column:\n", mv)

avg = df['Age'].mean()
print(f"Avarage of Age: {avg}")
uv = df['Age'].nunique()
print(f"unique values: {uv}")

eng_emp = df[df['Department']  == 'Engineering']
print(eng_emp)

max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary'] == max_salary]
print("Highest paid employee: \n", max_salary_emp)

dep_count = df['Department'].value_counts()
print("number of employees in each department: \n", dep_count)

sort = df.sort_values(by = 'Age', ascending = False)
print("senior to junior employee: \n", sort)

df['Experince'] = df['Age'].apply(lambda  x: 'senior' if x>=30 else 'junior')
print("data with Experince column: \n", df)

# data visualization

plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
plt.title("Department")
plt.show()