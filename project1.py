# import numpy as np

# np.random.seed(1)
# sales = np.random.randint(5000, 50001, 30) # 30 days of daily sales (in Rupees) 
# print(sales)

# # Task 1. Display the sales data along with its shape, size, ndim, and dtype.
# np.random.seed(1)
# sales = np.random.randint(5000, 50001, 30)  
# print(sales)
# print(sales.shape)
# print(sales.size)
# print(sales.ndim)
# print(sales.dtype)

# # Task 2. Calculate the total revenue of the month (sum of all 30 days).
# sales = np.random.randint(5000, 50001, 30)  
# total_revenue = np.sum(sales)
# print("Total revenue:", total_revenue)

# # Task 3. Calculate the average daily sales.
# sales = np.random.randint(5000, 50001, 30)  
# avg_sales = np.mean(sales)
# print("average daily sales:", avg_sales)

# Task 4. Find the best sales day 
# — display both the day number (index) and the sales value (use argmax).
# best_day = np.argmax(sales)
# best_sales = sales[best_day]

# print("best day:", best_day)
# print("best sales:", best_sales)

# Task 5. Find the worst sales day
# — display both the day number (index) and the sales value (use argmin).
# worst_day = np.argmin(sales)
# worst_sales = sales[worst_day]

# print("worst day:", worst_day)
# print("worst sales:", worst_sales)

# Task 6. Count how many days had sales ABOVE the monthly average (use boolean indexing).
# sales = np.random.randint(5000, 50001, 30)
# monthly_average = np.mean(sales)
# above_average = sales > monthly_average
# print("monthly_average:", monthly_average)
# print("Days above average:", np.sum(above_average))

# Task 7. Days with sales below 20,000 are considered 'Slow Days'.
#  Count how many Slow Days occurred this month.
# sales = np.random.randint(5000, 50001, 30)
# slow_days = sales < 20000
# print("Total slow days:", np.sum(slow_days))

# Task 8. Filter and display all sales values that fall between 20,000 and 35,000 
# (use the & operator). 
# sales = np.random.randint(5000, 50001, 30)
# print(sales[(sales > 20000) & (sales < 35000)])

# Task 9. Display all days where sales were either below 10,000 OR above 40,000 
# (use the | operator).
# sales = np.random.randint(5000, 50001, 30)
# print(sales[(sales < 10000) | (sales > 40000)])

# # Task 10. Using np.where(), create a label array : if sales >= 30,000 mark the day as
# #  'Target Achieved', otherwise 'Target Missed'. Count how many days achieved the target.
# sales = np.random.randint(5000, 50001, 30)
# labels = np.where(sales >= 30000, "Target Achived", "Target Missed")
# print(labels)
# count = np.sum(sales >= 30000)
# print("Target achived days:", count)

# Task 11. Compare the first 15 days vs the last 15 days — which half of the month generated 
# more revenue? (Use slicing + sum.)
# first_half = sales[:15]
# last_half = sales[15:]

# first_revenue = np.sum(first_half)
# last_revenue = np.sum(last_half)

# print("First 15 days revenue:", first_revenue)
# print("Last 15 days revenue:", last_revenue)

# if first_revenue > last_revenue:
#     print("First half generated more revenue")
# else:
#     print("Last half generated more revenue")

# Task 12. Sort the sales in descending order and display the Top 5 best sales days.
# sorted_sales = np.sort(sales)[::-1]
# top_5 = sorted_sales[:5]
# print("top 5 days:", top_5)

# Task 13. Sort the sales in ascending order and display the Bottom 3 worst sales days.
# sorted_sales = np.sort(sales)
# bottom_3 = sorted_sales[:3]
# print("Bottom 3 days:", bottom_3)

# Task 14. The store adds 5% GST on all sales. 
# Create a new array with GST-inclusive values (use broadcasting — no loops allowed)
# sales = np.random.randint(5000, 50001, 30)
# GST = sales * 1.05
# print(GST)

