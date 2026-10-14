# Project 1 — E-Commerce Sales Analysis
# Dataset
import numpy as np

np.random.seed(10)

product = np.array([
    'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
    'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
    'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
    'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
])

category = np.array([
    'Electronics', 'Electronics', 'Electronics', 'Accessories',
    'Accessories', 'Accessories', 'Electronics', 'Office',
    'Wearable', 'Electronics', 'Accessories', 'Accessories',
    'Networking', 'Accessories', 'Accessories', 'Electronics',
    'Storage', 'Storage', 'Storage', 'Electronics'
])

price = np.random.randint(500, 80001, 20)
quantity = np.random.randint(1, 15, 20)
rating = np.random.randint(1, 6, 20)

# 📝 Project Tasks
# Basic Array Information

# Task 1. Display all five arrays with their shape, size, ndim, and dtype.
# print("Products is:", product)
# print("Category is:", category)
# print("price is:", price)
# print("Quantity is:", quantity)
# print("Rating is:", rating)

# print("--Array imformation--")

# print("Product -> shape:", product.shape, "Size:", product.size, 
#       "ndim:", product.ndim, "dtype:", product.dtype)
# print("category -> shape:", category.shape, "Size:", category.size, 
#       "ndim:", category.ndim, "dtype:", category.dtype)
# print("quantity -> shape:", quantity.shape, "Size:", quantity.size, "ndim:", 
#       quantity.ndim, "dtype:", quantity.dtype)
# print("Rating -> shape:", rating.shape, "Size:", rating.size, "ndim:", 
#       rating.ndim, "dtype:", rating.dtype)


# Task 2. Display itemsize and nbytes of the price array.
# price = np.random.randint(500, 80001, 20)
# print("price is:", price)
# print("itemsize:", price.itemsize, "nbytes:", price.nbytes)

# Task 3. Display complete details of the first product using index 0.
# print("Products is:", product[0])
# print("Category is:", category[0])
# print("price is:", price[0])
# print("Quantity is:", quantity[0])
# print("Rating is:", rating[0])

# Task 4. Display complete details of the last product using negative indexing.
# print("Products is:", product[-1])
# print("Category is:", category[-1])
# print("price is:", price[-1])
# print("Quantity is:", quantity[-1])
# print("Rating is:", rating[-1])

# Task 5. Display products from 5th to 12th position using slicing.
# print("product is:", product[5:13])

# Task 6. Display every alternate product using step slicing.
# print("product is:", product[0: 21: 2])

# Task 7. Display all products in reverse order using [::-1].
# print("Products is:", product[::-1])
# print("Category is:", category[::-1])
# print("price is:", price[::-1])
# print("Quantity is:", quantity[::-1])
# print("Rating is:", rating[::-1])

# 💰 Sales Analysis

# Task 8. Calculate the total quantity sold.
# Total_quantity = np.sum(quantity)
# print("Total quantity sold:", Total_quantity)

# Task 9. Calculate the average, maximum, and minimum product price.
# price = np.random.randint(500, 80001, 20)
# print("price is:", price)

# avg_price = np.mean(price)
# print("avg price is:", avg_price)

# Max_price = np.max(price)
# print("max price is:", Max_price)

# Min_price = np.min(price)
# print("Min price is:", Min_price)

# Task 10. Find the most expensive product using argmax() and display its name and price.
# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])

# price = np.random.randint(500, 80001, 20)

# index = np.argmax(price)

# print("product:", product[index])
# print("price:", price[index])

# Task 11. Find the cheapest product using argmin().
# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])

# price = np.random.randint(500, 80001, 20)

# index = np.argmin(price)

# print("product:", product[index])
# print("price:", price[index])

# Task 12. Find the product with the highest rating.
# rating = np.random.randint(1, 6, 20)
# highest_rating = np.max(rating)
# print("highest rating is:", highest_rating)

# Task 13. Find the product with the lowest rating.
# rating = np.random.randint(1, 6, 20)
# lowest_rating = np.min(rating)
# print("lowest rating is:", lowest_rating)

# 🔎 Boolean Indexing

# Task 14. Display names of products whose price is more than ₹50,000.
# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])

# price = np.random.randint(500, 80001, 20)

# result = product[price > 50000]
# print(result)

# Task 15. Count how many products have a price below ₹10,000.
# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])

# price = np.random.randint(500, 80001, 20)
# count = np.sum(price < 10000)
# print("Total products:", count)

# Task 16. Display products whose rating is between 3 and 5 using &.
# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])
# rating = np.random.randint(1, 6, 20)
# result = rating[(rating >= 3) & (rating <= 5)]
# print(result)


# Task 17. Display products whose price is below ₹5,000 OR above ₹60,000 using |.
# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])

# price = np.random.randint(500, 80001, 20)
# result = price[(price < 5000) | (price > 60000)]
# print(result)

# Task 18. Calculate:
# sales = price × quantity
# Then display products having sales value greater than ₹1,00,000.

# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])

