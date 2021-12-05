from general_functions import read_data
import numpy as np

day = 5
data = read_data(day, test=False)

# part 1
data = [x.split(' -> ') for x in data]
data = [[y.split(',') for y in x] for x in data]
data = np.array([[[int(z) for z in y] for y in x] for x in data])

max_x = np.max(data[:, :, 0])
max_y = np.max(data[:, :, 1])
diagram = np.zeros([max_x+1, max_y+1], dtype=int)

# create arrays
for vector in data:
    # find verticals
    if vector[0, 0] == vector[1, 0]:
        y_positions = np.sort([vector[0, 1], vector[1, 1]])
        for ypos in range(y_positions[0], y_positions[1]+1):
            diagram[ypos, vector[0, 0]] += 1
    # find horizontals
    if vector[0, 1] == vector[1, 1]:
        x_positions = np.sort([vector[0, 0], vector[1, 0]])
        for xpos in range(x_positions[0], x_positions[1]+1):
            diagram[vector[1,1], xpos] += 1

result = (np.sum(np.where(diagram >= 2, 1, 0)))
print(result)