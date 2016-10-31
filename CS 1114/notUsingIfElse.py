def checkStudentProgress(grade):
    if isPassing(grade):
        pass
    else:
        dealWithFailingGrade(grade)

def isPassing(grade):
    '''returns True if student grade is at least 65 and False if not'''
    '''
    if grade >= 65:
        return True
    else:
        return False
    '''
    return grade >= 65 #Don't need the return true or false anymore

    #or

    passing = grade >= 65
    return passing
 