# price = np.random.randint(500, 80001, 20)
# quantity = np.random.randint(1, 15, 20)

# sales = price * quantity

# result = product[sales > 100000]
# print("Products:", result)

# 🏷️ Category Analysis

# Task 19. Display names and prices of all Electronics products.
# category = np.array([
#     'Electronics', 'Electronics', 'Electronics', 'Accessories',
#     'Accessories', 'Accessories', 'Electronics', 'Office',
#     'Wearable', 'Electronics', 'Accessories', 'Accessories',
#     'Networking', 'Accessories', 'Accessories', 'Electronics',
#     'Storage', 'Storage', 'Storage', 'Electronics'
# ])
# price = np.random.randint(500, 80001, 20)
# result = category == "Electronics"

# print("Products:", product[result])
# print("Prices:", price[result])


# Task 20. Calculate the average price of Electronics products.
# category = np.array([
#     'Electronics', 'Electronics', 'Electronics', 'Accessories',
#     'Accessories', 'Accessories', 'Electronics', 'Office',
#     'Wearable', 'Electronics', 'Accessories', 'Accessories',
#     'Networking', 'Accessories', 'Accessories', 'Electronics',
#     'Storage', 'Storage', 'Storage', 'Electronics'
# ])
# price = np.random.randint(500, 80001, 20)
# result = category == "Electronics"

# print("Products:", product[result])
# print("Prices:", np.mean(price[result]))

# Task 21. Calculate the average price of:

# Electronics
# Accessories
# Storage
# Wearable
# Office

# using Boolean masks.

# category = np.array([
#     'Electronics', 'Electronics', 'Electronics', 'Accessories',
#     'Accessories', 'Accessories', 'Electronics', 'Office',
#     'Wearable', 'Electronics', 'Accessories', 'Accessories',
#     'Networking', 'Accessories', 'Accessories', 'Electronics',
#     'Storage', 'Storage', 'Storage', 'Electronics'
# ])
# price = np.random.randint(500, 80001, 20)
# result = category == "Electronics"
# print("Prices:", np.mean(price[result]))

# result = category == "Accessories"
# print("Prices:", np.mean(price[result]))

# result = category == "Storage"
# print("Prices:", np.mean(price[result]))

# result = category == "Wearable"
# print("Prices:", np.mean(price[result]))

# result = category == "Office"
# print("Prices:", np.mean(price[result]))

# Task 22. Find which category has the highest average price.
# categories = np.unique(category)

# averages = []

# for c in categories:
#     avg = np.mean(price[category == c])
#     averages.append(avg)

# index = np.argmax(averages)

# print("Highest Average Price Category:", categories[index])
# print("Average Price:", averages[index])

# Task 23. Count the number of products in each category.
# categories, count = np.unique(category, return_counts=True)
# for i in range(len(categories)):
#     print(categories[i], ":", count[i])

# Task 24. Display Accessories products having a rating greater than 3.
# result = (category == "Accessories") & (rating > 3)

# print("Products:", product[result])
# print("Ratings:", rating[result])


# 📦 Quantity Analysis

# Task 25. Display products where quantity sold is more than 8.
# result = product[quantity > 8]
# print(result)

# Task 26. Count products where quantity sold is less than 3.
# count = np.sum(quantity < 3)
# print(count)

# Task 27. Create a new price array after giving 10% discount to every product using broadcasting.
# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])
# price = np.random.randint(500, 80001, 20)
# print("price:", price)
# new_price = price * 0.90
# print("New price:", new_price)

# Task 28. Give an additional ₹1,000 discount to products whose original price is above ₹50,000 using
#  np.where().
# new_price = np.where(price > 50000, price - 1000, price)

# print("Original Price:", price)
# print("New Price:", new_price)

# Task 29. Minimum selling price rule:

# After discounts, if price is below ₹1,000, make it exactly ₹1,000.Use np.where().

# new_price = np.where(price < 1000, 1000, price)
# print("final price:", new_price)


# 📈 Profit / Sales Analysis

# Task 30. Calculate total sales before discount and after discount.
# import numpy as np

# # Apply ₹1,000 discount to products above ₹50,000
# discounted_price = np.where(price > 50000, price - 1000, price)

# # If price is below ₹1,000, make it ₹1,000
# final_price = np.where(discounted_price < 1000, 1000, discounted_price)

# # Sales before discount
# sales_before = price * quantity

# # Sales after discount
# sales_after = final_price * quantity

# # Total sales
# total_before = np.sum(sales_before)
# total_after = np.sum(sales_after)

# print("Original Price:", price)
# print("Final Price:", final_price)
# print("Sales Before Discount:", sales_before)
# print("Sales After Discount:", sales_after)

# print("Total Sales Before Discount:", total_before)
# print("Total Sales After Discount:", total_after)

# Task 31. Convert the final price array into integer type using:
# astype(int)
# price = np.random.randint(500, 80001, 20)
# final_price = price.astype(int)
# print("Final price:", final_price)

