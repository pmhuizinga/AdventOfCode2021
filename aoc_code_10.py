from general_functions import read_data
import numpy as np
from scipy.ndimage import measurements

day = 10
data = read_data(day, test=True)

for row in data:
    print(row)
