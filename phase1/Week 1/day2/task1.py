'''
Create a NumPy array of 10 random numbers and calculate:

Mean, Median, Std Deviation.
'''

import numpy as np

random_numbers = np.random.rand(10)
print("Random Numbers:\n", random_numbers)

print("Mean:", random_numbers.mean())
print("Median:", np.median(random_numbers))
print("Std Dev:", random_numbers.std())