# Task 32. Sort final prices in ascending order and display the lowest 5 prices.
# price = np.random.randint(500, 80001, 20)
# sorted_price = np.sort(price)
# lowest_5 = sorted_price[:5]
# print("lowest price is:", lowest_5)

# 🥇 Ranking

# Task 33. Use argsort() to display product names from cheapest to most expensive.
# price = np.random.randint(500, 80001, 20)
# index = np.argsort(price)
# result = product[index]
# print("products from chepest to most expensive:", result)

# # Task 34. Display the Top 5 most expensive products using argsort() and [::-1].
# price = np.random.randint(500, 80001, 20)
# index = np.argsort(price)
# result = product[index[::-1][:5]]
# print("Top 5 most expensive products:", result)

# Task 35. Create product price bands using nested np.where():

# ₹50,000 or above → Premium
# ₹20,000–₹49,999 → Standard
# Below ₹20,000 → Budget

# Then count products in each band.
# price = np.random.randint(500, 80001, 20)
# print(price)
# result = np.where(price >= 50000, "Premium", 
#                   np.where(price >= 20000, "Standard", "Budget"))
# print(result)

# premium_count = np.sum(result == "Premium")
# standard_count = np.sum(result == "standard")
# budget_count = np.sum(result == "Budget")

# print("Premium:", premium_count)
# print("standard:", standard_count)
# print("budget:", budget_count)

# Task 36. Display names and categories of all Premium products.

# result = np.where(price >= 50000, "Premium", 
#                   np.where(price >= 20000, "Standard", "Budget"))
# print(result)

# premium_count = np.sum(result == "Premium")
# print("Premium:", premium_count)


# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])

# category = np.array([
#     'Electronics', 'Electronics', 'Electronics', 'Accessories',
#     'Accessories', 'Accessories', 'Electronics', 'Office',
#     'Wearable', 'Electronics', 'Accessories', 'Accessories',
#     'Networking', 'Accessories', 'Accessories', 'Electronics',
#     'Storage', 'Storage', 'Storage', 'Electronics'
# ])

# result = category == "Premium"
# print("premium products:", product[result])
# print("categories:", category[result])


# 📊 Reshaping & Combining

# Task 37. Create a new array:
# total_sales = price * quantity
# Then display each product with its total sales.

# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])
# price = np.random.randint(500, 80001, 20)
# quantity = np.random.randint(1, 15, 20)
# total_sales = price * quantity
# for i in range(len(product)):
#     print(product[i], ":", total_sales[i])


# Task 38. Combine:

# price
# quantity
# rating

# into a 3 × 20 matrix using vstack().
# Then transpose it so each row represents:
# [price, quantity, rating]
# Display the final matrix.

# price = np.random.randint(500, 80001, 20)
# quantity = np.random.randint(1, 15, 20)
# rating = np.random.randint(1, 6, 20)

# matrix = np.vstack((price, quantity, rating))
# final_matrix = matrix.T

# print("final matrix:", final_matrix)


# 🔄 Copy vs View

# Task 39.
# Create:

# copy_price = final_price.copy()
# Change the first value of copy_price to 0.
# Check whether the original final_price changed.

# price = np.random.randint(500, 80001, 20)
# copy_price = price.copy()
# copy_price[0] = 0

# print("original price:", price)
# print("copy_price is:", copy_price)

# print("original changed:", price[0]==0)

# Then repeat using:
# view_price = final_price.view()

# price = np.random.randint(500, 80001, 20)
# view_price = price.view()
# view_price[0] = 0

# print("original price:", price)
# print("copy_price is:", view_price)

# print("original changed:", price[0]==0)

# 🔍 Searching

# Task 40.

# Use np.where() to find the index of:

# 'Smartwatch'

# Then use that index to display its:

# Product
# Category
# Price
# Quantity
# Rating

# import numpy as np

# product = np.array([
#     'Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard',
#     'Mouse', 'Monitor', 'Printer', 'Smartwatch', 'Camera',
#     'Speaker', 'PowerBank', 'Router', 'Earbuds', 'Charger',
#     'Webcam', 'HardDisk', 'SSD', 'USB', 'Microphone'
# ])

# category = np.array([
#     'Electronics', 'Electronics', 'Electronics', 'Accessories',
#     'Accessories', 'Accessories', 'Electronics', 'Office',
#     'Wearable', 'Electronics', 'Accessories', 'Accessories',
#     'Networking', 'Accessories', 'Accessories', 'Electronics',
#     'Storage', 'Storage', 'Storage', 'Electronics'
# ])

# price = np.random.randint(500, 80001, 20)
# quantity = np.random.randint(1, 15, 20)
# rating = np.random.randint(1, 6, 20)

# # Find index of Smartwatch
# index = np.where(product == "Smartwatch")[0]

# # Display details
# print("Product:", product[index])
# print("Category:", category[index])
# print("Price:", price[index])
# print("Quantity:", quantity[index])
# print("Rating:", rating[index])