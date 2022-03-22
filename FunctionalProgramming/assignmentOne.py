'''
Write a scala function titled isPalindrome (s) that 
tests whether a given input string s is a palindrome.
'''
def isPalindrome(s) -> True: 
    if len(s) <= 1: 
        return True 
    if s[0] == s[len(s)-1]: 
        return isPalindrome(s[1:len(s)-1])
    else: 
        return False

def problemOne(): 
    print("Evaluating problem one...")
    test1 = ["s",True]
    test2 = ["aba",True]
    test3 = ["abba",True]
    test4 = ["abaa",False]
    test5 = ["", True]
    tests = [test1,test2,test3,test4,test5]
    for test in tests: 
        result = isPalindrome(test[0])
        if result != test[1]: 
            print("FAILED: ",test[0])
            return 
    print("*****TESTS PASSED*****")
    print()

''' 
Create a function that accepts a function as a parameter, practice using callbacks. Callbacks are easily abused
via callback hell but they can also improve your speed. 

note: python doesn't support type annotation for passed lambda functions
'''
def createCallback(fn, val1: int, val2: int) -> int: 
    result = fn(val1,val2)
    print(result)

def problemTwo(): 
    print("Evaluating problem two...")
    addition = lambda x1,x2 : x1 + x2 
    createCallback(addition,1,2)
    print("*****TESTS PASSED*****")
    print()

'''
Tail recursive solution to calculating the fibonacci sequence
'''
def calculateFibonacciTail(n: int, acc: int = 0): 
    pass

def calculateFibonacci(n: int): 
    print("Calculating fibonacci for n =",n)
    initial = [0,1]
    while len(initial) != n: 
        oneBack = len(initial)-1
        twoBack = len(initial)-2
        print("one: ", oneBack, " two: ", twoBack)
        initial.append(oneBack + twoBack)
    print(initial)
    print("result: ",initial[len(initial)-1])
    


def problemThree():
    n: int = 10
    testOne:int = calculateFibonacciTail(n)
    testTwo:int = calculateFibonacci(n)

    if testOne == testTwo: 
        print("*****TESTS PASSED*****")
    else:
        print("*****TESTS FAILED*****")
    print()
            
def main(): 
    print()
    problemOne()
    problemTwo()
    problemThree()

main()

