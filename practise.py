import numpy as np

# numpy array
# import numpy as np
# marks = np.array([70, 80, 65, 90, 75])
# print(marks)

# shape, size, ndim
# data = np.array([[10, 20, 30], [40, 50, 60]])
# print(data.shape)
# print(data.size)
# print(data.ndim)

# indexing & slicing
# sales = np.array([100, 200, 300, 400, 500])
# print(sales[0])
# print(sales[1])

# practise question
# Topic 1: NumPy Array — 5 Questions

# Q1. Employee Salaries
# Company ma 8 employees na salaries aapela che:
# [32000, 45000, 28000, 52000, 61000, 39000, 47000, 55000]
# NumPy array create karo ane print karo.

# salary = [32000, 45000, 28000, 52000, 61000, 39000, 47000, 55000]
# print(salary)

# Q2. Product Prices
# Ek store na 6 products ni prices:
# [499, 799, 1299, 599, 999, 1499]
# NumPy array create kari ne print karo.

# prices = [499, 799, 1299, 599, 999, 1499]
# print(prices)

# Q3. Monthly Sales
# Company ni 6 months ni sales:
# [45000, 52000, 48000, 61000, 75000, 68000]
# NumPy array create karo ane sales data display karo.

# Monthly_sales = [45000, 52000, 48000, 61000, 75000, 68000]
# print(Monthly_sales)

# Q4. Customer Ratings
# 10 customers e product ne ratings aapi:
# [4, 5, 3, 4, 2, 5, 4, 3, 5, 4]
# NumPy array create karo.

# rating = [4,5,3,4,2,5,4,3,5,4]
# print(rating)

# Q5. Transaction Amounts 🔥
# Ek company na transactions:
# [1200, 4500, 2300, 6700, 1500, 8900, 3200, 5400]
# NumPy array create karo ane check karo ke array successfully create thayu che ke nahi.

# Amounts = [1200, 4500, 2300, 6700, 1500, 8900, 3200, 5400]
# print(Amounts)

# 🟡 Topic 2: shape, size, ndim, dtype — 5 Questions

# Q6. Sales Dataset
# sales = np.array([
#     [12000, 15000, 18000],
#     [22000, 19000, 25000]
# ])

# Find:
# Number of rows and columns using shape
# Total sales records using size
# Number of dimensions using ndim
# Data type using dtype

# sales = np.array([
#     [12000, 15000, 18000],
#     [22000, 19000, 25000]
# ])
# print(sales)
# print(sales.shape)
# print(sales.size)
# print(sales.ndim)
# print(sales.dtype)

# Q7. Employee Dataset

# salary = np.array([
#     [30000, 45000],
#     [50000, 60000],
#     [35000, 42000],
#     [55000, 70000]
# ])

# Find:

# Shape
# Size
# Dimensions
# Data type

# salary = np.array([
#     [30000, 45000],
#     [50000, 60000],
#     [35000, 42000],
#     [55000, 70000]
# ])
# print(salary)
# print(salary.shape)
# print(salary.size)
# print(salary.ndim)
# print(salary.dtype)

# Q8. Product Inventory

# stock = np.array([
#     [120, 80, 150, 200],
#     [90, 110, 75, 130],
#     [180, 160, 140, 100]
# ])

# A company na inventory dataset ma:

# ketli rows che?
# ketla columns che?
# total ketla values che?
# array ketla dimensions nu che?

# Only NumPy properties use karo.

# stock = np.array([
#     [120, 80, 150, 200],
#     [90, 110, 75, 130],
#     [180, 160, 140, 100]
# ])
# print(stock.shape)
# print(stock.size)
# print(stock.ndim)

# Q9. Customer Data
# customers = np.array([120, 150, 180, 200, 175, 220, 250])

# Find:

# Shape
# Size
# Dimension
# Data type

# customers = np.array([120, 150, 180, 200, 175, 220, 250])
# print(customers.shape)
# print(customers.size)
# print(customers.ndim)
# print(customers.dtype)

# Q10. Data Analyst Interview Question 🔥

# revenue = np.array([
#     [10000, 12000, 15000, 18000],
#     [11000, 14000, 16000, 20000],
#     [13000, 15000, 17000, 22000]
# ])

# Without manually counting, NumPy properties thi find karo:

# Total number of values
# Number of rows
# Number of columns
# Number of dimensions

# revenue = np.array([
#     [10000, 12000, 15000, 18000],
#     [11000, 14000, 16000, 20000],
#     [13000, 15000, 17000, 22000]
# ])
# print(revenue.size)
# print(revenue.shape)
# print(revenue.ndim)

# 🔵 Topic 3: Indexing & Slicing — 5 Questions
# Q11. Monthly Revenue
# revenue = np.array([45000, 52000, 48000, 61000, 75000, 68000, 72000, 80000, 77000, 85000, 90000, 95000])

# Find:
# January revenue
# June revenue
# December revenue

# Indexing use karo.

# revenue = np.array([45000, 52000, 48000, 61000, 75000, 68000, 72000, 80000, 77000, 85000, 90000, 95000])
# print("January revenue is:", revenue[0])
# print("June revenue is:", revenue[5])
# print("December revenue is:", revenue[11])

# Q12. Top Sales Months

# Same revenue array ma:

# [45000, 52000, 48000, 61000, 75000, 68000, 72000, 80000, 77000, 85000, 90000, 95000]

# Find:
# First 3 months
# Last 3 months
# April to August ni sales

# Slicing use karo.

# revenue = [45000, 52000, 48000, 61000, 75000, 68000, 72000, 80000, 77000, 85000, 90000, 95000]
# print("First 3 month is:", revenue[0:3])
# print("Last 3 month is:", revenue[9:12])
# print("April to august is:", revenue[3:8])

# Q13. Employee Performance
# performance = np.array([72, 85, 91, 68, 77, 95, 88, 74, 90, 82])

# Find:
# First 5 employees na scores
# Last 4 employees na scores
# Employee 3 thi Employee 7 sudhina scores

# performance = np.array([72, 85, 91, 68, 77, 95, 88, 74, 90, 82])
# print("First 5 employee score:", performance[0:6])
# print("Last 4 employee score:", performance[6:10])
# print("score:", performance[3:8])

# Q14. Daily Website Visitors
# visitors = np.array([
#     1200, 1500, 1800, 2100, 2500,
#     2300, 2700, 3000, 2800, 3200
# ])

# Find:
# First day's visitors
# Last day's visitors
# First 4 days
# Last 4 days
# Day 4 to Day 8 visitors

# visitors = np.array([
#     1200, 1500, 1800, 2100, 2500,
#     2300, 2700, 3000, 2800, 3200
# ])
# print("first day's visitors is:", visitors[0])
# print("Last day's visitors is:", visitors[9])
# print("first 4 days:", visitors[0:5])
# print("Last 4 days:", visitors[6:10])
# print("day 4 to 8:", visitors[4:9])

# Q15. 🔥 Real Data Analyst Challenge

# A company has this monthly profit data:

# profit = np.array([
#     12000, 15000, 11000, 18000,
#     22000, 25000, 21000, 28000,
#     30000, 27000, 32000, 35000
# ])

# Using only indexing and slicing, find:

# January profit
# December profit
# First quarter profit
# Second quarter profit
# Last 6 months profit

# profit = np.array([
#     12000, 15000, 11000, 18000,
#     22000, 25000, 21000, 28000,
#     30000, 27000, 32000, 35000
# ])
# print(profit)
# print("january profit is:", profit[0])
# print("december profit is:", profit[11])
# print("first quarter profit is:", profit[0:4])
# print("second quarter profit is:", profit[4:8])
# print("Last 6 month profit is:", profit[6:12])

# Topic 4: Array Operations

# NumPy array par direct mathematical operations kari shakay che.

# import numpy as np
# sales = np.array([10000, 20000, 30000, 40000])
# print(sales + 5000)
# print(sales * 2)
# print(sales / 2)

# Data Analyst example

# Suppose badha product prices ma 10% increase karvo che:

# price = np.array([100, 200, 300, 400])
# new_price = price * 1.10
# print(new_price)

# 📝 Practice — 5 Questions

# Q1. Employee salary increase

# salary = np.array([30000, 40000, 50000, 60000, 70000])
# Badha employees ni salary ma ₹5,000 add karo.

# salary = np.array([30000, 40000, 50000, 60000, 70000])
# print(salary + 5000)

# Q2. Product discount

# price = np.array([500, 800, 1200, 1500, 2000])
# Badha products par 10% discount calculate karo.

# price = np.array([500, 800, 1200, 1500, 2000])
# discount = price * 0.90
# print(discount)

# Q3. Monthly sales

# sales = np.array([10000, 15000, 20000, 25000])
# Badha sales values ne 2 times karo.

# sales = np.array([10000, 15000, 20000, 25000])
# new_sales = sales * 2
# print(new_sales)

# Q4. Employee salary hike 🔥

# salary = np.array([25000, 35000, 45000, 55000])
# new_salary = salary * 1.15
# print(new_salary)

# Badhi salary ma 15% increment karo.

# Q5. Real-world challenge

# price = np.array([1000, 1500, 2000, 2500, 3000])
# new_price = price * 0.80
# print(new_price)

# Products par 20% discount pachi ni price calculate karo.

# 🟡 Topic 5: Mathematical & Statistical Functions

# Example:

# sales = np.array([10000, 20000, 15000, 30000, 25000])

# print(np.sum(sales))
# print(np.mean(sales))
# print(np.min(sales))
# print(np.max(sales))

# 📝 Practice — 5 Questions

# Q6. Monthly Sales
# sales = np.array([45000, 52000, 48000, 61000, 75000])
# print(np.sum(sales))
# print(np.mean(sales))
# print(np.min(sales))
# print(np.max(sales))

# Find:
# Total sales
# Average sales
# Minimum sales
# Maximum sales

# Q7. Employee Salaries

# salary = np.array([30000, 45000, 50000, 65000, 70000, 40000])
# print(np.mean(salary))
# print(np.max(salary))
# print(np.min(salary))
# print(np.sum(salary))

# Find:
# Average salary
# Highest salary
# Lowest salary
# Total salary

# Q8. Product Ratings

