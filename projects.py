# project-1 sales analysis system

import numpy as np

# month = np.array([
#     "January", "February", "March", "April",
#     "May", "June", "July", "August",
#     "September", "October", "November", "December"
# ])

# sales = np.array([
#     120000, 135000, 150000, 142000,
#     160000, 155000, 170000, 165000,
#     180000, 210000, 240000, 260000
# ])

# Find Total Sales
# Total_sales = np.sum(sales)
# print("Total sales is:", Total_sales)

# Find Average Sales
# Avg_sales = np.mean(sales)
# print("avg sales is:", Avg_sales)

# Find Highest & Lowest Sales
# Highest_sales = np.argmax(sales)
# print("highest sales is:", Highest_sales)

# Lowest_sales = np.argmin(sales)
# print("lowest sales is:", Lowest_sales)

# Find Best Selling Month
# best_month = np.argmax(sales)
# best_sales = sales[best_month]

# print("best month:", best_month)
# print("best_sales:", best_sales)

# Find Worst Selling Month
# worst_month = np.argmin(sales)
# worst_sales = sales[worst_month]

# print("worst month:", worst_month)
# print("worst_sales:", worst_sales)

# Calculate Quarterly Sales
# Q1 = np.sum(sales[0:3])
# Q2 = np.sum(sales[3:6])
# Q3 = np.sum(sales[6:9])
# Q4 = np.sum(sales[9:12])

# print("Q1 Sales:", Q1)
# print("Q2 Sales:", Q2)
# print("Q3 Sales:", Q3)
# print("Q4 Sales:", Q4)

# Apply 18% GST
# GST = sales * 0.18
# sales_with_gst = sales + GST

# print("gst amount:", GST)
# print("sales with gst:", sales_with_gst)

# Calculate Annual Growth %
# previous_year = 1500000
# current_year = np.sum(sales)

# growth = ((current_year - previous_year) / previous_year) * 100

# print("Current Year Sales:", current_year)
# print("Annual Growth %:", growth)

# project 2: student result analysis
import numpy as np

# students = np.array([
#     "Aarav", "Diya", "Raj", "Meera", "Krish",
#     "Anaya", "Yash", "Riya", "Dev", "Isha",
#     "Arjun", "Pooja", "Karan", "Neha", "Rohan",
#     "Sneha", "Aditya", "Kavya", "Dhruv", "Nisha",
#     "Harsh", "Priya", "Vivek", "Simran", "Manav",
#     "Jiya", "Rahul", "Tanya", "Sahil", "Mahi",
#     "Jay", "Aditi", "Varun", "Khushi", "Nikhil",
#     "Ayesha", "Meet", "Sana", "Parth", "Anjali",
#     "Om", "Shreya", "Devansh", "Muskan", "Tushar",
#     "Avni", "Rudra", "Palak", "Akash", "Tanvi"
# ])

# marks = np.array([
#     78, 92, 65, 88, 45,
#     73, 56, 81, 39, 95,
#     67, 52, 84, 71, 48,
#     90, 76, 63, 85, 58,
#     69, 34, 91, 77, 62,
#     55, 43, 87, 72, 29,
#     80, 94, 68, 51, 89,
#     74, 60, 97, 46, 83,
#     38, 79, 70, 25, 86,
#     64, 93, 57, 41, 75
# ])

# Tasks
# ● Average Marks
# Avg_marks = np.mean(marks)
# print("avg marks is:", Avg_marks)

# ● Highest Marks
# Highest_marks = np.max(marks)
# print("highest marks is:", Highest_marks)

# ● Lowest Marks
# Lowest_marks = np.min(marks)
# print("lowest marks is:", Lowest_marks)

# ● Pass/Fail Students
# passing_student = marks[marks >= 40]
# print("student has passed:", passing_student)

# Failing_student = marks[marks < 40]
# print("students has fail:", Failing_student)

# ● Grade Calculation
# grade = np.where(marks >= 90, "A+",
#         np.where(marks >= 80, "A",
#         np.where(marks >= 70, "B", 
#         np.where(marks >= 60, "C",
#         np.where(marks >= 50, "D", 
#         np.where(marks >= 40, "E", "F"))))))
# print(grade)
        
# ● Top 5 Students
# top5 = np.argsort(marks)[-5:][::-1]
# students[top5]
# marks[top5]

# ● Students Above Average
# average = np.mean(marks)
# above_average = students[marks > average]
# print("average is:", above_average)

# ● Standard Deviation
# SD = np.std(marks)
# print("standard deviation is:", SD)

# project 3:Employee salary analysis
import numpy as np

salary = np.array([
    28000, 35000, 45000, 52000, 60000,
    48000, 75000, 90000, 40000, 65000,
    32000, 55000, 70000, 42000, 58000,
    80000, 47000, 62000, 38000, 95000
])

# Tasks
# ● Average Salary
# Avg_salary = np.mean(salary)
# print("avg salary is:", Avg_salary)

# # ● Highest Salary
# Max_salary = np.max(salary)
# print("highest salary is:", Max_salary)

