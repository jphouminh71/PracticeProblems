'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
'''

# for each number you encounter, search to see how many more you have ahead of you to determine how many swaps you need? then swap? then move on? 

def swap(arr, i, j): 
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 

def bubbleUp(arr, index, end):
    for i in range(index,end):
        swap(arr,i, i+1)

# return the k'th position of last sorted item. 
def removeDuplicates(nums):
    if len(nums) <= 0: 
        return 0 
    i = 0
    k: int = len(nums)
    while i < k:
        if nums[i-1] == nums[i]:
            bubbleUp(nums,i,k-1)
            k-=1
            i = i - 1
        i+=1

    # means we kept swapping all the way     
    if k <= 0: 
        return 1
    return k

def testSuite(): 
    print("Running tests...")
    # elements sorted in increasing order 
    case0 = []
    case1 = [1,1,2]
    case2 = [0,0,1,1,1,2,2,3,3,4]
    case3 = [1,2]  
    case4 = [1,1,1,1]
    case5 = [1,2,2]

    


    # order of shifted elements do not matter 
    sol0 = []
    sol1 = [1,2,1]
    sol2 = [0,1,2,3,4,1,1,2,3,0] 
    sol3 = [1,2]
    sol4 = [1,1,1,1] # k = 1
    sol5 = [1,2,2]

    tests = [case0, case1, case2, case3, case4, case5]
    sols =  [sol0, sol1, sol2, sol3, sol4, sol5]

    # going to verify by hand because testing this annoying
    for i in range(0,len(tests)): 
        k = removeDuplicates(tests[i])
        print("k'th index: ", k)
        print("result:   ", tests[i])
        print("solution: ", sols[i])
        print("sortedPortion: ", tests[i][:k])
        print()


def main(): 
    testSuite()    
main()