# ratings = np.array([4, 5, 3, 4, 2, 5, 4, 3, 5, 4])
# print("average rating is:", np.mean(ratings))
# print("Highest rating is:", np.max(ratings))
# print("Lowest rating is:", np.min(ratings))
# print("Total of all ratings:",np.sum(ratings))

# Find:
# Average rating
# Highest rating
# Lowest rating
# Total of all ratings

# Q9. Daily Website Visitors

# visitors = np.array([1200, 1500, 1800, 2100, 1700, 2500, 3000])
# print("Total visitors is:", np.sum(visitors))
# print("Avg daily visitors is:", np.mean(visitors))
# print("Highest visitors is:", np.max(visitors))
# print("Lowest visitors is:", np.min(visitors))

# Find:
# Total visitors
# Average daily visitors
# Highest visitors
# Lowest visitors

# Q10. 🔥 Data Analyst Challenge

# revenue = np.array([
#     45000, 52000, 38000, 61000,
#     72000, 49000, 80000, 55000
# ])
# difference = np.max(revenue) - np.min(revenue)
# print("Total visitors is:", np.sum(revenue))
# print("Avg daily visitors is:", np.mean(revenue))
# print("Highest visitors is:", np.max(revenue))
# print("Lowest visitors is:", np.min(revenue))
# print("revenue is:", difference)

# Find:
# Total revenue
# Average revenue
# Highest revenue
# Lowest revenue
# Difference between highest and lowest revenue

# 🔵 Topic 6: Comparison Operators & Boolean Arrays ⭐

# Aa topic next level filtering mate base che.

# Suppose:

# salary = np.array([25000, 40000, 55000, 30000, 70000])

# Aapde check karvu che ke kaya employees ni salary ₹50,000 karta vadhu che:

# print(salary > 50000)

# Data Analyst ma actual filtering
# Boolean condition ne array sathe use kariye:

# salary = np.array([25000, 40000, 55000, 30000, 70000])

# high_salary = salary[salary > 50000]

# print(high_salary)

# 📝 Practice — 5 Questions

# Q11. Employee Salary Filter

# salary = np.array([25000, 45000, 55000, 30000, 65000, 70000])
# print(salary > 50000)

# Find all salaries greater than ₹50,000.

# Q12. Sales Filter

# sales = np.array([12000, 25000, 18000, 35000, 42000, 15000])
# new_sales = sales > 20000
# print(new_sales)

# Find all sales greater than ₹20,000.

# Q13. Product Price Filter

# price = np.array([499, 799, 1299, 599, 1999, 999])
# new_price = price < 1000
# print(new_price)

# Find products whose price is less than ₹1,000.

# Q14. Customer Rating Filter

# rating = np.array([2, 5, 3, 4, 1, 5, 4, 2, 5])
# print(rating >= 4)

# Find all ratings greater than or equal to 4.

# Q15. 🔥 Real Data Analyst Challenge

# salary = np.array([
#     28000, 35000, 45000, 52000,
#     60000, 48000, 75000, 90000,
#     40000, 65000
# ])
# print(salary > 50000)
# print(salary < 40000)
# print(salary >= 60000)

# count = np.sum(salary > 50000)
# print(count)

# Find:

# Salaries greater than ₹50,000
# Salaries less than ₹40,000
# Salaries greater than or equal to ₹60,000
# Count how many employees earn more than ₹50,000

# 🟢 Topic 7: np.where() — Condition Based Selection

# import numpy as np
# salary = np.array([30000, 55000, 45000, 70000, 35000])
# result = np.where(salary > 50000, "High", "Low")
# print(result)


# ⭐ Practice — 5 Questions

# Q1. Employee salary category

# salary = np.array([25000, 45000, 60000, 35000, 75000])
# result = np.where(salary > 50000, "High", "Low")
# print(result)

# np.where() use kari ne:
# salary > 50000 → "High"
# otherwise → "Low"

# Q2. Product stock

# stock = np.array([10, 50, 5, 80, 25, 100])
# result = np.where(stock >= 50, "Available", "Low stock")
# print(result)

# stock >= 50 → "Available"
# otherwise → "Low Stock"

# Q3. Student result

# marks = np.array([45, 78, 32, 90, 55, 28])
# result = np.where(marks >= 40, "Pass", "Fail")
# print(result)

# marks >= 40 → "Pass"
# otherwise → "Fail"

# Q4. Sales performance

# sales = np.array([45000, 72000, 38000, 90000, 55000])
# result = np.where(sales >= 60000, "Good", "Need Improvement")
# print(result)

# sales >= 60000 → "Good"
# otherwise → "Need Improvement"

# Q5. 🔥 Real-world

# profit = np.array([12000, -5000, 18000, -2000, 25000, 8000])
# result = np.where(profit > 0,"Profit", "Loss")
# print(result)

# np.where() use kari ne:
# profit > 0 → "Profit"
# otherwise → "Loss"

# 🟡 Topic 8: Boolean Indexing / Masking ⭐


# Example:

# salary = np.array([30000, 55000, 45000, 70000, 35000])
# high_salary = salary[salary > 50000]
# print(high_salary)

# ⭐ Practice — 5 Questions

# Q6.

# sales = np.array([12000, 25000, 18000, 35000, 42000, 15000])
# high_salary = sales[sales > 20000]
# print(high_salary)

# Sales greater than 20000 filter karo.

# Q7.

# salary = np.array([28000, 45000, 52000, 32000, 70000, 60000])
# new_salary = salary[salary >= 50000]
# print(new_salary)

# Salary greater than or equal to 50000 filter karo.

# Q8.

# price = np.array([499, 799, 1299, 599, 1999, 999])
# new_price = price[price < 1000]
# print(new_price)

# Price less than 1000 hoy e products filter karo.

# Q9.

# rating = np.array([2, 5, 3, 4, 1, 5, 4, 2, 5])
# new_rating = rating[rating >= 4]
# print(new_rating)

# Rating greater than or equal to 4 filter karo.

# Q10. 🔥 Real Data Analyst

# revenue = np.array([
#     25000, 52000, 38000, 65000,
#     72000, 41000, 85000, 30000
# ])
# print(revenue[revenue > 50000])
# print(revenue[revenue < 40000])
# print(revenue[revenue >= 70000])

# Find:
# Revenue > 50000
# Revenue < 40000
# Revenue >= 70000

# 🔵 Topic 9: Multiple Conditions — & and | ⭐🔥

# Example:

# & = and
# salary = np.array([30000, 45000, 55000, 65000, 75000])
# result = salary[(salary > 40000) & (salary < 70000)]
# print(result)

# | = OR
# salary = np.array([30000, 45000, 55000, 65000, 75000])
# result = salary[(salary < 40000) | (salary > 70000)]
# print(result)

# ⭐ Practice — 5 Questions

# Q11. Employee salary

# Find salaries:
# greater than 40000 AND less than 70000

# salary = np.array([25000, 35000, 45000, 55000, 65000, 75000])
# result = salary[(salary > 40000) & (salary < 70000)]
# print(result)


# Q12. Product price

# Find products:
# price >= 700 AND price <= 1800

# price = np.array([300, 700, 1200, 1800, 2500, 900])
# result = price[(price >= 700) & (price <= 1800)]
# print(result)

# Q13. Sales

# Find sales:
# less than 20000 OR greater than 50000

# sales = np.array([15000, 25000, 35000, 45000, 55000, 65000])
# new_sales = sales[(sales < 20000) | (sales > 50000)]
# print(new_sales)

# Q14. Customer rating

# Find ratings:
# equal to 2 OR equal to 5

# rating = np.array([1, 2, 3, 4, 5, 3, 5, 4, 2])
# result = rating[(rating == 2) | (rating == 5)]
# print(result)

# Q15. 🔥🔥 Real Data Analyst Challenge

# Company na employee salaries:

# salary = np.array([
#     28000, 35000, 45000, 52000,
#     60000, 48000, 75000, 90000,
#     40000, 65000
# ])
# result1 = salary[(salary >= 40000) & (salary <= 70000)]
# print(result1)

# result2 = salary[(salary < 35000) | (salary > 75000)]
# print(result2)

# result3 = salary[salary >= 50000]
# print(result3)

# result4 = salary[(salary >= 30000) & (salary <= 60000)]
# print(result4)

# Find:

# Employees earning between ₹40,000 and ₹70,000
# Employees earning less than ₹35,000 OR more than ₹75,000
# Employees earning ₹50,000 or more
# Employees earning between ₹30,000 and ₹60,000

# Topic 11: axis ⭐

# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600]
# ])

# axis=0 → column-wise
# print(np.sum(sales, axis=0))


# ⭐ Practice — 5

# Q6.

# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600],
#     [700, 800, 900]
# ])

# # Column-wise total
# column_total = np.sum(sales, axis=0)

# # Row-wise total
# row_total = np.sum(sales, axis=1)

# print("Column-wise Total:", column_total)
# print("Row-wise Total:", row_total)

# Find total sales:
# column-wise
# row-wise

# Q7.

# marks = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [80, 85, 95]
# ])

# Find average:
# each column
# each row

# marks = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [80, 85, 95]
# ])
# column_avg = np.mean(marks, axis = 0)
# row_avg = np.mean(marks, axis = 1)
# print("column wise avg:", column_avg)
# print("row wise avg:", row_avg)

# Q8.

# revenue = np.array([
#     [10000, 15000, 12000],
#     [18000, 20000, 22000]
# ])
# column_max = np.max(revenue, axis = 0)
# row_max = np.max(revenue, axis = 1)
# print("column wise max:", column_max)
# print("row wise max:", row_max)

# Find maximum:

# column-wise
# row-wise

# Q9.

# expenses = np.array([
#     [5000, 7000, 6000],
#     [8000, 9000, 7500],
#     [4000, 5000, 4500]
# ])
# column_min = np.min(expenses, axis = 0)
# row_min = np.min(expenses, axis = 1)
# print("column wise min:", column_min)
# print("row wise min:", row_min)

# Find minimum:
# column-wise
# row-wise

# Q10. 🔥 Data Analyst Challenge

# sales = np.array([
#     [12000, 15000, 18000, 20000],
#     [22000, 25000, 21000, 28000],
#     [30000, 32000, 35000, 31000]
# ])
# column_total = np.sum(sales, axis=0)
# row_total = np.sum(sales, axis=1)
# print("column wise total:", column_total)
# print("row wise total:", row_total)

