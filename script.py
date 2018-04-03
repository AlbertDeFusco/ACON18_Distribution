#!/usr/bin/env python

# This script was developed with
#  python=2.7
#  numpy=1.10
#

import numpy as np

N = 11

numbers = np.random.randint(10, 100, size=N)
print 'An array of {n:d} random integers.'.format(n=N)
print numbers
print

middle = numbers[N/2]
print 'The middle value is {:d}'.format(middle)