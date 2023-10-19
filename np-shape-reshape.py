#!/bin/python3

import numpy

if __name__ == '__main__':
    A = numpy.array(list(map(int, input().split(" "))))
    print(numpy.reshape(A, (3, 3)))


