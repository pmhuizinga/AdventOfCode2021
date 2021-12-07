from general_functions import read_data
import numpy as np
import math

day = 6
data = read_data(day, test=True)
data = [int(x) for x in data[0].split(',')]


def lanternfish(lst, days):
    day = 0
    arr = np.array(lst)
    while days > 0:
        day += 1
        for idx in range(len(arr)):
            if arr[idx] == 0:
                arr[idx] = 7
                arr = np.append(arr, 9)

        arr = arr - 1
        days -= 1
        print('day: {}, arr: {}'.format(day, arr))

    return list(arr)

# %%
start_num = 3
period = 18
print('6a:')
result = lanternfish([start_num], period)
print('result for 6a: {}'.format(len(result)))

# %%
import math

nr_of_children = 0
checklist = []


def calc_child(start_num, period, nr_of_children):
    checklist.append([start_num, period, nr_of_children])
    if start_num <= period:
        days_after_first_birth = period - start_num
        nr_of_children += 1 + math.floor(days_after_first_birth / 7)
        if days_after_first_birth > 7:
            print('startnum: {}, days_after_first_birth: {}, nr_of_children: {}'.format(8,
                                                                                        days_after_first_birth,
                                                                                        nr_of_children))
            nr_of_children = calc_child(8, days_after_first_birth, nr_of_children)
            days_after_first_birth -= 7

    print(checklist)
    return nr_of_children

print(1 + calc_child(3, period, 0))
# print(sum([(1+calc_child(x, 18, 0)) for x in [3]]))