# column_avg = np.mean(sales, axis=0)
# row_avg = np.mean(sales, axis=1)
# print("column wise avg:", column_avg)
# print("row wise avg:", row_avg)

# Find:
# Total sales for each row
# Total sales for each column
# Average sales for each row
# Average sales for each column


# 🔵 Topic 12: np.unique() ⭐

# dept = np.array([
#     "IT", "HR", "Sales", "IT", "HR", "IT"
# ])

# print(np.unique(dept))

# # Count pan kari shakay
# values, counts = np.unique(dept, return_counts=True)
# print(values)
# print(counts)

# ⭐ Practice — 5

# Q11. Department Analysis

# dept = np.array([
#     "IT", "HR", "Sales", "IT", "HR",
#     "Finance", "IT", "Sales"
# ])
# print(np.unique(dept))

# Find all unique departments.

# Q12. Customer Cities

# Find unique cities.
# city = np.array([
#     "Surat", "Ahmedabad", "Mumbai", "Surat",
#     "Delhi", "Mumbai", "Surat", "Delhi"
# ])
# print(np.unique(city))

# Q13. Product Categories

# category = np.array([
#     "Laptop", "Mobile", "Laptop", "Tablet",
#     "Mobile", "Laptop", "Tablet", "Mobile"
# ])
# print(np.unique(category))
# values, counts = np.unique(category, return_counts=True)
# print(values)
# print(counts)

# Find:
# Unique categories
# Count of each category

# Q14. Employee Departments 🔥

# dept = np.array([
#     "IT", "HR", "IT", "Sales", "Finance",
#     "HR", "IT", "Sales", "Finance", "IT"
# ])
# print(np.unique(dept))
# values, counts = np.unique(dept, return_counts=True)
# print(values)
# print(counts)

# Find:

# Unique departments
# Number of employees in each department

# Q15. 🔥🔥 Real Data Analyst Challenge

# A company na customer data ma:

# import numpy as np

# city = np.array([
#     "Surat", "Ahmedabad", "Surat",  "Vadodara", "Ahmedabad",
#     "Surat", "Rajkot", "Vadodara", "Surat", "Ahmedabad"])

# # Unique cities and their counts
# cities, counts = np.unique(city, return_counts=True)

# print("Unique Cities:")
# print(cities)

# print("\nCustomer Count:")
# print(counts)

# # City having highest number of customers
# highest_city = cities[np.argmax(counts)]

# print("\nCity with highest customers:")
# print(highest_city)

# print("Highest Customer Count:")
# print(np.max(counts))
# Find:

# All unique cities
# Each city na customers ni count
# Kaya city na customers highest che?

# 14. flatten() and ravel()
# 2D array ને 1D array માં convert કરવા માટે.

# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600]
# ])
# print(sales.flatten())
# print(sales.ravel())

# Practice – 5 Questions

# Q1. Monthly sales:

# sales = np.array([
#     [10000, 12000, 15000],
#     [11000, 13000, 16000]
# ])
# print(sales.flatten())

# flatten() નો ઉપયોગ કરીને 1D sales array બનાવો.

# Q2. Employee salaries:

# salary = np.array([
#     [30000, 35000],
#     [40000, 45000],
#     [50000, 55000]
# ])
# print(salary.ravel())

# ravel() નો ઉપયોગ કરીને 1D array બનાવો.

# Q3. Product quantities:

# quantity = np.array([
#     [10, 20, 30],
#     [15, 25, 35]
# ])
# print(quantity.flatten())
# print("Total quantity:", np.sum(quantity))

# Flatten કરીને total quantity શોધો.

# Q4. Customer IDs:

# customers = np.array([
#     [101, 102, 103],
#     [104, 105, 106]
# ])
# print(customers.flatten())
# print("Total cutomers is:", np.sum(customers))

# 1D array બનાવો અને તેમાં number of customers શોધો.

# Q5. Revenue:

# revenue = np.array([
#     [50000, 60000],
#     [70000, 80000]
# ])
# print(revenue.flatten)
# print("Avg value is:", np.mean(revenue))

# flatten() કરીને average revenue શોધો.

# 15. Transpose .T

# import numpy as np

# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600]
# ])

# print("Original:")
# print(sales)
# print("Transpose:")
# print(sales.T)

# Practice – 5 Questions

# Q6. Employee salary data:

# salary = np.array([
#     [30000, 40000, 50000],
#     [35000, 45000, 55000]
# ])
# print("original:")
# print(salary)
# print("Transpose:")
# print(salary.T)

# print(salary.shape)

# Transpose કરો અને shape print કરો.

# Q7. Monthly sales:

# sales = np.array([
#     [10000, 12000, 15000, 18000],
#     [11000, 13000, 16000, 19000]
# ])
# print("Transpose:")
# print(sales.T)

# Transpose કરો.

# Q8. Product data:

# products = np.array([
#     [100, 200, 300],
#     [10, 20, 30]
# ])
# print("Transpose:")
# print(products.T)


# Q9. Revenue:

# revenue = np.array([
#     [50000, 60000],
#     [70000, 80000],
#     [90000, 100000]
# ])
# print("Original:", revenue)
# print(revenue.shape)
# print("Transpose:")
# print(revenue.T)
# print(revenue.shape)

# Original અને transpose બંનેની shape print કરો.

# Q10. Customer data:

# customers = np.array([
#     [101, 102, 103],
#     [25, 30, 35]
# ])
# # Transpose
# result = customers.T
# print("Original Array:")
# print(customers)
# print("\nTransposed Array:")
# print(result)

# Transpose કરો અને resulting array print કરો.

# 16. np.concatenate(), vstack() અને hstack()

# આ functions નો ઉપયોગ બે અથવા વધુ arrays ને જોડવા માટે થાય છે.

# np.concatenate()
# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])
# result = np.concatenate((a, b))
# print(result)

# vstack() → Vertical
# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])
# print(np.vstack((a, b)))

# hstack() → Horizontal
# print(np.hstack((a, b)))

# Practice – 5 Questions

# Q11. January અને February sales ને concatenate કરો:

# jan = np.array([10000, 12000, 15000])
# feb = np.array([11000, 13000, 16000])
# result = np.concatenate((jan, feb))
# print(result)

# Q12. બે employee salary arrays ને vstack() કરો:

# team1 = np.array([30000, 35000, 40000])
# team2 = np.array([45000, 50000, 55000])
# print(np.vstack((team1, team2)))

# Q13. બે product quantity arrays ને hstack() કરો:

# product1 = np.array([10, 20, 30])
# product2 = np.array([40, 50, 60])
# print(np.hstack((product1, product2)))

# Q14. બે months ના revenue data ને combine કરો:

# march = np.array([50000, 60000, 70000])
# april = np.array([55000, 65000, 75000])
# result = np.concatenate((march, april))
# print(result)

# concatenate() નો ઉપયોગ કરો.

# Q15. બે department ના employee IDs:

# it = np.array([101, 102, 103])
# hr = np.array([201, 202, 203])
# print(np.vstack((it, hr)))

# vstack() નો ઉપયોગ કરીને બંને departments ને એક 2D array માં combine કરો.

# Topic 17: Sorting — np.sort()

# Array ને ascending order માં arrange કરવા માટે np.sort() વાપરીએ.

# import numpy as np
# salary = np.array([50000, 30000, 70000, 40000, 60000])
# result = np.sort(salary)

# print("Original Salary:")
# print(salary)

# print("Sorted Salary:")
# print(result)

# # Descending order:
# print(np.sort(salary)[::-1])

# Practice — 5 Questions

# Q1. Product prices ને ascending order માં sort કરો.

# price = np.array([500, 200, 800, 300, 600])
# print(np.sort(price)[::1])

# Q2. Employee salaries ને descending order માં sort કરો.

# salary = np.array([45000, 30000, 70000, 55000, 40000])
# print(np.sort(salary)[::-1])

# Q3. Monthly sales ને ascending order માં sort કરો.

# sales = np.array([25000, 18000, 35000, 22000, 40000])

# print("Original sales:")
# print(sales)

# print(np.sort(sales)[::1])

# Q4. Customer purchase amounts ને descending order માં sort કરો.

# purchase = np.array([1200, 500, 2500, 800, 1800])
# print(np.sort(purchase)[::-1])

# Q5. Product ratings ને ascending order માં sort કરો.

# rating = np.array([4.5, 2.8, 5.0, 3.5, 4.0])
# print(np.sort(rating)[::1])

# 🔹 Topic 18: np.argmax() and np.argmin()

# import numpy as np
# sales = np.array([10000, 25000, 18000, 40000, 30000])
# index = np.argmax(sales)

# print("Index of highest sales:", index)
# print("Highest Sales:", sales[index])

# # np.argmin()

# index = np.argmin(sales)
# print("Index of lowest sales:", index)
# print("Lowest Sales:", sales[index])

# Practice — 5 Questions

# Q6. Employee salaries માં highest salary અને તેનો index શોધો.

# salary = np.array([35000, 50000, 42000, 70000, 45000])
# index = np.argmax(salary)
# print("Index of the highest salary:", index)
# print("Highest salary:", salary[index])

# Q7. Monthly revenue માં lowest revenue અને તેનો index શોધો.

# revenue = np.array([50000, 62000, 45000, 80000, 55000])
# index = np.argmin(revenue)
# print("Index of lowest revenue:", index)
# print("Lowest revenue:", revenue[index])

# Q8. Product prices માં સૌથી expensive product નો index શોધો.

# price = np.array([500, 1200, 800, 2500, 1500])
# index = np.argmax(price)
# print("Index of expensive price:", index)
# print("Most expensive product:", price[index])

# Q9. Customer spending માં highest spending શોધો.

# spending = np.array([2500, 1800, 4500, 3200, 5000])
# index = np.argmax(spending)
# print("Highest spending:", spending[index])

# Q10. Daily website visitors માં lowest visitors વાળો day/index શોધો.

# visitors = np.array([1200, 1500, 900, 1800, 1300])
# index = np.argmin(visitors)
# print("Lowest visitors:", visitors[index])


# 🔹 Topic 19: np.mean() + np.median() + np.std()

