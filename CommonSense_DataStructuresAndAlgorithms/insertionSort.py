'''
    InsertionSort 


    Runtime analysis: O(n^2)
'''
import time
from datetime import timedelta

def insertionSortTextbook(nums: [int]) -> [int]: 
    for index in range(1,len(nums)): 
        temp_value = nums[index]
        position = index - 1
        # shift all values greater than the one we are currently interested in up on unit 
        # until we find a value that is <= to it 
        while position >= 0: 
            # we found something that greater than the one we are comparing with 
            if nums[position] > temp_value:  
                nums[position+1] = nums[position]
                position -= 1
            else: 
                # we found something smaller 
                break  
        # we are at the correct position so we insert there 
        nums[position + 1] = temp_value
    return nums

def insertionSort(nums:[int]) -> [int]:
    for index in range(1, len(nums)): 
        valueToInsert = nums[index]
        lastShiftedIndex = index 
        for scanPosition in range(index-1,-1,-1):  
            if nums[scanPosition] > valueToInsert:  
                nums[scanPosition+1] = nums[scanPosition]
                lastShiftedIndex = scanPosition
            else: 
                break 
        nums[lastShiftedIndex] = valueToInsert
    return nums  

def isSorted(nums:[int]) -> bool: 
    isSorted = True 
    for i in range(len(nums)-1): 
        if nums[i] > nums[i+1]:
            isSorted = False 
            break 
    return isSorted  
    
def runTests(nums: [int], method): 
    copiedArray = nums[:]
    startTime = time.time() 
    result = method(copiedArray)
    passed = isSorted(result)
    endTime = time.time()

    if passed == True : 
        print(f"***PASSED*** {len(result)} sized array. [{timedelta(seconds = endTime - startTime)} seconds]")
    else:
        print(f"***FAILED*** {result}")


def startTests(tests): 
    print("Insertion Sort")
    for test in tests: 
        runTests(test, insertionSort)
    print() 
    print("Insertion Sort Textbook")
    for test in tests: 
        runTests(test, insertionSortTextbook)

def testMethods(): 
    for k in range(10,-1,-1):
        print(k)


def main(): 
    testCase1 = [5,4,3,2,1]
    testCase2 = [3,1,5]
    testCase3 = [4,2,7,1,3]
    testCase4 = [11,2,33,4,544,11,2,33,4,544,11,2,33,4,544,11,2,33,4,544,11,2,33,
                    4,544,11,2,33,4,544,11,2,33,4,544,11,2,33,4,544,11,2,33,4,544,
                        11,2,33,4,544,11,2,33,4,544,11,2,33,4,544]
    tests = [testCase1, testCase2, testCase3, testCase4]
    runRealTest = True 
    if runRealTest:
        startTests(tests)  
    else: 
        testMethods() 
main()