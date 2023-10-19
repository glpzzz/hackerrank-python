#!/bin/python3

import numpy

if __name__ == '__main__':
    
    N = int(input())
    A = [list(map(float, input().split(" "))) for _ in range(N)]
    
    print(round(numpy.linalg.det(A), 2))