# Mean

# salary = np.array([30000, 40000, 50000, 60000, 70000])
# print(np.mean(salary))

# Median

# salary = np.array([30000, 40000, 50000, 60000, 70000])
# print(np.median(salary))

# Standard Deviation

# sales = np.array([100, 105, 110, 95, 100])
# print(np.std(sales))

# Q11. Employee salaries નો average શોધો.

# salary = np.array([30000, 35000, 40000, 45000, 50000])
# print(np.mean(salary))

# Q12. Customer purchase amounts નો median શોધો.

# purchase = np.array([500, 800, 1200, 1500, 2000])
# print(np.median(purchase))

# Q13. Monthly sales નું mean અને median બંને શોધો.

# sales = np.array([10000, 12000, 15000, 18000, 20000])
# print(np.mean(sales))
# print(np.median(sales))

# Q14. Product prices નો standard deviation શોધો.

# price = np.array([100, 105, 110, 95, 100])
# print(np.std(price))

# Q15. નીચેના revenue data માટે mean, median અને standard deviation શોધો.

# revenue = np.array([
#     50000,
#     55000,
#     60000,
#     65000,
#     70000
# ])
# print("Mean is:", np.mean(revenue))
# print("Median is:", np.median(revenue))
# print("Standard deviation is:", np.std(revenue))


# 🔹 Topic 20: np.sum() with axis

# np.sum() થી total કાઢી શકીએ છીએ.

# 1D Array
# import numpy as np
# sales = np.array([10000, 15000, 20000])
# print(np.sum(sales))

# 2D Array
# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600]
# ])

# print("Total:", np.sum(sales))
# print("Column Total:", np.sum(sales, axis=0))
# print("Row Total:", np.sum(sales, axis=1))

# Practice — 5 Questions

# Q1. ત્રણ મહિનાની sales નું total શોધો.

# sales = np.array([25000, 30000, 35000])
# print("Total:", np.sum(sales))

# Q2. Department-wise salary નું total શોધો.

# salary = np.array([
#     [30000, 35000, 40000],
#     [45000, 50000, 55000]
# ])
# total = np.sum(salary, axis=1)
# print("Department wise salary total:")
# print(total)

# Q3. ઉપરના data માં row-wise salary total શોધો.

# salary = np.array([
#     [30000, 35000, 40000],
#     [45000, 50000, 55000]
# ])
# total = np.sum(salary, axis=1)
# print("Row-wise total:", total)

# Q4. નીચેના product sales નું column-wise total શોધો.

# sales = np.array([
#     [100, 200, 300],
#     [150, 250, 350],
#     [200, 300, 400]
# ])
# total = np.sum(sales, axis=0)
# print("Column-wise total:", total)

# Q5. ઉપરના sales data નું grand total શોધો.

# sales = np.array([
#     [100, 200, 300],
#     [150, 250, 350],
#     [200, 300, 400]
# ])
# total = np.sum(sales)
# print(total)

# 🔹 Topic 21: np.count_nonzero()

# import numpy as np

# salary = np.array([30000, 45000, 60000, 70000, 35000])
# count = np.count_nonzero(salary > 50000)
# print("Employees earning above 50000:", count)

# Another Example
# sales = np.array([10000, 25000, 5000, 30000, 45000])
# print(np.count_nonzero(sales > 20000))

# Practice — 5 Questions

# Q6. Salary > 50000 હોય એવા employees count કરો.

# salary = np.array([30000, 55000, 60000, 45000, 70000, 35000])
# count = np.count_nonzero(salary > 50000)
# print("employee earning more than 50000:", count)

# Q7. Sales > 20000 હોય એવા months count કરો.

# sales = np.array([10000, 25000, 30000, 15000, 40000])
# count = np.count_nonzero(sales > 20000)
# print("Sales above 20000:", count)

# Q8. Product price < 500 હોય એવા products count કરો.

# price = np.array([200, 700, 450, 800, 300, 600])
# count = np.count_nonzero(price < 500)
# print("product price less than 500:", count)

# Q9. Customer spending >= 1000 હોય એવા customers count કરો.

# spending = np.array([500, 1200, 800, 1500, 2000, 700])
# count = np.count_nonzero(spending >= 1000)
# print("Customer spending above 1000 is:", count)

# Q10. Employees with experience > 5 years count કરો.

# experience = np.array([2, 7, 10, 3, 8, 1, 6])
# count = np.count_nonzero(experience > 5)
# print(count)

# 🔹 Topic 22: np.any() and np.all()

# np.any()
# એકપણ value condition satisfy કરે છે?

# import numpy as np
# sales = np.array([10000, 15000, 50000, 20000]
# result = np.any(sales > 40000)
# print(result)

# np.all()
# બધી values condition satisfy કરે છે?

# sales = np.array([10000, 15000, 50000, 20000])
# result = np.all(sales > 5000)
# print(result)

# result = np.all(sales > 15000)
# print(result)


# Data Analyst Example
# salary = np.array([60000, 55000, 70000, 45000])

# print("Any salary above 65000:",
#       np.any(salary > 65000))

# print("All salaries above 40000:",
#       np.all(salary > 40000))


# Practice — 5 Questions

# # Q11. Check કરો કે sales માં કોઈપણ value > 50000 છે કે નહીં.

# sales = np.array([20000, 35000, 45000, 60000])
# print("any sales above 50000:", np.any(sales > 50000))
# print("all sales above 50000:", np.all(sales > 50000))


# Q12. Check કરો કે બધી salaries > 30000 છે કે નહીં.

# salary = np.array([35000, 40000, 50000, 60000])
# print("all salary above 30000:", np.all(salary > 30000))

# Q13. Check કરો કે કોઈ product price < 100 છે કે નહીં.

# price = np.array([200, 150, 80, 300, 250])
# print("any product price below 100:", np.any(price < 100))

# Q14. Check કરો કે બધા employees ની experience >= 2 years છે કે નહીં.

# experience = np.array([3, 5, 2, 7, 4])
# print("all employee experience above 2 years:", np.all(experience >= 2))

# Q15. Customer spending માટે check કરો:

# કોઈ customer > 10000 spend કરે છે?
# બધા customers > 1000 spend કરે છે?

# spending = np.array([2500, 5000, 12000, 3000, 8000])
# print("any customer spend above 10000:", np.any(spending > 10000))
# print("all customer spend above 1000:", np.all(spending > 1000))

# Topic 23: np.cumsum() — Cumulative Sum

# import numpy as np
# sales = np.array([10000, 15000, 12000, 18000])
# result = np.cumsum(sales)

# print("Sales:", sales)
# print("Cumulative Sales:", result)

# Practice — 5 Questions

# Q1. Daily sales નું cumulative total શોધો.

# sales = np.array([5000, 7000, 6000, 8000, 9000])
# result = np.cumsum(sales)
# print("sales:", sales)
# print("cumulative sales:", result)

# Q2. Monthly revenue નું running total શોધો.

# revenue = np.array([20000, 25000, 30000, 28000])
# total = np.cumsum(revenue)
# print("revenue:", revenue)
# print("cumulative sales:", total)

# Q3. Customer purchases નું cumulative spending શોધો.

# purchase = np.array([500, 800, 1200, 700])
# spending = np.cumsum(purchase)
# print("purchase:", purchase)
# print("cumulative purchase:", spending)

# Q4. Daily website visitors નું cumulative count શોધો.

# visitors = np.array([1000, 1200, 1500, 1300])
# total = np.cumsum(visitors)
# print("Visitors:", visitors)
# print("cumulative visitors:",total )

# Q5. 6 months ની sales માટે cumulative sales શોધો.

# sales = np.array([10000, 15000, 12000, 18000, 20000, 22000])
# result = np.cumsum(sales)
# print("sales:", sales)
# print("cumulative result is:", result)

# 🔹 Topic 24: np.diff() — Difference Between Consecutive Values

# import numpy as np
# sales = np.array([100, 120, 150, 130])
# result = np.diff(sales)
# print(result)


# sales = np.array([10000, 12000, 15000, 13000])
# change = np.diff(sales)
# print("Change in Sales:", change)


# Practice — 5 Questions

# Q6. Daily sales માં consecutive change શોધો.

# sales = np.array([10000, 12000, 11000, 15000])
# result = np.diff(sales)
# print(result)

# Q7. Monthly revenue માં difference શોધો.

# revenue = np.array([50000, 55000, 62000, 58000])
# result = np.diff(revenue)
# print(result)

# Q8. Employee salary data માં consecutive difference શોધો.

# salary = np.array([30000, 35000, 40000, 45000])
# result = np.diff(salary)
# print(salary)

# Q9. Website visitors માં daily change શોધો.

# visitors = np.array([1000, 1200, 1100, 1400, 1600])
# result = np.diff(visitors)
# print(result)

# Q10. Product prices માં consecutive price changes શોધો.

# price = np.array([500, 550, 530, 600, 650])
# result = np.diff(price)
# print(result)

# 🔹 Topic 25: np.insert() અને np.delete()

# Array માં value add/remove કરવા માટે.

# np.insert()
# import numpy as np
# salary = np.array([30000, 40000, 50000])
# result = np.insert(salary, 1, 35000)
# print(result)

# np.delete()
# salary = np.array([30000, 40000, 50000])
# result = np.delete(salary, 1)
# print(result)

# Practice — 5 Questions

# Q11. Salary array માં index 2 પર 45000 insert કરો.

# salary = np.array([30000, 35000, 50000, 55000])
# result = np.insert(salary, 2, 45000)
# print(result)

# Q12. Product price array માં index 1 પર 250 insert કરો.

# price = np.array([100, 300, 400, 500])
# result = np.insert(price, 2, 250)
# print(result)

# Q13. Employee salary array માં index 3 delete કરો.

# salary = np.array([30000, 35000, 40000, 45000, 50000])
# result = np.delete(salary, 3)
# print(result)

# Q14. Customer IDs માં index 2 delete કરો.

# customers = np.array([101, 102, 103, 104, 105])
# result = np.delete(customers, 2)
# print(customers)

# Q15. Sales array માં:

# Index 2 પર 18000 insert કરો.
# પછી index 4 delete કરો.

# sales = np.array([10000, 12000, 15000, 20000, 22000])
# result = np.insert(sales, 2, 18000)
# print(result)

