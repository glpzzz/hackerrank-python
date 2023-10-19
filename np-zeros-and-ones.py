#!/bin/python3

import numpy

if __name__ == '__main__':
    
    user_input = list(map(int, input().split()))
    print(numpy.zeros(user_input, dtype=int))
    print(numpy.ones(user_input, dtype=int))
