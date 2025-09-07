'''
Create a Pandas DataFrame with:

Columns → Student, Math_Score, Science_Score.

Add 5 rows of fake data.

Filter students with Math_Score > 50.
'''

import pandas as pd

data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Math_Score": [85, 19, 78, 29, 48],
    "Science_Score": [88, 92, 76, 89, 91]
}
df = pd.DataFrame(data)
print(df["Math_Score"])
print(df[df["Math_Score"] > 50])