# result1 = np.delete(sales, 4)
# print(result1)


# Topic 26: np.mean() with axis

# import numpy as np

# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600]
# ])

# print("Overall Average:", np.mean(sales))
# print("Column-wise Average:", np.mean(sales, axis=0))
# print("Row-wise Average:", np.mean(sales, axis=1))


# Practice — 5 Questions

# Q1. Employee salaries નો row-wise average શોધો.

# salary = np.array([
#     [30000, 35000, 40000],
#     [45000, 50000, 55000]
# ])
# print("Row-wise average:", np.mean(salary))

# Q2. Monthly sales નો column-wise average શોધો.

# sales = np.array([
#     [10000, 12000, 15000],
#     [11000, 13000, 16000],
#     [12000, 14000, 17000]
# ])
# print("Column-wise average:", np.mean(sales))

# Q3. Product ratings નો overall average શોધો.

# rating = np.array([
#     [4, 5, 3],
#     [5, 4, 5]
# ])
# print("Overall average:", np.mean(rating))

# Q4. Revenue નો row-wise average શોધો.

# revenue = np.array([
#     [50000, 60000, 70000],
#     [55000, 65000, 75000]
# ])
# print("Row-wise average:", np.mean(revenue))

# Q5. Sales નો column-wise અને row-wise બંને average શોધો.

# sales = np.array([
#     [10000, 12000, 15000],
#     [11000, 13000, 16000],
#     [12000, 14000, 17000]
# ])
# print("Column-wise average:", np.mean(sales))
# print("Row-wise average:", np.mean(sales))

# 🔹 Topic 27: np.min() / np.max() with axis

# 2D data માં દરેક row અથવા column નું minimum/maximum શોધી શકાય.

# import numpy as np

# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600],
#     [150, 250, 350]
# ])

# print("Column-wise Maximum:", np.max(sales, axis=0))
# print("Row-wise Maximum:", np.max(sales, axis=1))

# print("Column-wise Minimum:", np.min(sales, axis=0))
# print("Row-wise Minimum:", np.min(sales, axis=1))


# Practice — 5 Questions

# Q6. દરેક department માં highest salary શોધો.

# salary = np.array([
#     [30000, 35000, 40000],
#     [45000, 50000, 55000],
#     [60000, 65000, 70000]
# ])
# print("department-wise highest salary:", np.max(salary, axis=1))

# Q7. દરેક month નું minimum sales value શોધો.

# sales = np.array([
#     [10000, 12000, 15000],
#     [8000, 14000, 16000],
#     [11000, 13000, 17000]
# ])
# print("Monthly minimum sales value:", np.min(sales, axis=1))

# Q8. Product prices નું row-wise maximum શોધો.

# price = np.array([
#     [100, 200, 300],
#     [150, 250, 350]
# ])
# print("row-wise maximum:", np.max(price, axis=0))

# Q9. Revenue નું column-wise minimum શોધો.

# revenue = np.array([
#     [50000, 60000, 70000],
#     [45000, 65000, 75000],
#     [55000, 58000, 80000]
# ])
# print("column-wise minimum:", np.min(revenue, axis=1))

# Q10. Sales data માં row-wise maximum અને minimum બંને શોધો.

# sales = np.array([
#     [10000, 12000, 15000],
#     [8000, 14000, 16000],
#     [11000, 13000, 17000]
# ])
# print("row-wise maximum:", np.max(sales))
# print("row-wise minimum:", np.min(sales))

# 🔹 Topic 28: np.isnan() — Missing Values શોધવા

# import numpy as np

# sales = np.array([10000, 15000, np.nan, 20000, 25000])
# print(np.isnan(sales))


# Missing values count કરવી:
# missing = np.sum(np.isnan(sales))
# print("Missing Values:", missing)


# print("Average Sales:", np.nanmean(sales))
# Practice — 5 Questions

# Q11. નીચેના salary data માં missing values શોધો.

# salary = np.array([30000, 40000, np.nan, 50000, np.nan])
# print(np.isnan(salary))

# Q12. Sales data માં total missing values count કરો.

# sales = np.array([10000, np.nan, 15000, 20000, np.nan, 25000])
# missing = np.sum(np.isnan(sales))
# print("Missing Values:", missing)

# Q13. Revenue data માં missing values શોધો અને count કરો.

# revenue = np.array([50000, 60000, np.nan, 70000, 80000])
# print(np.isnan(revenue))
# missing = np.sum(np.isnan(revenue))
# print("Missing values:", missing)

# Q14. Customer spending માં missing values છે. Missing values ignore કરીને average spending શોધો.

# spending = np.array([500, 800, np.nan, 1200, 1500])

# # Missing values ignore કરીને average
# average = np.nanmean(spending)

# print("Average Spending:", average)

# Q15. Product prices માં missing values count કરો અને missing values ignore કરીને average price શોધો.

# price = np.array([100, 200, np.nan, 400, np.nan, 500])
# missing = np.sum(np.isnan(price))
# print("Missing value is:", missing)

# average = np.nanmean(price)
# print("average price:", average)

# Topic 29: np.nan_to_num() — Missing Values Replace કરવી

# import numpy as np
# sales = np.array([10000, 15000, np.nan, 20000, np.nan])
# result = np.nan_to_num(sales, nan=0)

# print("Original:", sales)
# print("After replacing NaN:", result)

# Practice — 5 Questions

# Q1. Missing salary values ને 0 થી replace કરો.

# salary = np.array([30000, np.nan, 40000, np.nan, 50000])
# result = np.nan_to_num(salary, nan=0)
# print("Original:", salary)
# print("After replacing value:", result)

# Q2. Missing sales values ને 0 થી replace કરો.

# sales = np.array([10000, 15000, np.nan, 20000])
# result = np.nan_to_num(sales, nan=0)
# print("Original:", sales)
# print("After replacing values:", result)


# Q3. Missing product prices ને 100 થી replace કરો.

# price = np.array([200, np.nan, 500, np.nan, 800])
# result = np.nan_to_num(price, nan=100)
# print("Original:", price)
# print("After replacing values:", result)

# Q4. Missing customer spending ને 0 થી replace કરો.

# spending = np.array([500, np.nan, 1200, 800, np.nan])
# result = np.nan_to_num(spending, nan=0)
# print("Original:", spending)
# print("After replacing values:", result)

# Q5. Missing revenue ને 0 થી replace કરીને total revenue શોધો.

# revenue = np.array([50000, np.nan, 60000, 70000, np.nan])
# result = np.nan_to_num(revenue, nan=0)
# print("Total revenue:", np.sum(result))

# 🔹 Topic 30: np.percentile() — Percentile

# import numpy as np
# salary = np.array([30000, 40000, 50000, 60000, 70000])
# p50 = np.percentile(salary, 50)
# print("50th Percentile:", p50)

# Common Percentiles
# print(np.percentile(salary, 25))
# print(np.percentile(salary, 50))
# print(np.percentile(salary, 75))


# Practice — 5 Questions

# Q6. Employee salaries નો 50th percentile શોધો.

# salary = np.array([30000, 35000, 40000, 50000, 60000])
# print(np.percentile(salary, 50))

# Q7. Customer spending નો 75th percentile શોધો.

# spending = np.array([500, 800, 1000, 1500, 2000])
# print(np.percentile(spending, 75))

# Q8. Product prices નો 25th percentile શોધો.

# price = np.array([100, 200, 300, 500, 800])
# print(np.percentile(price, 25))

# Q9. Monthly sales નો 90th percentile શોધો.

# sales = np.array([10000, 12000, 15000, 18000, 20000, 25000])
# print(np.percentile(sales, 90))

# Q10. Revenue માટે 25th, 50th અને 75th percentile શોધો.

# revenue = np.array([40000, 50000, 60000, 70000, 80000, 90000])
# print(np.percentile(revenue, 25))
# print(np.percentile(revenue, 50))
# print(np.percentile(revenue, 75))

# 🔹 Topic 31: np.corrcoef() — Correlation


# import numpy as np

# advertising = np.array([10, 20, 30, 40, 50])
# sales = np.array([20, 30, 40, 50, 60])
# result = np.corrcoef(advertising, sales)
# print(result)

# અહીં advertising વધે ત્યારે sales પણ વધે છે, એટલે positive correlation મળશે.


# Practice — 5 Questions

# Q11. Advertising અને sales વચ્ચે correlation શોધો.

# advertising = np.array([10, 20, 30, 40, 50])
# sales = np.array([15, 25, 35, 45, 55])
# result = np.corrcoef(advertising, sales)
# print(result)

# Q12. Study hours અને exam marks વચ્ચે correlation શોધો.

# hours = np.array([1, 2, 3, 4, 5])
# marks = np.array([40, 50, 60, 70, 80])
# result = np.corrcoef(hours, marks)
# print(result)

# Q13. Product price અને quantity sold વચ્ચે correlation શોધો.

# price = np.array([100, 200, 300, 400, 500])
# quantity = np.array([50, 40, 30, 20, 10])
# result = np.corrcoef(price, quantity)
# print(result)

# Q14. Website visitors અને sales વચ્ચે correlation શોધો.

# visitors = np.array([1000, 1500, 2000, 2500, 3000])
# sales = np.array([100, 140, 180, 220, 260])
# result = np.corrcoef(visitors, sales)
# print(result)

# Q15. Customer age અને spending વચ્ચે correlation શોધો.

# age = np.array([20, 25, 30, 35, 40])
# spending = np.array([500, 700, 900, 1200, 1500])
# result = np.corrcoef(age, spending)
# print(result)

# 32. np.clip() — Limit / Cap Values

# np.clip(array, minimum, maximum)

# Example
# salary = np.array([25000, 35000, 50000, 75000, 120000])
# result = np.clip(salary, 30000, 80000)
# print(result)


# Q1. Product prices:

# price = np.array([100, 250, 500, 800, 1500])
# result = np.clip(price, 200, 1000)
# print(result)

# Keep prices between 200 and 1000.

# Q2. Employee salaries:

# salary = np.array([18000, 25000, 40000, 70000, 150000])
# result = np.clip(salary, 25000, 100000)
# print(result)

# Keep salaries between 25000 and 100000.

# Q3. Customer ratings:

