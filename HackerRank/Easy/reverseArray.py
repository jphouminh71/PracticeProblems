# Recursive Solution
# O(n) solution
def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

# arrays are all passed by reference
def reverseArray(arr,pos1,pos2):
    if ((pos2-pos1) < 1):
        return arr
    swap(arr,pos1,pos2)
    reverseArray(arr, pos1+1, pos2-1)

def main(): 
    arr = [8,1,2,3,4,9]
    arr2 = [1,2,3]
    arr3 = [1]
    arr4 = [1,4,3,2]

    test = arr4    
    reverseArray(test,0,len(test)-1)
    print("----")
    print("After reverse: ",test)

main()