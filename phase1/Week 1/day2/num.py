import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2D array (matrix)
mat = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", mat)

# Array operations
print("Mean:", arr.mean())
print("Std Dev:", arr.std())
print("Sum:", arr.sum())

# Random numbers
rand_arr = np.random.rand(3, 3)
print("Random Array:\n", rand_arr)