# rating = np.array([1, 2, 3, 4, 5, 6, 7])
# result = np.clip(rating, 1,5)
# print(result)

# Keep ratings between 1 and 5.

# Q4. Daily sales:

# sales = np.array([5000, 12000, 18000, 25000, 50000])
# result = np.clip(sales, 10000, 30000)
# print(result)

# Keep sales between 10000 and 30000.

# Q5. Discount percentages:

# discount = np.array([5, 10, 20, 40, 70])
# result = np.clip(discount, 0, 30)
# print(result)

# Company allows maximum 30% discount. Use np.clip().

# 33. np.histogram() — Frequency Distribution

# Example:

# salary = np.array([25000, 30000, 35000, 40000, 45000, 50000])

# counts, bins = np.histogram(
#     salary,
#     bins=[20000, 30000, 40000, 50000, 60000]
# )
# print(counts)
# print(bins)


# Practice — Q6 to Q10

# Q6. Customer spending:

# Create bins:
# 0–1000
# 1000–2000
# 2000–3000
# 3000–5000

# Find the number of customers in each range.
# import numpy as np

# spending = np.array([200, 500, 800, 1200, 1500, 2200, 2800, 3500, 4200])

# bins = [0, 1000, 2000, 3000, 5000]

# counts, edges = np.histogram(spending, bins=bins)

# print("Number of customers in each range:", counts)
# print("Bins:", edges)

# Q7. Employee salaries:

# salary = np.array([22000,25000,28000,32000,35000,42000,48000,55000,65000])
# bins = [0, 20000, 30000, 40000, 70000]
# counts, edges = np.histogram(salary, bins=bins)
# print("Number of employee:", counts)
# print("Bins:", edges)


# Create salary ranges:

# 20000–30000
# 30000–40000
# 40000–50000
# 50000–70000

# Find frequency in each range.

# Q8. Product prices:

# price = np.array([100,150,250,300,450,600,750,900,1200])

# Create ranges:

# 0–300
# 300–600
# 600–1000
# 1000–1500

# price = np.array([100, 150, 250, 300, 450, 600, 750, 900, 1200])

# bins = [0, 300, 600, 1000, 1500]

# counts, edges = np.histogram(price, bins=bins)

# print("Number of products in each range:", counts)
# print("Bins:", edges)

# Q9. Customer age:

# age = np.array([18,22,25,28,31,35,40,45,52,60])

# Create age groups:

# 18–30
# 30–40
# 40–50
# 50–70

# Find the number of customers in each group.

# import numpy as np

# age = np.array([18, 22, 25, 28, 31, 35, 40, 45, 52, 60])
# bins = [18, 30, 40, 50, 70]
# counts, edges = np.histogram(age, bins=bins)
# print("Number of customers in each age group:", counts)
# print("Age groups:", edges)

# Q10. Monthly sales:

# sales = np.array([10000,15000,18000,22000,25000,30000,35000,40000])
# bins = [10000, 20000, 30000, 40000, 50000]
# counts, edges = np.histogram(sales, bins)
# print("number of frequency in each sales group:", counts)
# print("sales groups:", edges)

# Create ranges:

# 10000–20000
# 20000–30000
# 30000–40000
# 40000–50000

# Find the frequency of sales in each range.

# 34. NumPy Set Operations

# 1. np.intersect1d()

# Finds values common in both arrays.

# jan = np.array([101, 102, 103, 104])
# feb = np.array([103, 104, 105, 106])
# result = np.intersect1d(jan, feb)
# print(result)

# 2. np.setdiff1d()

# result = np.setdiff1d(jan, feb)
# print(result)

# 3. np.union1d()

# result = np.union1d(jan, feb)
# print(result)

# 📊 Practice — Q11 to Q15

# Q11. Customer analysis

# jan = np.array([101,102,103,104,105])
# feb = np.array([103,104,105,106,107])
# result = np.intersect1d(jan,feb)
# print(result)

# Find customers who purchased in both months.

# Q12.

# Using the same arrays, find customers who purchased in January but not February.
# jan = np.array([101,102,103,104,105])
# feb = np.array([103,104,105,106,107])
# result = np.setdiff1d(jan,feb)
# print(result)

# Q13.

# Using the same arrays, find all unique customers who purchased in either month.
# jan = np.array([101,102,103,104,105])
# feb = np.array([103,104,105,106,107])
# result = np.union1d(jan, feb)
# print(result)

# Q14. Product analysis

# store_a = np.array([101,102,103,104,105])
# store_b = np.array([103,104,105,106,107])
# result = np.intersect1d(store_a, store_b)
# print(result)

# Find products available in both stores.

# Q15. Customer analysis

# online = np.array([201,202,203,204,205])
# offline = np.array([203,204,206,207])
# result1 = np.intersect1d(online, offline)
# print(result1)

# result2 = np.setdiff1d(online, offline)
# print(result2)

# result3 = np.union1d(online, offline)
# print(result3)

# Find:
# Customers who used both channels
# Customers who used online but not offline
# All unique customers

# Topic 38: np.argsort()

# import numpy as np

# salary = np.array([50000, 30000, 70000, 40000])
# index = np.argsort(salary)
# print(index)
# print(salary[index])

# Employees ને salary પ્રમાણે sort કરવા અને employee names સાથે same order maintain કરવા useful છે.

# name = np.array(["Rahul", "Amit", "Priya", "Neha"])
# salary = np.array([50000, 30000, 70000, 40000])

# index = np.argsort(salary)

# print(name[index])
# print(salary[index])

# Practice Q1–Q5

# Q1. Employee Salary
# name = np.array(["Rahul", "Amit", "Priya", "Neha", "Kiran"])
# salary = np.array([50000, 30000, 70000, 40000, 60000])
# index = np.argsort(salary)
# print(name[index])
# print(salary[index])


# Q2. Product Price
# product = np.array(["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"])
# price = np.array([55000, 800, 1500, 12000, 7000])
# index = np.argsort(price)
# print(product[index])
# print(price[index])

# Task:
# Price પ્રમાણે products ને lowest to highest arrange કરો.

# Q3. Customer Spending
# customer = np.array(["C101", "C102", "C103", "C104", "C105"])
# spending = np.array([5000, 1200, 8000, 3000, 2000])
# index = np.argsort(spending)
# index = index[::-1]
# print(customer[index])
# print(spending[index])

# Task:
# Customer spending પ્રમાણે customers ને highest to lowest arrange કરો.

# Q4. Product Sales ⭐
# product = np.array(["A", "B", "C", "D", "E"])
# sales = np.array([45000, 25000, 70000, 30000, 55000])
# index = np.argsort(sales)
# index = index[::-1]
# print(product[index])
# print(sales[index])

# Q5. Employee Performance ⭐⭐⭐

# name = np.array(["Rahul", "Priya", "Amit", "Neha", "Kiran"])
# performance = np.array([78, 92, 65, 88, 75])
# index = np.argsort(performance)
# index = index[::1]
# print(name[index])
# print(performance[index])

# 🚀 Topic 39: np.ptp()

# sales = np.array([10000, 15000, 12000, 25000, 18000])
# result = np.ptp(sales)
# print(result)


# Practice Q6–Q10

# Q6.

# salary = np.array([30000, 45000, 50000, 70000, 90000])
# result = np.ptp(salary)
# print(result)

# Find salary range.

# Q7.

# sales = np.array([12000, 18000, 25000, 15000, 30000])
# result = np.ptp(sales)
# print(result)

# Find sales range.

# Q8.

# price = np.array([100, 250, 500, 750, 1000])
# result = np.ptp(price)
# print(result)

# Find price range.

# Q9.

# revenue = np.array([50000, 75000, 60000, 90000, 120000])
# result = np.ptp(revenue)
# print(result)

# Find revenue range.

# Q10. Find the range of customer spending:

# spending = np.array([500, 1200, 800, 2500, 4000, 1500])
# result = np.ptp(spending)
# print(result)

# 🚀 Topic 40: np.nanmedian()

# salary = np.array([30000, 40000, np.nan, 50000, 60000])
# result = np.nanmedian(salary)
# print(result)

# np.median() અને np.nanmedian() નો difference:

# np.median(salary)

# → nan

# પરંતુ:

# np.nanmedian(salary)

# → missing value ignore કરીને median આપે છે.

# Practice Q11–Q15

# Q11.

# salary = np.array([30000, 40000, np.nan, 50000, 60000])
# result = np.nanmedian(salary)
# print(result)

# Find median salary ignoring missing value.

# Q12.

# sales = np.array([10000, 15000, np.nan, 20000, 25000])
# result = np.median(sales)
# print(result)

# Find median sales.

# Q13.

# spending = np.array([500, 800, np.nan, 1200, 1500])
# result = np.median(spending)
# print(result)

# Find median customer spending.

# Q14.

# price = np.array([100, 200, np.nan, 400, 500])
# print(np.median(price))

# Find median product price.

# Q15.

# revenue = np.array([50000, np.nan, 75000, 90000, np.nan, 120000])
# print(np.nanmedian(revenue))

# Find median revenue ignoring missing values.

# Topic 41: Broadcasting

# import numpy as np

# salary = np.array([
#     [30000, 40000, 50000],
#     [35000, 45000, 55000]
# ])
# bonus = np.array([2000, 3000, 4000])
# result = salary + bonus
# print(result)


# Practice Q1–Q5

# Q1. Employee Bonus

# salary = np.array([
#     [30000, 40000, 50000],
#     [35000, 45000, 55000]
# ])

# bonus = np.array([2000, 3000, 4000])
# result = salary + bonus
# print(result)

# Broadcasting નો ઉપયોગ કરીને bonus salary માં add કરો.

# Q2. Product Discount
# price = np.array([
#     [1000, 2000, 3000],
#     [1500, 2500, 3500]
# ])

# discount = np.array([100, 200, 300])
# product = price - discount
# print(product)

# દરેક product માંથી corresponding discount subtract કરો.

# Q3. Monthly Sales Target
# sales = np.array([
#     [10000, 15000, 20000],
#     [12000, 18000, 22000]
# ])

# target = np.array([8000, 12000, 18000])
# value = sales - target
# print(value)

# દરેક sales value માંથી corresponding target subtract કરો.

