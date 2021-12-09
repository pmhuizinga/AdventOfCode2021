from general_functions import read_data
import numpy as np

day = 7
data = read_data(day, test=True)
data = [int(x) for x in data[0].split(',')]
#%%

max_pos = max(data)
min_pos = min(data)
avg_pos = np.mean(data)

