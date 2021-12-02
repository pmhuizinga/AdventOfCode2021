from general_functions import read_data

day = 1
data = read_data(day, test=True)
data = [int(x) for x in data]


# part 1
def count_up(data):
    return sum(i < j for i, j in zip(data[:-1], data[1:]))


print(count_up(data))

# part 2
print(count_up([sum(data[i - 3:i]) for (i, x) in enumerate(data) if i < len(data) and i >= 2]))
