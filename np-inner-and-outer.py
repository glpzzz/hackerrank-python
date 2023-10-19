#!/bin/python3

import numpy

if __name__ == '__main__':
    
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    
    print(numpy.inner(A,B))
    print(numpy.outer(A,B))
