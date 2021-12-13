from general_functions import read_data
import numpy as np

day = 8
data = read_data(day, test=False)
data = [x.split(' | ') for x in data]

def count_digits(data):
    counter = 0
    countlist = [2, 4, 3, 7]
    for entry in data:
        codes = entry[1].split(' ')
        for digit in codes:
            if len(digit) in countlist:
                counter += 1

    return counter

print(count_digits(data))

# part 2
'''
	a	b	c	d	e	f	g	count
0	1	1	1		1	1	1	6
1			1			1		2
2	1		1	1	1		1	5
3	1		1	1		1	1	5
4		1	1	1		1		4
5	1	1		1		1	1	5
6	1	1		1	1	1	1	6
7	1		1			1		3
8	1	1	1	1	1	1	1	7
9	1	1	1	1		1	1	6

count 2 = 1
count 3 = 7
count 4 = 4
count 7 = 8
'''
def count_digits(data):
    global one, entry_dict_2, four
    output2 = 0
    for entry in data:
        entry_dict = {}
        entry_dict_2 = {}
        codes = entry[0].split(' ')
        # step one: get the easy digits
        for idx, digit in enumerate(codes):
            if len(digit) == 2:
                entry_dict[idx] = 1
                one = digit
            elif len(digit) == 4:
                entry_dict[idx] = 4
                four = digit
            elif len(digit) == 3:
                entry_dict[idx] = 7
            elif len(digit) == 7:
                entry_dict[idx] = 8

        # step 2: get the digits with six and five characters. Match them with the 'easy digits'.
        for idx, digit in enumerate(codes):
            if len(digit) == 6:
                if sum([x in one for x in digit]) == 1:
                    entry_dict[idx] = 6
                elif sum([x in four for x in digit]) == 4:
                    entry_dict[idx] = 9
                else:
                    entry_dict[idx] = 0
            if len(digit) == 5:
                if sum([x in one for x in digit]) == 2:
                    entry_dict[idx] = 3
                elif sum([x in four for x in digit]) == 3:
                    entry_dict[idx] = 5
                else:
                    entry_dict[idx] = 2

        for idx, digit in enumerate(codes):
            entry_dict_2[''.join(sorted(digit))] = entry_dict[idx]

        output = ''
        test = entry[1].split(' ')
        for digit in test:
            output = output + str(entry_dict_2[''.join(sorted(digit))])

        output = int(output)
        output2 += output

    return output2

print(count_digits(data))