# Compute and print the ratio for the amount of; positive, negative, and zero, in the set. 
# O(n) solution
def plusMinus(arr):
    pos = 0 
    neg = 0
    zero = 0
    for val in arr:
        if val == 0:
            zero+=1
        elif val > 0:
            pos+=1
        else:
            neg+=1
    size = len(arr)
    aa = pos / size 
    bb = neg / size 
    zz = zero / size 
    print("%.6f"%aa)
    print("%.6f"%bb)
    print("%.6f"%zz)


def main():
    arr = [1,1,0,-1,-1]
    test = arr 
    plusMinus(test)

main()