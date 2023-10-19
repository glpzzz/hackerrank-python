#!/bin/python3

import numpy

if __name__ == '__main__':
    
    N = int(input())
    A = [list(map(int, input().split(" "))) for _ in range(N)]
    B = [list(map(int, input().split(" "))) for _ in range(N)]
    
    print(numpy.dot(A,B))

