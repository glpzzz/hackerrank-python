#!/bin/python3

if __name__ == '__main__':
    def is_leap(year):
        leap = False
        
        if year % 4 == 0:
            leap = True
        
        if year % 100 == 0:
            leap = False
            
        if year % 400 == 0:
            leap = True
        
        return leap
    
    year = int(input())
    print(is_leap(year))
