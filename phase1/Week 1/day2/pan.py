import pandas as pd

# Series
s = pd.Series([10, 20, 30, 40], name="Scores")
print("Series:\n", s)

# DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 95]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Select column
print("\nAges:\n", df["Age"])

# Filter rows
print("\nAge > 28:\n", df[df["Age"] > 28])

# Summary statistics
print("\nSummary:\n", df.describe())
