#!/bin/python3

import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    line = tuple(map(int, input().split(" ")))
    print(numpy.eye(*line))

