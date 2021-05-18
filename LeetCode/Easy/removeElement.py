from typing import List


def swap(nums:List[int], pos1, pos2):
    temp = nums[pos1]
    nums[pos1] = nums[pos2]
    nums[pos2] = temp


def removeElement(nums: List[int], val: int) -> int:
    print("Value to Remove: ", val)
    print("Initial: ",nums)
    total = len(nums)

    for i in range(0,len(nums)):
        if (nums[i] == val):
            nums[i] = -1
            total = total - 1

    nums.sort()
    nums.reverse()
            
    
    print("Final: ",nums)
    print("Expected: [0,1,4,0,3]")
    print(total)
        

# this solution keeps track of the values to be filled while it goes through the rest of the array
# and when it finds a good one, it will replace the next value needed
def sol(nums: List[int], val: int) -> int:
    print(nums)
    length =0
    for i in range(0,len(nums)):
        if (nums[i] != val):
            nums[length] = nums[i]
            length += 1
    print(nums)
    return length


def main():

    test1 = [3,2,2,3]   # [2,2,3,3] or nums = [2,2,0,0] or [2,2]
    val1 = 3  

    test2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    sol(test2,val2)
main()