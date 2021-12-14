import numpy as np

from general_functions import read_data

day = 11
data = read_data(day, test=True)
arr = np.array([[int(y) for y in x] for x in data])


#
def update_step(arr):
    counter = 0
    # 1: add 1
    arr = arr + 1
    rows = arr.shape[0]
    cols = arr.shape[1]

    def update_surrounding(idx, idy):
        # first test with right
        arr[idx:idx+1, idy:idy+1] += 1
        # if idx == 0:
        #     if idy == 0:
        #         arr[0:2, 0:2] += 1
        #     else:
        #         arr[0:2, idy:idy+2] += 1
        # elif idx == cols:
        #     if idy == rows:
        #         arr[0:2, 0:2] += 1

    def flash(arr):
        for idx, x in enumerate(arr):
            for idy, y in enumerate(x):
                if arr[idx, idy] == 10:
                    update_surrounding(idx, idy)
                    # continue  # print(idx, idy)
        return arr

    # while arr.max() == 10:
    if arr.max() == 10:
        arr = flash(arr)
        count = np.count_nonzero(arr==11)

    return arr


b = update_step(arr)
c = update_step(b)
