from general_functions import read_data

day = 1
data = read_data(day)
data = [int(x) for x in data]

print(sum([1 for i, j in zip(data[:-1], data[1:]) if i < j]))



