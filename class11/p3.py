import numpy as np

# 1. Create a 1D NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2. Create a 2D NumPy array
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print("2D Array:")
print(arr2)

# 3. Perform element-wise operations
arr3 = arr1 * 2  # Multiply each element of arr1 by 2
print("Array after multiplication by 2:", arr3)

# 4. Array addition
arr4 = np.array([10, 20, 30, 40, 50])
arr5 = arr1 + arr4
print("Array after addition:", arr5)

# 5. Using NumPy built-in functions
# Finding the mean of arr1
mean_val = np.mean(arr1)
print("Mean of arr1:", mean_val)

# Finding the sum of arr2
sum_val = np.sum(arr2)
print("Sum of arr2:", sum_val)

# Reshaping arr2 to a 1D array
reshaped_arr = arr2.reshape(6)
print("Reshaped arr2:", reshaped_arr)

# Create an array of zeros
zeros_arr = np.zeros((3, 3))
print("Array of zeros:")
print(zeros_arr)

# Create an array of ones
ones_arr = np.ones((2, 4))
print("Array of ones:")
print(ones_arr)
