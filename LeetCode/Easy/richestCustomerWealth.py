'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
'''
from typing import List

def maximumWealth(accounts: List[List[int]]) -> int: 
    max = -1
    for customer in accounts:
        if sum(customer) >= max: 
            max = sum(customer)
    return max 


def main():
    account1 = [[1,2,3],[3,2,1]]
    account2 = [[1,5],[7,3],[3,5]]

    ans1 = 6 
    ans2 = 10 

    test1 = maximumWealth(account1)
    test2 = maximumWealth(account2)

    if test1 == ans1: 
        print("test one passed")
    if test2 == ans2: 
        print("test two passed")

main()


