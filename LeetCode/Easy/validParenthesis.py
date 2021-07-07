'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

# go through the string but build up two dictionaries? Then once they are both built check from outisde to in 
# [ (,{ ] [ }, )]   check them both at the same time working inwards    

def validParenthesis(s): 
    # trivial cases 
    if len(s) <= 1:
        return False 
    if len(s) % 2 != 0: 
        return False

    keys = [")", "}", "]"]
    opposites = {
        ")":"(", 
        "}":"{",
        "]":"[",
    }
    
    popped = 0 
    stack = []
    for char in s:
        # keep track of opening parenthesis 
        if char not in keys: 
            stack.append(char)
            continue
        # check to see if the closing parenthesis has corresponding opening
        if len(stack) > 0:
            popped += 1 
            matching = stack.pop()
            if matching != opposites[char]:
                return False 
            continue 
        # if we come here then it means that we got a closing parenthesis with no opening.
        return False 
    # stack must be empty 
    if len(stack) > 0 or ((popped * 2) < len(s) // 2) : 
        return False 
    return True 

def runTests(tests): 
    passed = True 
    for i in range(0, len(tests)):
            result = validParenthesis(tests[i][0])
            if result != tests[i][1]:
                print("Expecetd: ", tests[i][1])
                print("Got: ", result)
                print("FAILED: ", tests[i][0])
                passed = False 
    if passed: 
        print("TEST PASSED !")

def main(): 
    test1 = ["()",True]
    test2 = ["(()){}",True]
    test3 = ["(]",False]
    test4 = ["{",False]
    test5 = ["{[()]}",True]
    test6 = ["((", False]
    test7 = ["){", False]
    test8 = ["))", False]
    tests = [test1, test2, test3, test4,test5,test6, test7,test8]
    runTests(tests)
main()