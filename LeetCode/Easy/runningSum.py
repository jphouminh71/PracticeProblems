'''
Given an array nums. 
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

ex. 
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''
from typing import List

# O(n^2) runtime
def runningSum(nums: List[int]) -> List[int]: 
    size = len(nums)
    summed = []
    for i in range(0,size): 
        runner = nums[i]
        for prev in range(0,i):
            runner += nums[prev]
        summed.append(runner)
    print("SUM1:", summed)

# O(n) , but still slow because using built in functions
def runningSum2(nums: List[int]) -> List[int]:
    size = len(nums) 
    summed = []

    for index in range(0,size):
        slice = nums[:index]
        summed.append(sum(nums[0:index+1]))
    print("SUM2:",summed)


# O(n) , fastest and no additional memory
def runningSum3(nums: List[int]) -> List[int]:
    size = len(nums) 
    sum = 0

    for index in range(0,size):
        sum += nums[index]
        nums[index] = sum
    print("SUM3:",nums)

def main(): 
    nums = [1,2,3,4]  # [1,3,6,10]
    nums2 = [3,1,2,10,1] # [3,4,6,16,17]

    runningSum(nums)
    runningSum2(nums)
    runningSum3(nums)

main()