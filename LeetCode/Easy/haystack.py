
'''
    Try to use a stack here? Push a character onto a stack if it matches each 
    pattern character consequatively and pop all if they don't match
'''

class Stackey(object):
    def __init__(self, cap):
        self.stack = []
        self.cap = cap

    def push(self,c):
        self.stack.append(c)
        if (len(self.stack) == self.cap):
            return self.isFull()

    def popAll(self):
        size = len(self.stack)
        for i in range(0,size):
            self.stack.pop()

    # If this triggers then we found the needle
    def isFull(self): 
        print("FULL: ", self.stack)
        return True

    # need to return the index of the first occurrance of the needle
    # backtrace the size of the stack of the haystack and return that integer
    def getSize(self):
        return len(self.stack)



# Going to push values onto the stack 
def solution(haystack, pattern):
    # catch edge cases
    if pattern == "":
        return 0
    elif len(pattern) > len(haystack):
        return -1

    # init stack 
    stack = Stackey(len(pattern))

    index = 0     # index to keep track of which character to match in pattern
    indexOfHaystack = 0
    found = False
    size = len(haystack)

    
    # maybe change this too a while loop so you can have a scanning index that can go back and forth
    for i in range(0,size):
        char = haystack[i]
        if (char == pattern[index]):
            index+=1
            indexOfHaystack += 1
            isFull = stack.push(char)
            if (isFull):
                found = True
                break
            continue
        index = 0
        indexOfHaystack += 1
        stack.popAll()
        
        
    
    # stack should be filled with the needle at this point
    if found == True:
        print("FOUND")
        print("Str: ", haystack)
        print("Pat: ", pattern)
        firstOccurance = indexOfHaystack - index
        print(firstOccurance)
        return firstOccurance
        
    if found == False:
        print("NOT FOUND")
        print("Str: ", haystack)
        print("Pat: ", pattern)
        print(stack.stack)
        return -1



# if you can't figure out your other solution then just do the slicing approach 


def main(): 
    #Input: haystack = "hello", needle = "ll"
    #Output: 2
    haystack = "hello"
    needle = "ll"

    #Input: haystack = "aaaaa", needle = "bba"
    #Output: -1
    haystack2 = "aaaaa"
    needle2 = "bba"

    haystack3 = "mississippi"
    needle3 = "issip"


    solution(haystack, needle)
main()