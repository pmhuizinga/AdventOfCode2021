from general_functions import read_data
import numpy as np
import math

day = 3
data = read_data(day, test=False)
data = [list(x) for x in data]
data = [[int(y) for y in x] for x in data]
data = np.array(data)


# part 1
def calculate_binary_value(most_common=True):
    binval = ''
    for col in range(data.shape[1]):
        if most_common:
            binval = binval + (str(int(np.round(np.sum(data[:, col]) / data.shape[0]))))
        else:
            binval = binval + (str(int(np.round(1 - np.sum(data[:, col]) / data.shape[0]))))

    return int(binval, 2)


gamma_rate = calculate_binary_value(most_common=True)
epsilon_rate = calculate_binary_value(most_common=False)
print('part 1')
print(gamma_rate * epsilon_rate)


# part 2
def get_rating(mc=True):
    arr_new = data

    for col in range(arr_new.shape[1]):
        if arr_new.shape[0] == 1:
            return int("".join(list([str(x) for x in arr_new[0]])), 2)

        most_common = int(math.ceil(np.median(arr_new[:, col])))

        if mc is False:
            most_common = 1 - most_common

        arr_new = arr_new[arr_new[:, col] == most_common]


oxi = get_rating(mc=True)
co2 = get_rating(mc=False)

print('part 2')
print(oxi * co2)
