from general_functions import read_data
import numpy as np

day = 9
data = read_data(day, test=True)
data = np.array([[int(y) for y in x] for x in data])

# check if the value to the left is lower
check_left = data[:, 1:] < data[:, :-1]
# check if the value to the right is lower
check_right = data[:, :-1] < data[:, :-1]
