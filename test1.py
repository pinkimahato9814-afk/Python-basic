import numpy as np
import statistics as st
import numpy as np
from statistics import mode

# sample data
data = [12, 15, 18, 21, 24, 24, 27, 30, 33, 36]

# convert to numpy array
arr = np.array(data)

# Mean
mean_value = np.mean(arr)

# Median
median_value = np.median(arr)

# Mode
mode_value = mode(arr)

# Quartiles
Q1 = np.percentile(arr, 25)
Q2 = np.percentile(arr, 50)
Q3 = np.percentile(arr, 75)

# Percentile example (90th percentile)
percentile_90 = np.percentile(arr, 90)

print("Data:", arr)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Quartile Q1:", Q1)
print("Quartile Q2:", Q2)
print("Quartile Q3:", Q3)
print("90th Percentile:", percentile_90)