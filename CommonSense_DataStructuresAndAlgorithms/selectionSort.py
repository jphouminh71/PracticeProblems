'''
    Simple sort algorithm that finds the lowest value in each iteration and places it in the last 
    index that it hasn't updated. Results in array being sorted in ascending order  

    Runtime analysis: O(n^2)
'''
import time
from datetime import timedelta

def selectionSort(nums:[int]) -> [int]:
    for i in range(len(nums)): 
        minIndex = i
        for j in range(i+1, len(nums)):             
            if nums[j] < nums[minIndex]: 
                minIndex = j
        swap(nums, i, minIndex)   
    return nums  


def swap(arr, indexOne, indexTwo): 
    temp = arr[indexOne]
    arr[indexOne] = arr[indexTwo] 
    arr[indexTwo] = temp 


def isSorted(nums:[int]) -> bool: 
    isSorted = True 
    for i in range(len(nums)-1): 
        if nums[i] > nums[i+1]:
            isSorted = False 
            break 
    return isSorted  
    

def runTests(nums: [int], method): 
    startTime = time.time() 
    result = method(nums)
    passed = isSorted(result)
    endTime = time.time()

    if passed == True : 
        print(f"***PASSED*** {result} [{timedelta(seconds = endTime - startTime)} seconds]")
    else:
        print(f"***FAILED*** {result}")

def startTests(tests): 
    print("selection sort")
    for test in tests: 
        runTests(test, selectionSort)
def testMethods(): 
    swapTest = [1,2,3]
    swap(swapTest, 0, 2)
    print(swapTest)


def main(): 
    testCase1 = [5,4,3,2,1]
    testCase2 = [11,2,33,4,544]
    testCase3 = [4,2,7,1,3]
    testCase4 = [4,2,7,1,3]
    tests = [testCase1, testCase2, testCase3, testCase4]

    runRealTest = True 
    if runRealTest:
        startTests(tests)    
    else: 
        testMethods() 
main()