# Task 15. Every alternate day (day 1, 3, 5, ...) the store ran an advertisement. Extract the sales 
# of these alternate days using step slicing, and calculate their average. Compare it with the 
# average of the non-advertisement days — did the advertisement work? 
# Advertisement days: Day 1, 3, 5, 7, ...
# ad_days = sales[::2]

# # Non-advertisement days: Day 2, 4, 6, 8, ...
# non_ad_days = sales[1::2]

# # Calculate averages
# ad_average = np.mean(ad_days)
# non_ad_average = np.mean(non_ad_days)

# print("Advertisement days sales:", ad_days)
# print("Advertisement average:", ad_average)

# print("Non-advertisement days sales:", non_ad_days)
# print("Non-advertisement average:", non_ad_average)

# # Compare
# if ad_average > non_ad_average:
#     print("Advertisement worked!")
# else:
#     print("Advertisement did not work.")

# Task 16. Replace all sales values below 10,000 with exactly 10,000 (assume a minimum guaranteed 
# franchise income) using np.where(). Recalculate the new total revenue and compare it with the 
# original. 
# Replace sales below 10,000 with 10,000
# new_sales = np.where(sales < 10000, 10000, sales)

# print("Original Sales:", sales)
# print("New Sales:", new_sales)

# # Calculate total revenue
# original_total = np.sum(sales)
# new_total = np.sum(new_sales)

# print("Original Total Revenue:", original_total)
# print("New Total Revenue:", new_total)

# print("Revenue Increase:", new_total - original_total)

# Task 17. Reshape the 30-day sales array into a 6x5 matrix (6 weeks x 5 working days). 
# Calculate the total sales of each week (use axis). 
# sales_matrix = sales.reshape(6,5)
# print(sales_matrix)

# weekly_sales = np.sum(sales_matrix, axis=1)
# print("Weekly sales:", weekly_sales)

# Task 18. From the same 6x5 matrix, find the average sales for each weekday column — which 
# weekday performs best?
# sales_matrix = sales.reshape(6,5)
# print(sales_matrix)

# weekday_avg = np.mean(sales_matrix, axis=0)
# print("weekday average:", weekday_avg)

# Final Deliverable 
# Prepare a short summary report (print statements) 
# showing : Total Revenue, Average Daily Sales, Best Day, Worst Day, Target Achievement Count, 
# Best Week, and Best Weekday. 
# Write one line of business advice for the store owner based on your analysis

# import numpy as np

# sales = np.random.randint(5000, 50001, 30)  
# print(sales)

# # Total Revenue
# Total_revenue = np.sum(sales)
# print("Total revenue is:", Total_revenue)

# # Average Daily Sales
# Avg_daily_sales = np.mean(sales)
# print("average daily sales is:", Avg_daily_sales)

# # Best Day
# best_day = np.argmax(sales)
# best_sales = sales[best_day]
# print("best day:", best_day+1)
# print("best sales:", best_sales)

# # worst day
# worst_day = np.argmin(sales)
# worst_sales = sales[worst_day]
# print("worst day:", worst_day+1)
# print("worst sales:", worst_sales)

# # Target achived
# labels = np.where(sales >= 30000, "Target Achived", "Target Missed")
# count = np.sum(sales >= 30000)
# print("Target achived days:", count)

# sales_matrix = sales.reshape(6,5)

# weekly_sales = np.sum(sales_matrix, axis=1)

# # Best Week
# best_week = np.argmax(weekly_sales)
# best_week_sales = weekly_sales[best_week]

# print("Best Week:", best_week + 1)
# print("Best Week Sales:", best_week_sales)

# # Average sales of each weekday
# weekday_average = np.mean(sales_matrix, axis=0)

# weekdays = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

# best_weekday = np.argmax(weekday_average)

# print("Best Weekday:", weekdays[best_weekday])
# print("Best Weekday Average Sales:", weekday_average[best_weekday])

# # Business Advice
# print("Business Advice: Focus on improving low-sales " \
# "days and repeat the strategies used on the best-performing week and weekday.")