import numpy as np 
np.random.seed(7)
names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
                  'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
                  'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
                       'Bhavna', 'Sanjay'])   # 20 employees 

dept = np.array(['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR',                     
                 'Sales', 'IT', 'Accounts', 'IT', 'Sales', 'HR',                     
                 'Accounts', 'IT', 'Sales', 'IT', 'Accounts', 'HR', 'Sales'])

salaries = np.random.randint(18000, 95001, 20)   # monthly salary 
age = np.random.randint(22, 56, 20) 
exp_yrs  = np.random.randint(0, 21, 20)         # years of experience

# Task 1. Display all five arrays along with the shape, size, ndim, and dtype of each. 
# Verify that every array has exactly 20 elements.
# print("Names:", names)
# print("Department:", dept)
# print("Salaries:", salaries)
# print("Age:", age)
# print("Experience:", exp_yrs)

# print("\n--- Array Information ---")

# print("Names -> Shape:", names.shape, "Size:", names.size,
#       "ndim:", names.ndim, "dtype:", names.dtype)

# print("Department -> Shape:", dept.shape, "Size:", dept.size,
#       "ndim:", dept.ndim, "dtype:", dept.dtype)

# print("Salaries -> Shape:", salaries.shape, "Size:", salaries.size,
#       "ndim:", salaries.ndim, "dtype:", salaries.dtype)

# print("Age -> Shape:", age.shape, "Size:", age.size,
#       "ndim:", age.ndim, "dtype:", age.dtype)

# Task 2. Display the salaries array's itemsize and nbytes. Verify the formula : 
# size x itemsize = nbytes.
# import numpy as np
# salaries = np.random.randint(18000, 95001, 20)
# print("Size:", salaries.size)
# print("Itemsize:", salaries.itemsize)
# print("nbytes:", salaries.nbytes)

# print("size * itemsize:", salaries.size * salaries.itemsize)
# print("Formula verified:", salaries.size * salaries.itemsize == salaries.nbytes)

# Task 3. Display the complete details of the first employee
#  : name, department, salary, age, and experience (use index 0 on all arrays).
# import numpy as np

# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])   # 20 employees 

# dept = np.array(['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR',                     
#                  'Sales', 'IT', 'Accounts', 'IT', 'Sales', 'HR',                     
#                  'Accounts', 'IT', 'Sales', 'IT', 'Accounts', 'HR', 'Sales'])

# salaries = np.random.randint(18000, 95001, 20)   # monthly salary 
# age = np.random.randint(22, 56, 20) 
# exp_yrs  = np.random.randint(0, 21, 20)

# print("Name:", names[0])
# print("dept:", dept[0])
# print("salaries:", salaries[0])
# print("age:", age[0])
# print("exp_yrs:", exp_yrs[0])

# Task 4. Display the complete details of the last employee using negative indexing.
# import numpy as np

# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])   # 20 employees 

# dept = np.array(['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR',                     
#                  'Sales', 'IT', 'Accounts', 'IT', 'Sales', 'HR',                     
#                  'Accounts', 'IT', 'Sales', 'IT', 'Accounts', 'HR', 'Sales'])

# salaries = np.random.randint(18000, 95001, 20)   # monthly salary 
# age = np.random.randint(22, 56, 20) 
# exp_yrs  = np.random.randint(0, 21, 20)

# print("Name:", names[-1])
# print("dept:", dept[-1])
# print("salaries:", salaries[-1])
# print("age:", age[-1])
# print("exp_yrs:", exp_yrs[-1])

# Task 5. Display the names of employees 5 to 12 using slicing.
# import numpy as np

# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])   # 20 employees 

# dept = np.array(['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR',                     
#                  'Sales', 'IT', 'Accounts', 'IT', 'Sales', 'HR',                     
#                  'Accounts', 'IT', 'Sales', 'IT', 'Accounts', 'HR', 'Sales'])

# salaries = np.random.randint(18000, 95001, 20)   # monthly salary 
# age = np.random.randint(22, 56, 20) 
# exp_yrs  = np.random.randint(0, 21, 20)

# print("Name:", names[5:13])
# print("dept:", dept[5:13])
# print("salaries:", salaries[5:13])
# print("age:", age[5:13])
# print("exp_yrs:", exp_yrs[5:13])

# Task 6. Display the names of every alternate employee using step slicing.
# import numpy as np

# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])   # 20 employees 

