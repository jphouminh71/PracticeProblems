'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Ex.
input: 07:05:45PM
output: 19:05:45


this one was very annoying. brain might just be slow rn. 
'''

# strip the last two chars to determine time of day
# seems like you would only need to adjust the hour hand once you determine time of day. 
# if AM then leave it the same
# if PM then add 12 
def timeConversion(s):
    timeOfDay = s[len(s)-2:]
    hours = int(s[:2]) 
    remaining = s[2:len(s)-2]

    if timeOfDay == "AM": 
        # midnight
        if hours == 12 and int(remaining[4:]) == 0:
            return "00:00:00"
        else: 
            if hours == 12:
                return "00" + remaining 
            return "0"+str(hours)+remaining
    elif timeOfDay == "PM": 
        if hours < 12:
            return str(hours + 12) + remaining
        else: 
            return str(hours) + remaining 

def main(): 
    ex_one = "07:05:45PM"   # 19:05:45
    ex_two = "12:40:22AM"   # 00:40:22 
    ex_three = "06:40:03AM" # 06:40:03
    ex_four = "12:45:54PM"  # 12:45:54
    ex_five = "12:00:00AM"  # 00:00:00

    test = ex_five
    t = timeConversion(test)
    print(t)


main()