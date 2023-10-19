#!/bin/python3

import numpy

if __name__ == '__main__':
    N,M = list(map(int, input().split(" ")))
    A=[list(map(int, input().split(" "))) for _ in range(N)]
    
    print(numpy.mean(A, axis=1))
    print(numpy.var(A, axis=0))
    print(round(numpy.std(A), 11))