# dept = np.array(['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR',                     
#                  'Sales', 'IT', 'Accounts', 'IT', 'Sales', 'HR',                     
#                  'Accounts', 'IT', 'Sales', 'IT', 'Accounts', 'HR', 'Sales'])

# salaries = np.random.randint(18000, 95001, 20)   # monthly salary 
# age = np.random.randint(22, 56, 20) 
# exp_yrs  = np.random.randint(0, 21, 20)

# print("Alternate employee:", names[::2])

# Task 7. Display all employee names in reverse order using [::-1].
# import numpy as np

# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])   # 20 employees 

# dept = np.array(['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR',                     
#                  'Sales', 'IT', 'Accounts', 'IT', 'Sales', 'HR',                     
#                  'Accounts', 'IT', 'Sales', 'IT', 'Accounts', 'HR', 'Sales'])

# salaries = np.random.randint(18000, 95001, 20)   # monthly salary 
# age = np.random.randint(22, 56, 20) 
# exp_yrs  = np.random.randint(0, 21, 20)

# print("Reverse order:", names[::-1])

# Task 8. Calculate the company's total monthly salary expense.
# salaries = np.random.randint(18000, 95001, 20)  # monthly salary 
# print("salaries:", salaries)
# print("Total_salaries:", np.sum(salaries))

# Task 9. Calculate the average, maximum, and minimum salary.
# salaries = np.random.randint(18000, 95001, 20)  # monthly salary 
# print("salaries:", salaries)
# print("average salaries:", np.mean(salaries))
# print("maximum salaries:", np.max(salaries))
# print("Minimum salaries:", np.min(salaries))

# Task 10. Find the highest paid employee
#  — display the name and salary (use argmax on salaries and use that index on names).

# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])   # 20 employees 

# salaries = np.random.randint(18000, 95001, 20)
# highest_index = np.argmax(salaries)

# print("Highest paid employee:", names[highest_index])
# print("Highest salary:", salaries[highest_index])

# Task 11. Find the lowest paid employee — display the name and salary (use argmin).
# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])   # 20 employees 

# salaries = np.random.randint(18000, 95001, 20)

# lowest_index = np.argmin(salaries)

# print("Lowest paod employee:", names[lowest_index])
# print("Lowest salary:", salaries[lowest_index])

# Task 12. Find the oldest and youngest employee by name (argmax and argmin on age).

# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])

# age = np.random.randint(22, 56, 20) 

# oldest_index = np.argmax(age)

# print("Name:", names[oldest_index])
# print("age:", age[oldest_index])

# youngest_index = np.argmin(age)

# print("Name:", names[youngest_index])
# print("age:", age[youngest_index])

# Task 13. Find the most experienced employee by name.
# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])

# exp_yrs  = np.random.randint(0, 21, 20)         # years of experience

# Most_experience = np.argmax(exp_yrs)

# print("Name:", names[Most_experience])
# print("Exp_yrs:", exp_yrs[Most_experience])

# Task 14. Boolean indexing : display the names of all employees earning more than 60,000.
# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])

# salaries = np.random.randint(18000, 95001, 20)

# high_salary = salaries > 60000

# print("employee earning more than 60000:", names[high_salary])

# Task 15. Count how many employees earn less than 30,000.
# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])

# salaries = np.random.randint(18000, 95001, 20)

# low_salary = salaries < 30000

# print("Employees earning less than 30000:", names[low_salary])

# Task 16. Display the names of employees aged between 25 and 35 (use the & operator).
# age = np.random.randint(22, 56, 20) 

# print(age[(age > 25) & (age<35)])

# Task 17. Display the names of employees who earn below 25,000 OR above 80,000 (use the |
# operator).

# salaries = np.random.randint(18000, 95001, 20)
# print(salaries[(salaries < 25000) | (salaries > 80000)])

# Task 18. Count how many employees earn more than the company average salary, and display their
# names.
# avg_salary = np.mean(salaries)
# high_salary = names[salaries > avg_salary]

# print("Average salary is:", avg_salary)
# print("Employee earning more than average:")
# print(high_salary)
# print("Count:", len(high_salary))

# Task 19. Boolean indexing on a string array : display the names and salaries of all IT department
# employees (use dept == 'IT' as the mask).

# mask = dept == 'IT'

# print("IT Department Employees:")
# print(names[mask])
# print(salaries[mask])

