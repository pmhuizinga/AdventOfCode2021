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
diagram = np.zeros([max_y + 1, max_x + 1], dtype=int)

# create arrays
for vector in data:
    # find verticals
    if vector[0, 0] == vector[1, 0]:
        y_positions = np.sort([vector[0, 1], vector[1, 1]])
        for y_pos in range(y_positions[0], y_positions[1] + 1):
            diagram[y_pos, vector[0, 0]] += 1
    # find horizontals
    if vector[0, 1] == vector[1, 1]:
        x_positions = np.sort([vector[0, 0], vector[1, 0]])
        for x_pos in range(x_positions[0], x_positions[1] + 1):
            diagram[vector[1, 1], x_pos] += 1

result = (np.sum(np.where(diagram >= 2, 1, 0)))
print(result)

# part 2
diagram = np.zeros([max_x + 1, max_y + 1], dtype=int)
for vector in data:

    if vector[0, 0] == vector[1, 0]:
        # find verticals
        y_positions = np.sort([vector[0, 1], vector[1, 1]])
        for y_pos in range(y_positions[0], y_positions[1] + 1):
            diagram[y_pos, vector[0, 0]] += 1

    elif vector[0, 1] == vector[1, 1]:
        # find horizontals
        x_positions = np.sort([vector[0, 0], vector[1, 0]])
        for x_pos in range(x_positions[0], x_positions[1] + 1):
            diagram[vector[1, 1], x_pos] += 1

    else:
        # find diagonals
        print(vector)
        if vector[1, 0] > vector[0, 0]:
            # x up
            if vector[1, 1] > vector[0, 1]:
                # y up
                print('1. top left to bottom right')
                x_up, y_up = 1, 1
                x_start = vector[0, 0]
                x_end = vector[1, 0] + 1
                y_start = vector[0, 1]
                y_end = vector[1, 1] + 1
            elif vector[1, 1] < vector[0, 1]:
                # y down
                print('2. bottom left to top right')
                x_up, y_up = -1, 1
                x_start = vector[1, 0]
                x_end = vector[0, 0] - 1
                y_start = vector[1, 1]
                y_end = vector[0, 1] + 1
        elif vector[1, 0] < vector[0, 0]:
            # x down
            if vector[1, 1] > vector[0, 1]:
                # y up
                print('3. top right to bottom right')
                x_up, y_up = -1, 1
                x_start = vector[0, 0]
                x_end = vector[1, 0] - 1
                y_start = vector[0, 1]
                y_end = vector[1, 1] + 1
            elif vector[1, 1] < vector[0, 1]:
                # y down
                print('4. bottom right to top left')
                x_up, y_up = -1, -1
                x_start = vector[0, 0]
                x_end = vector[1, 0] - 1
                y_start = vector[0, 1]
                y_end = vector[1, 1] - 1

        for x, y in zip(list(range(x_start, x_end, x_up)), list(range(y_start, y_end, y_up))):
            print(x, y)
            diagram[y, x] += 1

result = (np.sum(np.where(diagram >= 2, 1, 0)))
print(result)