# Q4. Product Price + Tax
# price = np.array([
#     [1000, 2000, 3000],
#     [1500, 2500, 3500]
# ])

# tax = np.array([100, 200, 300])
# amount = price + tax
# print(amount)

# Tax amount add કરીને final price શોધો.

# Q5. Employee Salary Increment ⭐
# salary = np.array([
#     [30000, 40000, 50000],
#     [35000, 45000, 55000]
# ])

# increment = np.array([3000, 4000, 5000])
# updated_salary = salary + increment
# print(updated_salary)

# Broadcasting નો ઉપયોગ કરીને updated salary શોધો.

# Topic 42: np.split()

# import numpy as np

# sales = np.array([10000, 12000, 15000, 18000, 20000, 25000])
# result = np.split(sales, 3)
# print(result)

# 📝 Practice Questions
# Q1. Monthly Sales ⭐

# sales = np.array([10000, 12000, 15000, 18000, 20000, 25000])
# result = np.split(sales, 3)
# print(result)

# Sales data ને 3 equal parts માં split કરો.

# Q2. Employee Salaries
# salary = np.array([30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000])
# result = np.split(salary,4)
# print(result)

# Salary array ને 4 equal parts માં split કરો.

# Q3. Customer IDs
# customer_id = np.array([101, 102, 103, 104, 105, 106])
# result = np.split(customer_id, 2)
# print(result)

# Customer IDs ને 2 equal groups માં split કરો.

# Q4. Product Sales ⭐

# sales = np.array([500, 800, 1200, 1500, 2000, 2500, 3000, 3500])
# result = np.split(sales, 4)
# print(result)
# Sales ને 4 equal parts માં split કરો.

# Q5. Interview-Type Question ⭐⭐⭐

# revenue = np.array([
#     10000, 12000, 15000,
#     18000, 20000, 22000,
#     25000, 28000, 30000
# ])
# result = np.split(revenue, 3)
# print(result)

# Revenue data ને 3 equal groups માં split કરો અને દરેક group print કરો.

# np.vsplit() — Vertical Split

# vsplit() array ને rows પ્રમાણે split કરે છે.

# Perfect Example
# import numpy as np

# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600],
#     [700, 800, 900],
#     [1000, 1100, 1200]
# ])

# result = np.vsplit(sales, 2)

# print(result)

# 🚀 np.hsplit() — Horizontal Split

# Perfect Example
# import numpy as np

# sales = np.array([
#     [100, 200, 300, 400],
#     [500, 600, 700, 800],
#     [900, 1000, 1100, 1200]
# ])

# result = np.hsplit(sales, 2)

# print(result)

# 📊 Data Analyst Practice
# Q1 — vsplit()
# sales = np.array([
#     [100, 200],
#     [300, 400],
#     [500, 600],
#     [700, 800]
# ])
# result = np.vsplit(sales, 2)
# print(result)

# Array ને 2 equal row groups માં split કરો.

# Q2 — vsplit()
# salary = np.array([
#     [30000, 40000],
#     [45000, 50000],
#     [55000, 60000],
#     [65000, 70000]
# ])
# result = np.vsplit(salary, 4)
# print(result)

# Array ને 4 row groups માં split કરો.

# Q3 — hsplit()
# sales = np.array([
#     [100, 200, 300, 400],
#     [500, 600, 700, 800]
# ])
# result = np.hsplit(sales, 2)
# print(result)

# Array ને 2 equal column groups માં split કરો.

# Q4 — hsplit()
# revenue = np.array([
#     [1000, 2000, 3000, 4000],
#     [5000, 6000, 7000, 8000]
# ])
# result = np.hsplit(revenue, 4)
# print(result)

# Array ને 4 column groups માં split કરો.

# Q5 — Interview Type ⭐
# data = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130, 140, 150, 160]
# ])
# result = np.vsplit(data, 2)
# print(result)
# result1 = np.hsplit(data, 2)
# print(result)

# vsplit() નો ઉપયોગ કરીને 2 row groups બનાવો.
# hsplit() નો ઉપયોગ કરીને 2 column groups બનાવો.
# બંનેના output print કરો.

# Topic 44: astype() — Change Data Type

# import numpy as np
# salary = np.array([30000.5, 40000.8, 50000.2])
# new_salary = salary.astype(int)
# print(new_salary)
# print(new_salary.dtype)

# Another Example: String → Integer
# data = np.array(["100", "200", "300"])
# data = data.astype(int)
# print(data)
# print(data.dtype)


# 📝 Practice Questions
# Q1.
# salary = np.array([30000.5, 40000.7, 50000.9])
# data = salary.astype(int)
# print(data)
# print(data.dtype)

# Salary ને int માં convert કરો.

# Q2.
# price = np.array(["100", "250", "500", "750"])
# data = price.astype(int)
# print(price)
# print(data.dtype)

# Price ને int માં convert કરો.

# Q3.
# sales = np.array([10000, 20000, 30000])
# data = sales.astype(float)
# print(sales)
# print(data.dtype)

# Sales ને float માં convert કરો.

# Q4.
# customer_id = np.array([101, 102, 103, 104])
# data = customer_id.astype(float)
# print(customer_id)
# print(data.dtype)

# Customer IDs ને float માં convert કરો અને dtype check કરો.

# Q5. ⭐ Interview Type
# revenue = np.array(["10000", "25000", "50000", "75000"])
# data = revenue.astype(int)
# print(data.dtype)
# print("Total revenue:", np.sum(data)) 

# Revenue ને integer માં convert કરો.
# Converted array નું dtype print કરો.
# Total revenue calculate કરો.

# Topic 45: np.zeros(), np.ones(), np.full()
# 1. np.zeros()

# import numpy as np
# data = np.zeros(5)
# print(data)

# 2. np.ones()

# data = np.ones(5)
# print(data)

# 3. np.full()

# data = np.full(5, 100)
# print(data)


# 📝 Practice Q1–Q5

# Q1. 10 employees માટે initial bonus 0 રાખવા np.zeros() use કરો.
# data = np.zeros(10)
# print(data)

# Q2. 5 products માટે initial stock 1 રાખવા np.ones() use કરો.
# stock = np.ones(5)
# print(stock)

# Q3. 6 products માટે default price 500 રાખવા np.full() use કરો.
# product = np.full(6, 500)
# print(product)

# Q4. 4 departments માટે initial sales target 10000 રાખો.
# departments = np.full(4, 10000)
# print(departments)

# Q5. ⭐ 12 months માટે initial revenue 0 રાખવા યોગ્ય NumPy function use કરો.
# months = np.zeros(12)
# print(months)

# Topic 46: np.arange()

# Syntax
# np.arange(start, stop, step)

# Perfect Data Analyst Example
# import numpy as np
# months = np.arange(1, 13)
# print(months)

# Step સાથે Example
# numbers = np.arange(10, 51, 10)
# print(numbers)

# 📝 Practice Questions
# Q1.

# 1 થી 20 સુધીના numbers ની array બનાવો.
# array = np.arange(1, 11)
# print(array)

# Q2.

# 10 થી 100 સુધીના numbers 10 ના step સાથે બનાવો.
# step = np.arange(10, 110, 10)
# print(step)

# Q3.

# 1 થી 31 સુધીના days of month ની array બનાવો.
# arr = np.arange(1, 31)
# print(arr)

# Q4.

# 2020 થી 2025 સુધીના years ની array બનાવો.
# years = np.arange(2020, 2026)
# print(years)

# Q5. ⭐ Interview Type

# Company ના product IDs 1001 થી 1020 સુધી છે.

# np.arange() નો ઉપયોગ કરીને બધા product IDs ની array બનાવો.

# product_id = np.arange(1001, 1021)
# print(product_id)

# Topic 47: np.linspace()

# np.linspace(start, stop, number_of_values)

# import numpy as np
# data = np.linspace(0, 100, 5)
# print(data)


# salary_range = np.linspace(20000, 60000, 5)
# print(salary_range)


# 📝 5 Practice Questions

# Q1. 0 થી 100 વચ્ચે 6 equally spaced values બનાવો.
# data = np.linspace(0, 100, 6)
# print(data)

# Q2. ₹10,000 થી ₹50,000 વચ્ચે 5 equally spaced salary values બનાવો.
# salary = np.linspace(10000, 50000, 5)
# print(salary)

# Q3. 1 થી 10 વચ્ચે 10 equally spaced values બનાવો.
# values = np.linspace(1, 10, 10)
# print(values)

# Q4. Product price ₹500 થી ₹2500 વચ્ચે 5 equally spaced values generate કરો.
# price = np.linspace(500, 2500, 5)
# print(price)

# Q5. ⭐ Sales range ₹20,000 થી ₹1,00,000 વચ્ચે 9 equally spaced values generate કરો.
# sales = np.linspace(20000, 100000, 9)
# print(sales)

# Topic 48: np.random Functions

# import numpy as np
# data = np.random.randint(1, 101, 5)
# print(data)

# spending = np.random.randint(500, 5001, 10)
# print(spending)

# 5. Practice Questions

# Q1. 1 થી 100 વચ્ચે 10 random numbers generate કરો.
# numbers = np.random.randint(1, 101, 10)
# print(numbers)

# Q2. 500 થી 5000 વચ્ચે 8 random customer spending values generate કરો.
# values = np.random.randint(500, 5001, 8)
# print(values)

# Q3. 20 employees માટે 20 થી 60 વચ્ચે random ages generate કરો.
# ages = np.random.randint(20, 61, 20)
# print(ages)

# Q4. 100 થી 1000 વચ્ચે 10 random product prices generate કરો.
# prices = np.random.randint(100, 1001, 10)
# print(prices)

# Q5. ⭐ 10000 થી 50000 વચ્ચે 15 random monthly sales values generate કરો.
# sales = np.random.randint(10000, 50001, 15)
# print(sales)

# Topic 49: Advanced / Fancy Indexing

# import numpy as np
# sales = np.array([10000, 20000, 30000, 40000, 50000])
# result = sales[[0, 2, 4]]
# print(result)

# Suppose 5 productsની sales છે અને આપણને Product 1, Product 3 અને Product 5 ની sales જોઈએ:

# import numpy as np
# sales = np.array([15000, 22000, 18000, 30000, 25000])
# selected = sales[[0, 2, 4]]
# print(selected)


