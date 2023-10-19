#!/usr/bin/python3

import numpy

if __name__ == 'main':
    N,M = list(map(int, input().split(" ")))
    A = [list(map(int, input().split(" "))) for _ in range(N)]
    print(numpy.prod(numpy.sum(A, axis=0)))

