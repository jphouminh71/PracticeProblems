'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.
'''
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# need to detach the next node if you add it to the new list 
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    mergedList: ListNode = None 
    tail: ListNode = None
    curr1: ListNode = l1
    curr2: ListNode = l2 

    # if both are empty
    if l1 == None and l2 == None: 
        return mergedList
    
    # if one is empty
    if l1 == None: 
        return curr2
    if l2 == None: 
        return curr1
    # assign the head of the list 
    if l1.val <= l2.val: 
        mergedList = l1 
        curr1 = l1.next
    else: 
        mergedList = l2
        curr2 = l2.next 
    tail = mergedList

    # go through the rest of the lists and assign accordingly to the new linked list head 
    while(curr1 and curr2): 
        if curr1.val <= curr2.val:
            tail.next = curr1 
            curr1 = curr1.next
        else: 
            tail.next = curr2 
            curr2 = curr2.next
        tail = tail.next 

    # empty out the list that remains
    while (curr1):
        tail.next = curr1
        tail = tail.next 
        curr1 = curr1.next 
    while (curr2):
        tail.next = curr2
        tail = tail.next
        curr2 = curr2.next 
    return mergedList
    
def main(): 
    arr = [1,2,5]
    arr2 = [1,3,4]

    # creating the lists
    x1: ListNode = ListNode(arr[0], ListNode(arr[1],ListNode(arr[2])))
    x2: ListNode = ListNode(arr2[0], ListNode(arr2[1],ListNode(arr2[2])))
    merged = mergeTwoLists(ListNode(1),None)
    
    temp = merged
    while (temp):
        print(temp.val)
        temp = temp.next
main()