# # ● Lowest Salary
# Lowest_salary = np.min(salary)
# print("lowest salary is:", Lowest_salary)

# ● Tax Deduction 10%
# tax = salary * 0.10
# print("salary:", salary)
# print("tax deduction:", tax)

# ● Salary After Tax
# tax = salary * 0.10
# new_salary = salary - tax
# print(new_salary)

# ● Employees earning above ₹50,000
# earning = salary[salary > 50000]
# print(earning)

# project 4:product price analysis
# import numpy as np

# products = np.array([
#     "Laptop",
#     "Mobile",
#     "Headphones",
#     "Smartwatch",
#     "Tablet",
#     "Keyboard",
#     "Mouse",
#     "Monitor",
#     "Printer",
#     "Speaker"
# ])

# price = np.array([
#     55000,
#     25000,
#     3000,
#     5000,
#     18000,
#     2500,
#     1200,
#     15000,
#     12000,
#     4500
# ])

# Tasks
# ● Add GST
# GST = price * 1.18
# new_price = GST + price
# print("new price is:", new_price)

# ● Apply Discount
# Discount = price * 0.10
# product_price = price - Discount
# print("price is:", product_price)

# ● Final Price
# gst = price * 0.18
# price_with_gst = price + gst

# discount = price_with_gst * 0.10
# final_price = price_with_gst - discount

# print("Final Price:", final_price)

# ● Most Expensive Product
# Most_expensive = np.max(price)
# print("most expensive product is:", Most_expensive)

# ● Cheapest Product
# Cheapest_product = np.min(price)
# print("chepest product is:", Cheapest_product)

# ● Products Above ₹1000
# above_1k = products[price > 1000]
# print("the product is:", above_1k)

# Project 2 — Student Performance Analysis

# students = np.array([
#     'Aarav', 'Diya', 'Rohan', 'Isha', 'Vivaan',
#     'Anaya', 'Arjun', 'Meera', 'Kabir', 'Myra',
#     'Dev', 'Sara', 'Yash', 'Kiara', 'Reyansh',
#     'Tara', 'Aditya', 'Riya', 'Krish', 'Aanya'
# ])

# department = np.array([
#     'IT', 'CS', 'IT', 'EC', 'CS',
#     'IT', 'ME', 'CS', 'IT', 'EC',
#     'CS', 'IT', 'ME', 'CS', 'EC',
#     'IT', 'CS', 'ME', 'IT', 'EC'
# ])

# marks = np.random.randint(30, 101, 20)
# attendance = np.random.randint(50, 101, 20)
# assignments = np.random.randint(3, 11, 20)

# Practice questions
# Display array information for all arrays.
# print("students is:", students)
# print("department is:", department)
# print("marks is:", marks)
# print("attendance is:", attendance)
# print("assignments is:", assignments)

# print("== Array information ==")

# print("students -> shape:", students.shape, "size:", students.size, "ndim:", students.ndim, 
#       "dtype:", students.dtype)
# print("department -> shape:", department.shape, "size:", department.size, "ndim:", department.ndim, 
#       "dtype:", department.dtype)
# print("marks -> shape:", marks.shape, "size:", marks.size, "ndim:", marks.ndim, "dtype:", marks.dtype)
# print("attendance -> shape:", attendance .shape, "size:", attendance .size, "ndim:", attendance.ndim, 
#       "dtype:", attendance .dtype)
# print("assignments -> shape:", assignments.shape, "size:", assignments.size, "ndim:", assignments.ndim, 
#       "dtype:", assignments.dtype)

# Display first student's complete details.
# print("students is:", students[0])
# print("department is:", department[0])
# print("marks is:", marks[0])
# print("attendance is:", attendance[0])
# print("assignments is:", assignments[0])

# Display last student's complete details.
# print("students is:", students[-1])
# print("department is:", department[-1])
# print("marks is:", marks[-1])
# print("attendance is:", attendance[-1])
# print("assignments is:", assignments[-1])

# Display students from position 6 to 15.
# print("students is:", students[6:16])
# print("department is:", department[6:16])
# print("marks is:", marks[6:16])
# print("attendance is:", attendance[6:16])
# print("assignments is:", assignments[6:16])

# Display alternate students.
# print("students is:", students[::2])
# print("department is:", department[::2])
# print("marks is:", marks[::2])
# print("attendance is:", attendance[::2])
# print("assignments is:", assignments[::2])

# Reverse the student array.
# print("students is:", students[::-1])
# print("department is:", department[::-1])
# print("marks is:", marks[::-1])
# print("attendance is:", attendance[::-1])
# print("assignments is:", assignments[::-1])

# Find total marks.
# Total_marks = np.sum(marks)
# print("Total marks is:", Total_marks)

# Find average, maximum and minimum marks.
# avg_marks = np.mean(marks)
# print("avg marks is:", avg_marks)

# Find the highest-scoring student using argmax().
# highest_scoring = np.argmax(marks)
# print("student:", students[highest_scoring])
# print("highest score is:", marks[highest_scoring])

