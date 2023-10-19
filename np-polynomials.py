#!/bin/python3

import numpy

if __name__ == '__main__':
    
    P = list(map(float, input().split(" ")))
    x = int(input())
    
    print(numpy.polyval(P, x))
