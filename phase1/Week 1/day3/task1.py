'''
1.Use NumPy to generate 100 random numbers (normal distribution). Plot:

Histogram (Matplotlib)

KDE Plot (Seaborn).
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

#  generate 100 random numbers

random_numbers = np.random.randn(100)
print(random_numbers)

# plot histogram

plt.hist(random_numbers, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Random Numbers')
plt.show()

# plot kde plot
sns.kdeplot(random_numbers, color='orange')
plt.title('KDE Plot of Random Numbers')
plt.show()