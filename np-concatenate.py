#!/bin/python3

import numpy

if __name__ == '__main__':
    
    N, M, P = list(map(int, input().split(" ")))
    
    A = [list(map(int, input().split(" "))) for _ in range(N)]
    B = [list(map(int, input().split(" "))) for _ in range(M)]
    
    print(numpy.concatenate((A, B)))
