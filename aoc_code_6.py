from general_functions import read_data
import numpy as np
import math

# %%
start_val = [3]
days = 19
freq = 7
start_day = 8
global nr_of_offspring


def test(start_val, days, freq, start_day):
    print(days - start_val)
    if (days - start_val) > freq:
        nr_of_offspring = math.floor((days - start_val) / freq)

    return nr_of_offspring


print(test(start_val[0], days, freq, start_day))

# %%
day = 6
data = read_data(day, test=True)
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
period = 30
print('6a:')
result = lanternfish([start_num], period)
print('result for 6a: {}'.format(len(result)))

# %%
nr_of_children = 0

def calc_child(start_number: int, days: int, number_of_children: int = 0) -> int:
    if start_number <= days:
        days_remaining = days - start_number
        number_of_children += (math.ceil(days_remaining / 7))
        print(number_of_children)
        if days_remaining >= 7:
            return calc_child(8, days_remaining, number_of_children)
        else:
            return number_of_children
    # else:
    #     return number_of_children


print('result {}'.format(calc_child(start_num, period)))

# print(sum([(1+calc_child(x, 18, 0)) for x in [3]]))
# period - start_num = days_remaining
# checklist.append([start_number, days, number_of_children])
# print('startnum: {}, days_remaining: {}, nr_of_children: {}'.format(8, days_remaining, number_of_children))
# %%
