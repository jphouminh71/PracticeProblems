# Construct a staircase full of hashtags
# O(n) solution
def staircase(n):
    hashCount = 1
    spaceCount = n - 1
    spaces = ""
    hash = "#"

    while spaceCount >= 0: 
        spaces = ""
        hash = ""
        spaces = (spaces + " ") * (spaceCount)
        hash = (hash + "#") * (hashCount)
        print(spaces + hash)
        spaceCount -= 1
        hashCount+=1
    


def main(): 
    n = 6
    staircase(n)
main()