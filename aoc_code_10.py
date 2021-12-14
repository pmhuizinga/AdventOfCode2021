from general_functions import read_data

day = 10
data = read_data(day, test=False)

open_bits = ['[', '{', '<', '(']
close_bits = [']', '}', '>', ')']
reward = {None: 0, ')': 3, ']': 57, '}': 1197, '>': 25137}
stack = []

def question_10_a(data):
    for char in data:
        if char in open_bits:
            stack.append(char)
        if char in close_bits:
            idx = close_bits.index(char)
            if open_bits[idx] == stack[-1]:
                stack.pop()
            else:
                return char

print(sum([reward[question_10_a(x)] for x in data]))

