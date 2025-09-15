import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the DataFrame
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Math": [85, 90, 78, 88, 95],
    "Science": [88, 92, 76, 89, 91],
    "English": [88, 92, 76, 89, 91]
}

df = pd.DataFrame(data)

# Print the DataFrame to verify
print("Student Scores DataFrame:")
print(df)

# --- Boxplot of Scores ---
# Select only the numerical score columns for the boxplot
scores_df = df[["Math", "Science", "English"]]

# Plot the boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(scores_df.values, labels=scores_df.columns)
plt.title("Boxplot of Student Scores")
plt.ylabel("Scores")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# --- Heatmap of Correlations ---
# Calculate the correlation matrix
correlation_matrix = scores_df.corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=.5, linecolor='black')
plt.title("Correlation Heatmap of Student Scores")
plt.show()
