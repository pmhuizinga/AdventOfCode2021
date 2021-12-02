from general_functions import read_data

day = 2
data = read_data(day, test=False)
data = [(x.split(' ')) for x in data]

# part 1
horizontal_position = 0
vertical_position = 0

for movement in data:
    if movement[0] == 'forward':
        horizontal_position += int(movement[1])
    elif movement[0] == 'up':
        vertical_position -= int(movement[1])
    elif movement[0] == 'down':
        vertical_position += int(movement[1])

print(horizontal_position * vertical_position)

# part 2
horizontal_position = 0
vertical_position = 0
aim = 0

for movement in data:
    if movement[0] == 'forward':
        horizontal_position += int(movement[1])
        vertical_position += aim * int(movement[1])
    elif movement[0] == 'up':
        aim -= int(movement[1])
    elif movement[0] == 'down':
        aim += int(movement[1])

print(horizontal_position * vertical_position)
