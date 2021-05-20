'''
You are in charge of the cake for a child's birthday.
You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
'''


# need to find the sum of the tallest candle 
# going to solve with one iteration
# greatest value found onto the stack and push repeated value, if bigger number is found then clear stack and push greater value 
def birthdayCandles(candles):
    stack = []
    stack.append(candles[0])
    for candle in range(1,len(candles)): 
        if stack[0] < candles[candle]:
            stack.clear()
            stack.append(candles[candle])
        elif candles[candle] == stack[0]:
            stack.append(candles[candle])
    return len(stack)

def main(): 
    candles = [3,2,1,3]
    print(birthdayCandles(candles))

main()