#!/bin/python3

import numpy

if __name__ == '__main__':
    N,M = map(int, input().split(" "))
    
    A = numpy.zeros((N,M), dtype=int)
    for n in range(0,N):
        A[n] = list(map(int, input().split(" ")))
        
    B = numpy.zeros((N,M), dtype=int)
    for n in range(0,N):
        B[n] = list(map(int, input().split(" ")))
        
    print((A+B))
    print((A-B))
    print((A*B))
    print((A//B))
    print((A%B))
    print((A**B))