# Task 20. Calculate the average salary of the IT department only (apply the same mask on salaries).
# mask = dept == 'IT'
# it_avg_salary = np.mean(salaries[mask])
# print("Average IT department salary:", it_avg_salary)

# Task 21. Calculate the average salary of each department : IT, HR, Sales, and Accounts (repeat the
# mask technique four times).
# mask = dept == 'IT'
# it_avg_salary = np.mean(salaries[mask])
# print("Average IT department salary:", it_avg_salary)

# mask = dept == "HR"
# hr_avg_salary = np.mean(salaries[mask])
# print("Average HR department salary:", hr_avg_salary)

# mask = dept == "Sales"
# sales_avg_salary = np.mean(salaries[mask])
# print("Average Sales department salary:", sales_avg_salary)

# mask = dept == "Accounts"
# accounts_avg_salary = np.mean(salaries[mask])
# print("Average account department salary:", accounts_avg_salary)

# Task 22. Which department has the highest average salary?
# Task 22. Department with the highest average salary

# departments = np.unique(dept)

# avg_salaries = []

# for d in departments:
#     avg = np.mean(salaries[dept == d])
#     avg_salaries.append(avg)

# highest_index = np.argmax(avg_salaries)

# print("Department with highest average salary:", departments[highest_index])
# print("Highest Average Salary:", avg_salaries[highest_index])

# Task 23. Count how many employees work in each department (use boolean masks with sum).
# Task 23. Count employees in each department

# departments = np.unique(dept)

# for d in departments:
#     count = np.sum(dept == d)
#     print(d, ":", count)

# Task 24. Display the names of Sales employees who earn more than 50,000 (combine two masks with
# &).
# mask = (dept == "Sales") & (salaries > 50000)
# print(names[mask])

# Task 25. Display the names of employees with more than 10 years of experience.
# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])

# exp_yrs  = np.random.randint(0, 21, 20) 

# more_exp = exp_yrs > 10
# print("Name of employee:", names[more_exp])

# Task 26. Freshers check : count employees with less than 2 years of experience and display their
# names and departments.
# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                        'Bhavna', 'Sanjay'])

# dept = np.array(['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR',                     
#                  'Sales', 'IT', 'Accounts', 'IT', 'Sales', 'HR',                     
#                  'Accounts', 'IT', 'Sales', 'IT', 'Accounts', 'HR', 'Sales'])

# exp_yrs  = np.random.randint(0, 21, 20) 

# less_exp = exp_yrs < 2
# print("Count of employees:", less_exp.sum())
# print("Name of employee:", names[less_exp])
# print("Name of departments:", dept[less_exp])


# Task 27. The company announces a 10% increment for everyone. Build the new salary array using
# broadcasting (no loops allowed).
# salaries = np.random.randint(18000, 95001, 20)   # monthly salary 
# print("Salaries is:", salaries)

# new_salaries = salaries * 1.10
# print("New salaries is:", new_salaries)

# Task 28. Extra reward : employees with more than 10 years of experience get an additional 5,000. Add
# this using np.where() on the incremented salaries.
# import numpy as np

# # Employee names
# names = np.array(['Rahul', 'Priya', 'Amit', 'Sneha', 'Kiran', 'Vijay', 
#                   'Meena', 'Suresh', 'Kavita', 'Nilesh', 'Hetal', 'Jignesh',                      
#                   'Pooja', 'Manish', 'Dipika', 'Harsh', 'Riya', 'Chirag',                   
#                   'Bhavna', 'Sanjay'])

# # Departments
# dept = np.array(['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR',                     
#                  'Sales', 'IT', 'Accounts', 'IT', 'Sales', 'HR',                     
#                  'Accounts', 'IT', 'Sales', 'IT', 'Accounts', 'HR', 'Sales'])

# # Experience of employees
# exp_yrs = np.random.randint(0, 21, 20)

# # Salaries
# salaries = np.random.randint(18000, 95001, 20)

# print("Original Salaries:", salaries)
# print("Experience:", exp_yrs)

# # Task 27: 10% increment
# new_salaries = salaries * 1.10

# print("New Salaries after 10% increment:", new_salaries)

# # Task 28: Additional ₹5,000 reward for employees
# # with more than 10 years of experience
# reward = np.where(exp_yrs > 10, 5000, 0)

# # Add reward to incremented salaries
# final_salaries = new_salaries + reward

# print("Reward:", reward)
# print("Final Salaries:", final_salaries)