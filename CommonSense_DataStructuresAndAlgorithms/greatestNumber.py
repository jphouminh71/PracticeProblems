'''
    Chapter 4 excercise #4
    Find the the greatest value in the array in O(n) time

    note: range(len(arr)) is NOT inclusive. Ex if an arr is of size 5 then we are technically do 0...4 
'''

def greatestNumber(nums: [int]) -> int: 
    currMax = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > currMax:
            currMax = nums[i]
    print("returning: ", currMax)
    return currMax

def main(): 
    test = [1,4,52,4]
    result = greatestNumber(test)

    if result == max(test):
        print("***PASSED***")
    else: 
        print("***FAILED***")

main()