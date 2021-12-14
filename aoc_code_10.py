import numpy as np

from general_functions import read_data

day = 10
data = read_data(day, test=False)

open_bits = ['[', '{', '<', '(']
close_bits = [']', '}', '>', ')']
reward_1 = {None: 0, ')': 3, ']': 57, '}': 1197, '>': 25137}


def question_10_a(data):
    stack = []
    for char in data:
        if char in open_bits:
            stack.append(char)
        if char in close_bits:
            idx = close_bits.index(char)
            if open_bits[idx] == stack[-1]:
                stack.pop()
            else:
                return char


print(sum([reward_1[question_10_a(x)] for x in data]))

# part 2
reward_2 = {None: 0, ')': 1, ']': 2, '}': 3, '>': 4}
mapping = {'[': ']', '{': '}', '(': ')', '<': '>'}


def question_10_b(data):
    stack = []
    for char in data:
        if char in open_bits:
            stack.append(char)
        if char in close_bits:
            idx = close_bits.index(char)
            if open_bits[idx] == stack[-1]:
                stack.pop()
            else:
                return None
    return stack

out = [question_10_b(x) for x in data]
out = [[mapping[y] for y in x[::-1]] for x in out if x is not None]
print([x for x in out])

def total_score(list):
    score = 0
    for x in list:
        score = (score * 5) + reward_2[x]
    return score

print(np.median([total_score(x) for x in out]))