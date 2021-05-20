'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
 Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example
    let a = [1,3,5,7,9]

    min: 1 + 3 + 5 + 7 = 16
    max: 3 + 5 + 7 + 9 = 24
'''


# brute force: build up all different sets then find the min and max sum 

import itertools
import sys

# this is actually bad because, itertools.combination has exponential time complexity yikes. 
def miniMax(arr): 
    minn = sys.maxsize
    maxx = 0 
    for subset in itertools.combinations(arr, 4):
        summy = sum(subset)
        if summy < minn: 
            minn = summy
        if summy > maxx: 
            maxx = summy 
    print(minn,maxx)


# alternative solution is to sort the array, take last 4 subset for max, take first 4 subset for the min! 
# O(nlogn)
def sol(arr): 
    arr.sort()
    front = arr[:4]
    back = arr[len(arr)-4:len(arr)]
    max = sum(back)
    min = sum(front)
    print(min,max)

def main(): 
    a = [7 ,69, 2, 221, 8974]
    miniMax(a)
    sol(a)

main()