# Find the lowest-scoring student using argmin().
# lowest_scoring = np.argmin(marks)
# print("student:", students[lowest_scoring])
# print("lowest score is:", marks[lowest_scoring])

# Display students scoring above 80.
# above_80 = students[marks > 80]
# print("above 80 is:", above_80)

# Count students scoring below 50.
# below_50 = marks < 50
# print(below_50.sum())

# Display students with marks between 60 and 80 using &.
# student_marks = marks[(marks >= 60) & (marks <= 80)]
# print("student marks is:", student_marks)

# Display students scoring below 40 OR above 90 using |.
# student_marks = marks[(marks < 40)|(marks > 90)]
# print("student marks is:", student_marks)

# Display students with attendance above 75%.
# student_att = attendance[(attendance > 75)]
# print("student attendance is:", student_att)

# Count students with attendance below 60%.
# student_att = attendance[(attendance < 60)]
# print("student attendance is:", student_att)

# Display students having marks above 70 AND attendance above 80%.
# result = students[(marks>70)&(attendance>80)]
# print(result)

# Calculate average marks of IT students.
# IT_students = marks[department == "IT"]
# print(np.mean(IT_students))

# Calculate average marks of CS students.
# cs_students = marks[department == "CS"]
# print(np.mean(cs_students))

# Calculate average marks of EC students.
# ec_students = marks[department == "EC"]
# print(np.mean(ec_students))

# Calculate average marks of ME students.
# me_students = marks[department == "ME"]
# print(np.mean(me_students))

# Find the department with the highest average marks.
# categories = np.unique(department)

# averages = []

# for c in categories:
#     avg = np.mean(marks[department == c])
#     averages.append(avg)

# index = np.argmax(averages)

# print("Highest Average Marks Department:", categories[index])
# print("Average Marks:", averages[index])

# Count students in every department.
# categories = np.unique(department)
# for c in categories:
#     count = np.sum(department == c)
#     print(c, ":", count)

# Display students with more than 8 assignments.
# student_assi = students[assignments > 8]
# print("More than 8 assignments:", student_assi)

# Create a grade array using nested np.where().
# grade = np.where(marks >= 90, "A+",
#         np.where(marks >= 80, "A",
#         np.where(marks >= 70, "B", 
#         np.where(marks >= 60, "C",
#         np.where(marks >= 50, "D", 
#         np.where(marks >= 40, "E", "F"))))))
# print(grade)

# Count A/B/C/D students.
# grade = np.where(marks >= 90, "A+",
#         np.where(marks >= 80, "A",
#         np.where(marks >= 70, "B", 
#         np.where(marks >= 60, "C",
#         np.where(marks >= 50, "D", 
#         np.where(marks >= 40, "E", "F"))))))
# print(grade)

# print("A+:", np.sum(grade == "A+"))
# print("A:", np.sum(grade == 'A'))
# print("B:", np.sum(grade == 'B'))
# print("C:", np.sum(grade == 'C'))
# print("D:", np.sum(grade == 'D'))
# print("E:", np.sum(grade == "E"))
# print("F:", np.sum(grade == "F"))

# Display all A-grade students.
# grade = np.where(marks >= 90, "A+",
#         np.where(marks >= 80, "A",
#         np.where(marks >= 70, "B", 
#         np.where(marks >= 60, "C",
#         np.where(marks >= 50, "D", 
#         np.where(marks >= 40, "E", "F"))))))
# print(grade)
# result = students[grade == "A"]
# print(result)

# Sort marks and display top 5.
# marks = np.random.randint(30, 101, 20)
# sorted_marks = np.sort(marks)
# top_5 = sorted_marks[-5:][::-1]
# print("Top 5 marks:", top_5)

# Use argsort() to display students from lowest to highest marks.
# index = np.argsort(marks)
# print("Lowest to highest marks:", marks[index])
# print("students:", students[index])

# Display Top 5 students.
# sorted_marks = np.sort(students)
# top_5 = sorted_marks[-5:][::-1]
# print("Top 5 students:", top_5)

# Create a performance score using marks and attendance.
# performance = (marks * 0.7) + (attendance * 0.3)
# print("performance score:", performance)

# Combine marks, attendance and assignments using vstack().
# marks = np.random.randint(30, 101, 20)
# attendance = np.random.randint(50, 101, 20)
# assignments = np.random.randint(3, 11, 20)

# matrix = np.vstack((marks, attendance, assignments))
# print(matrix)

# Transpose the matrix.
# marks = np.random.randint(30, 101, 20)
# attendance = np.random.randint(50, 101, 20)
# assignments = np.random.randint(3, 11, 20)

# matrix = np.vstack((marks, attendance, assignments))
# print(matrix)

# Transpose = matrix.T
# print(Transpose)

# Perform copy vs view test.
# copy_marks = marks.copy()
# copy_marks[0] = 0

# print("Original:", marks)
# print("Copy:", copy_marks)

# view_marks = marks.view()
# view_marks[0] = 0

# print("Original:", marks)
# print("View:", view_marks)