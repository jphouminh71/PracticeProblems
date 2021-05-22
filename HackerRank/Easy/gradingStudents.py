'''
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from 0 to 100.
Any grade less than 38 is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3 ,round  up to the next multiple of 5.
If the value of 38 is less than , no rounding occurs as the result will still be a failing grade.
'''

def gradeHelper(grade): 
    # automatic fail 
    if grade < 38: 
        return grade
    
    # determine next mult of 5 
    for i in range(0,3): 
        if ((grade + i) % 5) == 0:
            return grade + i
    return grade

# return a new array with all the grades completed
def gradingStudents(grades): 
    for i in range(0,len(grades)):
        grades[i] = gradeHelper(grades[i])
    return grades 


def main(): 
    # always between 0 - 100 
    test1 = 84  #85
    test2 = 29  #fail, less than 38
    test3 = 57  #difference to next multiple is >= 3

    cases = [test1,test2,test3] 
    result = gradingStudents(cases)
    print(result)
    

main()