from general_functions import read_data

day = 10
data = read_data(day, test=True)

open_bits = ['[', '{', '<', '(']
close_bits = [']', '}', '>', ')']
reward = {None: 0, ')': 3, ']': 57, '}': 1197, '>': 25137}


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
    print(stack)

print(sum([reward[question_10_a(x)] for x in data]))

# part 2
reward = {None: 0, ')': 1, ']': 2, '}': 3, '>': 4}