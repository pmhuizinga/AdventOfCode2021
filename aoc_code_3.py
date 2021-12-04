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

    return binval


gamma_rate = int(calculate_binary_value(most_common=True), 2)
epsilon_rate = int(calculate_binary_value(most_common=False), 2)
print('part 1')
print(gamma_rate * epsilon_rate)


# part 2
def get_rating(mc=True):

    def bin_to_int(arr):
        string = ''
        for val in list(arr[0]):
            string = string + str(val)
        return int(string, 2)

    arr_new = data

    for col in range(arr_new.shape[1]):
        if arr_new.shape[0] == 1:
            return bin_to_int(arr_new)

        most_common = int(math.ceil(np.median(arr_new[:, col])))
        if mc is False:
            if most_common == 1:
                most_common = 0
            else:
                most_common = 1

        arr_new = arr_new[arr_new[:, col] == most_common]

    return bin_to_int(arr_new)


oxi = get_rating(mc=True)
co2 = get_rating(mc=False)
print('part 2')
print(oxi * co2)

