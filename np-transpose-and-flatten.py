#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    N,M = list(map(int, input().split(" ")))
    A = [list(map(int, input().split(" "))) for _ in range(N)]

    print(numpy.transpose(numpy.array(A)))
    print(numpy.array(A).flatten())
