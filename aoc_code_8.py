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
'''
