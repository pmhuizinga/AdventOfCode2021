from general_functions import read_data
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

day = 7
data = read_data(day, test=False)
data = [int(x) for x in data[0].split(',')]


max_pos = max(data)
min_pos = min(data)
avg_pos = np.round(np.mean(data))

plt.plot(list(range(1, len(data)+1)), data, color='blue')
plt.axhline(avg_pos, color='red')
plt.show()

def calc_steps_a(lst, val):
    result = []
    for item in lst:
        result.append(abs(item - val))

    return [val, sum(result)]

a = min(np.array([calc_steps_a(data, x) for x in list(range(min_pos, max_pos+1))])[:,1])
print(a)

# part 2
def calc_steps_b(lst, val):
    result = []
    for item in lst:
        result.append(sum(list(range(1, abs(item-val)+1, 1))))

    return [val, sum(result)]

b = min(np.array([calc_steps_b(data, x) for x in list(range(min_pos, max_pos+1))])[:,1])
print(b)


