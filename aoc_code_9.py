from general_functions import read_data
import numpy as np

day = 9
data = read_data(day, test=False)
data = np.array([[int(y) for y in x] for x in data])
rows = data.shape[0]
cols = data.shape[1]

# check if the value to the left is lower
check_left = data[:, 1:] < data[:, :-1]
check_left = np.c_[np.ones(rows), check_left]
# check if the value to the right is lower
check_right = data[:, :-1] < data[:, 1:]
check_right = np.c_[check_right, np.ones(rows)]
# check if the value to the top is lower
check_top = data[1:, :] < data[:-1, :]
check_top = np.r_[[np.ones(cols)], check_top]
# check if the value to the bottom is lower
check_bottom = data[:-1, :] < data[1:, :]
check_bottom = np.r_[check_bottom, [np.ones(cols)]]

total_check = check_left * check_right * check_top * check_bottom

print(sum(sum((total_check * data)+total_check)))