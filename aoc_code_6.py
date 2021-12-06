from general_functions import read_data
import numpy as np

day = 6
data = read_data(day, test=False)
data = [int(x) for x in data[0].split(',')]

def lanternfish(lst, days):

    arr = np.array(lst)
    while days > 0:
        for idx in range(len(arr)):
            if arr[idx] == 0:
                arr[idx] = 7
                arr = np.append(arr, 9)

        arr = arr - 1
        days -= 1
        print(days)

    return list(arr)

result = lanternfish(data, 80)
print(len(result))
