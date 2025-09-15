import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 22],
    "Score": [85, 90, 78, 88, 95]
}
df = pd.DataFrame(data)

# Histogram
sns.histplot(df["Score"], kde=True)
plt.title("Score Distribution")
plt.show()

# Boxplot
sns.boxplot(x=df["Score"])
plt.title("Score Boxplot")
plt.show()

# Scatter plot with regression line
sns.regplot(x="Age", y="Score", data=df)
plt.title("Age vs Score")
plt.show()

# Heatmap (correlation)
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
