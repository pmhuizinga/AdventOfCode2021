from general_functions import read_data
import numpy as np

day = 8
data = read_data(day, test=False)
data = [x.split(' | ') for x in data]

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
'''

def count_digits(data):
    ones = 0
    fours = 0
    sevens = 0
    eights = 0
    for entry in data:
        codes = entry[1].split(' ')
        for digit in codes:
            length = len(digit)
            if length == 2:
                ones += 1
            elif length == 4:
                fours += 1
            elif length == 3:
                sevens += 1
            elif length == 7:
                eights += 1
    return ones, fours, sevens, eights

print(sum(count_digits(data)))