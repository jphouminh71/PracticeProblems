'''
    Simple sort algorithm that "bubbles" up the highest value in the array 
    through each iteration of the algorithm. Given array is considered sorted
     once a pass through has not needed to make a swap. 

    Runtime analysis: O(n^2)
'''
import time
from datetime import timedelta

def bubbleSort(nums:[int]) -> [int]:
    lastSortedIndex = len(nums)-1 # we do -1 here because we are looking one index ahead in the search 
    IsSorted = False 
    while (IsSorted == False):   # O(n) , initially 
        IsSorted = True 
        for i in range(lastSortedIndex):   # O(n), initially 
            if nums[i] > nums[i+1]:
                swap(nums, i, i+1)
                IsSorted = False
        lastSortedIndex -= 1
    return nums

def swap(arr, indexOne, indexTwo): 
    temp = arr[indexOne]
    arr[indexOne] = arr[indexTwo] 
    arr[indexTwo] = temp 


def isSorted(nums:[int]) -> bool: 
    isSorted = True 
    for i in range(len(nums)-2): 
        if nums[i] > nums[i+1]:
            isSorted = False 
            break 
    return isSorted  
    

def runTests(nums: [int]): 
    startTime = time.time() 
    result = bubbleSort(nums)
    passed = isSorted(result)
    endTime = time.time()

    if passed == True : 
        print(f"***PASSED*** {result} [{timedelta(seconds = endTime - startTime)} seconds]")
    else:
        print(f"***FAILED*** {result}")

def startTests(tests): 
    for test in tests: 
        runTests(test)

def testMethods(): 
    swapTest = [1,2,3]
    swap(swapTest, 0, 2)
    print(swapTest)


def main(): 
    testCase1 = [5,4,3,2,1]
    testCase2 = [11,2,33,4,544]
    testCase3 = [4,2,7,1,3]
    tests = [testCase1, testCase2, testCase3]

    runRealTest = True 
    if runRealTest:
        startTests(tests)    
    else: 
        testMethods() 
main()