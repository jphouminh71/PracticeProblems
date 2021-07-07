'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
'''

# brute force solution O(n) but O(n) space also 
# can always assume that the array will be even. 
def shuffle(arr, n): 
    shuffled = []
    for i in range(n): 
        shuffled.append(arr[i])
        shuffled.append(arr[n])
        n+=1
    return shuffled

def shuffleTwo(arr, n): 
    for i in range(n): 
        next=arr[i+1]
        arr[i+1]=arr[n] 
        arr[n]=next
        n+=1
    return arr 

def test(): 
    arr = [1,2,3,4,4,3,2,1]
    ans = [1,4,2,3,3,2,4,1]
    n = 4 
    
    result = shuffleTwo(arr,n)
    print("init:   ",arr)
    print("result: ",result)
    print("ans:    ", ans)
    if (result == ans): 
        print("corrent")
    

def main(): 
    test()

    

main()