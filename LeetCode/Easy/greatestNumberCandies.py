'''
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the
greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
'''
from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = []
    maximum = max(candies)
    for i in range(0,len(candies)):
        amount = candies[i]
        needed = maximum - amount
        if needed <= extraCandies:
            result.append(True)
            continue
        result.append(False)
    return result 

# this is the way to do it with functional programming, its a lot faster too 
def kidsWithCandies2(candies: List[int], extraCandies: int) -> List[bool]:
    max_ = max(candies) - extraCandies
    return [x >= max_ for x in candies]

def main(): 
    extraCandies1 = 3 
    extraCandies2 = 1
    extraCandies3 = 10 
    test1 = [2,3,5,1,3]  # [true,true,true,false,true]
    test2 = [4,2,1,1,2]  # [false,false,false,false,false]
    test3 = [12,1,12]    # [True, False, True]
    test4 = [1,1,1]


    results = [
        [True,True,True,False,True],
        [False,False,False,False,False],
        [True,False,True]
    ]

    kidsWithCandies(test4, extraCandies2)



main()