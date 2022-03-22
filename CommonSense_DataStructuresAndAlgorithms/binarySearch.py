'''
    Binary Search Algorithm 
        - O(log(n)) runtime 
        - Can be used to search through any ordered set of values 

    We will not see the real benefits of binary search until we find a scenario with a LOT of data 
    compared to linear search because of how they both scale to infinity! 

    Tip: If you ever need to sift through data and you know its ordered know that you have the binary search algorithm in your toolbox 
    to be able to find elements in logarithmic time 
'''
import time
from datetime import timedelta

def binarySearch(nums: [int], target: int) -> bool:     
    if (len(nums) == 1):
        return nums[0] == target

    midpoint = (len(nums)) // 2
    value = nums[midpoint]

    if value == target: 
        return True
    if target < value: 
        return binarySearch(nums[:midpoint], target)
    else: 
        return binarySearch(nums[midpoint:], target)

def linearSearch(nums: [int], target: int) -> bool: 
    result = False 
    for num in nums: 
        if num == target:
            result = True
            break 
    return result 


def runTests(nums: [int], target: int, method) -> bool: 
    startTime = time.time() 
    result = method(nums, target)
    endTime = time.time()

    if result == True: 
        print(f"***PASSED*** [{len(nums)} elements][{timedelta(seconds = endTime - startTime)} seconds]")
    else:
        print("***FAILED***")
        print("result: ", result)
        print("arr: ", nums, " target: ", target)

def main(): 
    testCase1 = [1,2,3,4,5]
    testCase2 = [1,10,40,200]
    testCase3 = [1,2,3]
    testCase4 = [1,2,3,4]
    testCase5 = []
    for i in range(20001):    
        testCase5.append(i)

    target1 = 5
    target2 = 200 
    target3 = 3 
    target4 = 4
    target5 = 20000

    tests = [testCase1, testCase2, testCase3, testCase4, testCase5]
    targets = [target1, target2, target3, target4, target5]

    print("binary search")
    for i in range(len(targets)):
        runTests(tests[i], targets[i], binarySearch)
    print("linear search")
    for i in range(len(targets)):
        runTests(tests[i], targets[i], linearSearch)

main()