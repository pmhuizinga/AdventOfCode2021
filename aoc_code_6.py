from general_functions import read_data
import numpy as np
import math


# %%
day = 6
data = read_data(day, test=False)
data = [int(x) for x in data[0].split(',')]


def lanternfish(lst, days):
    day = 0
    arr = np.array(lst)
    print('day: {}, arr: {}'.format(day, arr))
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
# nr_of_children = 0
#
# def calc_child(start_number: int, days: int, number_of_children: int = 0) -> int:
#     if start_number <= days:
#         days_remaining = days - start_number
#         number_of_children += (math.ceil(days_remaining / 7))
#         print(number_of_children)
#         if days_remaining >= 7:
#             return calc_child(8, days_remaining, number_of_children)
#         else:
#             return number_of_children
#
# print('result {}'.format(calc_child(start_num, period)))

# print(sum([(1+calc_child(x, 18, 0)) for x in [3]]))
# period - start_num = days_remaining
# checklist.append([start_number, days, number_of_children])
# print('startnum: {}, days_remaining: {}, nr_of_children: {}'.format(8, days_remaining, number_of_children))
#%%
# thanks to Pieter....
from collections import defaultdict

def count_days(max_day, initial_day):
    # make dict
    days = defaultdict(int)

    # the first new fish is on:
    days[initial_day + 1] = 1

    # for every day:
    for day in range(max_day + 1):
        # if day value > zero: add 1 to 9 days ahead & add 1 to 7 days ahead. this value will be part of the
        # same loop later.
        if days[day] > 0:
            n = days[day]
            days[day + 9] += n
            days[day + 7] += n

    # result is the total until the max day (can't use values directly as it also has days after max day)
    # this is because of the +9/+7.

    total = 1
    # sum all values in the dictionary
    for day in range(max_day + 1):
        total += days[day]
    return total

print(sum([count_days(256, x) for x in data]))