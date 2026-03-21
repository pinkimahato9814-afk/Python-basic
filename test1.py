# import numpy as np
# import statistics as st
# import numpy as np
# from statistics import mode

# # sample data
# data = [12, 15, 18, 21, 24, 24, 27, 30, 33, 36]

# # convert to numpy array
# arr = np.array(data)

# # Mean
# mean_value = np.mean(arr)

# # Median
# median_value = np.median(arr)

# # Mode
# mode_value = mode(arr)

# # Quartiles
# Q1 = np.percentile(arr, 25)
# Q2 = np.percentile(arr, 50)
# Q3 = np.percentile(arr, 75)

# # Percentile example (90th percentile)
# percentile_90 = np.percentile(arr, 90)

# print("Data:", arr)
# print("Mean:", mean_value)
# print("Median:", median_value)
# print("Mode:", mode_value)
# print("Quartile Q1:", Q1)
# print("Quartile Q2:", Q2)
# print("Quartile Q3:", Q3)
# print("90th Percentile:", percentile_90)


import hashlib
from difflib import SequenceMatcher


def hash_file(fileName1, fileName2):

    # Use hashlib to store the hash of a file
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(fileName1, "rb") as file:

        # Use file.read() to read the size of file
        # and read the file in small chunks
        # because we cannot read the large files.
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)
            
    with open(fileName2, "rb") as file:

        # Use file.read() to read the size of file a
        # and read the file in small chunks
        # because we cannot read the large files.
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

        # hexdigest() is of 160 bits
        return h1.hexdigest(), h2.hexdigest()


msg1, msg2 = hash_file("pd1.pdf ", "pd1.pdf")

if(msg1 != msg2):
    print("These files are not identical")
else:
    print("These files are identical")