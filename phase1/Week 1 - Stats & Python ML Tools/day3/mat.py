import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Line plot
plt.plot(x, y, label="Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.legend()
plt.show()

# Bar plot
plt.bar(x, y, color="orange")
plt.title("Bar Chart")
plt.show()

# Scatter plot
plt.scatter(x, y, color="green")
plt.title("Scatter Plot")
plt.show()
