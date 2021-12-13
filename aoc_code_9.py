from general_functions import read_data
import numpy as np
from scipy.ndimage import measurements

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

# part 2
# https://dragly.org/2013/03/25/working-with-percolation-clusters-in-python/
data[data < 9] = 1
data[data == 9] = 0
lw, num = measurements.label(data)
area = list(measurements.sum(data, lw, index=np.arange(lw.max() + 1)))
area.sort()
print(int(np.product(area[-3:])))