# 📝 5 Practice Questions

# Q1. Employee salaries [30000, 45000, 50000, 60000, 75000] માંથી 1st, 3rd અને 5th salary select કરો.
# salary = np.array([30000, 45000, 50000, 60000, 75000])
# selected = salary[[0, 2, 4]]
# print(selected)

# Q2. Product prices માંથી index 1, 3, 4 ના prices select કરો.
# price = np.array([500, 800, 1200, 1500, 2000])
# result = price[[1, 3, 4]]
# print(result)

# Q3. Customer spending માંથી index 0, 2, 5 ના customers select કરો.
# spending = np.array([500, 1200, 800, 2000, 1500, 3000])
# result = spending[[0, 2, 5]]
# print(result)

# Q4. Monthly sales માંથી January, March અને June ની sales select કરો.
# sales = np.array([
#     10000, 15000, 12000, 18000, 20000, 25000,
#     22000, 28000, 30000, 27000, 32000, 35000
# ])
# result = sales[[0, 2, 5]]
# print(result)

# Q5. ⭐ 10 employeesના performance scoresમાંથી index 2, 5, 7, 9 ના scores select કરો.
# import numpy as np
# score = np.array([65, 72, 88, 91, 76, 95, 68, 84, 79, 90])
# result = score[[2, 5, 7, 9]]
# print(result)

# Fancy Indexing

# import numpy as np
# salary = np.array([30000, 40000, 50000, 60000, 70000])
# result = salary[[0, 2, 4]]
# print(result)


# Data Analyst Example 📊
# sales = np.array([10000, 15000, 20000, 25000, 30000])
# selected_sales = sales[[1, 3, 4]]
# print(selected_sales)


# Practice – 5 Questions

# Q1. Employee salariesમાંથી index 0, 2, 4 select કરો.
# salary = np.array([30000, 45000, 50000, 60000, 75000])
# selected_value = salary[[0, 2, 4]]
# print(selected_value)

# Q2. Product pricesમાંથી index 1, 3, 4 select કરો.
# price = np.array([500, 800, 1200, 1500, 2000])
# value = price[[1, 3, 4]]
# print(value)

# Q3. Customer spendingમાંથી index 0, 2, 5 select કરો.
# spending = np.array([500, 1200, 800, 2000, 1500, 3000])
# value = spending[[0, 2, 5]]
# print(value)

# Q4. Monthly salesમાંથી January, March અને June select કરો.
# sales = np.array([
#     10000, 15000, 12000, 18000, 20000, 25000,
#     22000, 28000, 30000, 27000, 32000, 35000
# ])
# Monthly_sales = sales[[0, 2, 5]]
# print(Monthly_sales)

# Q5. ⭐ Employee performance scoresમાંથી index 2, 5, 7, 9 select કરો.
# score = np.array([65, 72, 88, 91, 76, 95, 68, 84, 79, 90])
# value = score[[2, 5, 7, 9]]
# print(value)

# Topic 50: 2D Array Indexing & Slicing

# import numpy as np
# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600],
#     [700, 800, 900]
# ])

# print(sales[1, 2])
# print(sales[1])

# print(sales[:, 1])


# 📝 Practice Questions
# Q1
# આ array માંથી 2nd employee ની March sales select કરો.

# sales = np.array([
#     [10000, 12000, 15000],
#     [20000, 22000, 25000],
#     [15000, 18000, 21000]
# ])
# result = sales[1, 2]
# print(result)

# Q2
# બધા employees ની February sales select કરો.

# sales = np.array([
#     [11000, 13000, 16000],
#     [21000, 23000, 26000],
#     [14000, 17000, 20000]
# ])
# result = sales[:, 1]
# print(result)

# # Q3
# 1st employee ની complete sales select કરો.

# sales = np.array([
#     [12000, 14000, 16000],
#     [18000, 20000, 22000],
#     [25000, 27000, 29000]
# ])
# employee = sales[0]
# print(employee)

# Q4
# આ array માંથી 2nd અને 3rd employee ની sales select કરો.

# sales = np.array([
#     [10000, 12000, 14000],
#     [20000, 22000, 24000],
#     [30000, 32000, 34000],
#     [40000, 42000, 44000]
# ])
# employee = sales[2]
# print(employee)

# employee1 = sales[3]
# print(employee1)

# Q5 ⭐

# આ array માંથી January અને March ની બધી sales select કરો.

# sales = np.array([
#     [10000, 12000, 15000],
#     [20000, 22000, 25000],
#     [30000, 32000, 35000],
#     [40000, 42000, 45000]
# ])
# months = sales[:, [0, 2]]
# print(months)

# Topic 51: np.concatenate()

# import numpy as np
# sales_jan = np.array([[100, 200],
#                       [300, 400]])

# sales_feb = np.array([[500, 600],
#                       [700, 800]])

# result = np.concatenate((sales_jan, sales_feb), axis=0)

# print(result)

# np.concatenate((sales_jan, sales_feb), axis=0)

# np.concatenate((sales_jan, sales_feb), axis=1)


# 📝 5 Practice Questions
# Q1

# January અને February ની sales arrays ને row-wise (axis=0) combine કરો.

# jan = np.array([
#     [10000, 12000],
#     [15000, 18000]
# ])

# feb = np.array([
#     [11000, 13000],
#     [16000, 19000]
# ])
# result = np.concatenate((jan, feb), axis=0)
# print(result)

# Q2
# Product price અને discount data ને column-wise (axis=1) combine કરો.

# price = np.array([
#     [500],
#     [800],
#     [1200]
# ])

# discount = np.array([
#     [50],
#     [80],
#     [120]
# ])
# result = np.concatenate((price, discount), axis=1)
# print(result)

# Q3
# 2025 અને 2026 ના employee salary data ને rows તરીકે combine કરો.

# salary_2025 = np.array([
#     [30000, 40000],
#     [45000, 50000]
# ])

# salary_2026 = np.array([
#     [35000, 45000],
#     [50000, 55000]
# ])
# result = np.concatenate((salary_2025, salary_2026), axis=0)
# print(result)

# Q4
# Customer spending અને customer visits ને columns તરીકે combine કરો.

# spending = np.array([
#     [500],
#     [800],
#     [1200]
# ])

# visits = np.array([
#     [3],
#     [5],
#     [7]
# ])
# result = np.concatenate((spending, visits), axis=1)
# print(result)

# Q5 ⭐

# Two sales teams ના data ને row-wise combine કરો.

# team_A = np.array([
#     [10000, 12000, 15000],
#     [18000, 20000, 22000]
# ])

# team_B = np.array([
#     [25000, 27000, 30000],
#     [32000, 35000, 38000]
# ])
# result = np.concatenate((team_A, team_B), axis=0)
# print(result)

# Example

# 📝 5 Real Data Analyst Practice Questions

# Q1 — Sales Analysis
# sales = np.array([12000, 18000, 25000, 9000, 32000, 15000, 40000])
# new_sales = (sales[sales > 20000])
# print(new_sales)

# ₹20,000 કરતાં વધારે sales શોધો.

# Q2 — Customer Spending
# import numpy as np

# spending = np.array([500, 1200, 800, 2500, 3000, 700, 1800])

# average = np.mean(spending)
# result = spending[spending > average]

# print("Average spending:", average)
# print("Above average spending:", result)


# Average spending કરતાં વધારે spending કરનારા customersની values શોધો.

# Q3 — Employee Salary ⭐
# salary = np.array([30000, 45000, 52000, 38000, 65000, 70000, 42000])
# max = np.max(salary)
# print("Highest salary is:", max)

# min = np.min(salary)
# print("Lowest salary is:", min)

# diff = np.max(salary) - np.min(salary)
# print("The diffrence is:", diff)

# Highest salary શોધો.
# Lowest salary શોધો.
# Highest અને lowest salary વચ્ચેનો difference શોધો.


# Q4 — Product Discount
# price = np.array([500, 800, 1200, 1500, 2000])
# discount = price * 0.80
# print("Price is:", discount)

# દરેક product પર 20% discount આપ્યા પછીની final price શોધો.

# Q5 — Monthly Sales ⭐

# sales = np.array([
#     10000, 12000, 15000, 11000,
#     18000, 22000, 20000, 25000,
#     28000, 30000, 27000, 35000
# ])

# # Total yearly sales શોધો.
# Total_sales = np.sum(sales)
# print("Total sales is:", Total_sales)

# # Average monthly sales શોધો.
# Avg_sales = np.mean(sales)
# print("Avg sales is:", Avg_sales)

# # Highest monthly sales શોધો.
# Highest_sales = np.max(sales)
# print("Highest sales is:", Highest_sales)

# # Lowest monthly sales શોધો.
# Lowest_sales = np.min(sales)
# print("lowest sales is:", Lowest_sales)


# copy and view

# Q1. Create a NumPy array [10, 20, 30, 40]. Create a copy using copy(), change the first element of the
#  copy to 100, and print both arrays.
# arr = np.array([10,20,30,40])
# new_arr = arr.copy()
# new_arr[0] = 100
# print(arr)
# print(new_arr)

# Q2. Create a NumPy array [5, 10, 15, 20]. Create a view using view(), change the last element of the view to 50, and print both arrays.
# arr = np.array([5,10,15,20])
# new = arr.view()
# new[3] = 50
# print(arr)
# print(new)

# Q3. Create an array [1, 2, 3, 4, 5]. Make a copy, change the third element of the copy to 99, and verify whether the original array changed.
# arr = np.array([1,2,3,4,5])
# new = arr.copy()
# new[2] = 99
# print(arr)
# print(new)

# Q4. Create an array [10, 20, 30]. Make a view, change the second element of the view to 200, and print the original and view arrays.
# arr = np.array([10, 20, 30])
# new = arr.view()
# new[1] = 200
# print(arr)
# print(new)

# Q5. Create a 2 × 3 NumPy array, make both a copy() and a view(), modify one element in each, 
# and print the original, copy, and view.
# arr = np.array([[10, 20, 30],
#                [40, 50, 60]])

# new = arr.copy()
# new[1][2] = 100

# new1 = arr.view()
# new[0][1] = 500

# print("Original array:", arr)
# print("copy array:", new)
# print("view array:", new1)
