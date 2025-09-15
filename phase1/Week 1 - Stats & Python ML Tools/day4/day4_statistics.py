# Day 4: Mean, Median, Mode, Variance, Standard Deviation
# -------------------------------------------------------
# In this tutorial, we will explore basic statistical concepts
# using Python, NumPy, and Pandas.
# These are the building blocks of Machine Learning.

import numpy as np
import pandas as pd
from statistics import mean, median, mode

# -----------------------------
# 1. Dataset (Simple Example)
# -----------------------------
data = [10, 20, 20, 30, 40, 50, 60]

print("Dataset:", data)

# -----------------------------
# 2. Mean (Average)
# -----------------------------
# Formula: sum of values / number of values
mean_value = mean(data)
print("\nMean (Average):", mean_value)

# -----------------------------
# 3. Median (Middle value)
# -----------------------------
# If odd count → middle element
# If even count → avg of two middle elements
median_value = median(data)
print("Median:", median_value)

# -----------------------------
# 4. Mode (Most frequent value)
# -----------------------------
mode_value = mode(data)
print("Mode:", mode_value)

# -----------------------------
# 5. Variance
# -----------------------------
# Formula: Average of squared differences from the Mean
np_variance = np.var(data)
print("Variance (NumPy):", np_variance)

# -----------------------------
# 6. Standard Deviation
# -----------------------------
# Formula: sqrt(Variance)
np_std = np.std(data)
print("Standard Deviation (NumPy):", np_std)

# -----------------------------
# 7. Using Pandas for Quick Stats
# -----------------------------
df = pd.DataFrame(data, columns=["Values"])
print("\nPandas Describe:\n", df.describe())
