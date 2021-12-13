from general_functions import read_data
import numpy as np

day = 8
data = read_data(day, test=True)
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

count 2 = 1
count 3 = 7
count 4 = 4
count 7 = 8
'''

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
def count_digits(data):
    counter = 0
    countlist = [2, 4, 3, 7]
    for entry in data:
        codes = entry[1].split(' ')
        # step one: get the easy digits
        for idx, digit in enumerate(codes):
            if len(digit) == 2:

                print('digit is 1')
            elif len(digit) == 4:
                print('digit is 4')
            elif len(digit) == 3 :
                print('digit is 7')
            elif len(digit) == 7:
                print('digit is 8')
            elif len(digit) == 6:
                for char in digit.split():
                    'als er maar 1 waarde van de digit in 1 zit dan is het zes'


count_digits(data)