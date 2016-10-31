#!/usr/bin/python/

'''
Programmer: Janina Soriano
Username: js7817

filename: hw00.py

This program prints twenty questions and answers relating to CS 1114

Constraints: None

Assumptions: None
'''

from __future__ import print_function
import os

def printQ1():
    '''Asks what the lecture professor's name is'''
    print("Q: What is your lecture professor's name?")

def printQ2():
    '''Asks what her office hours are'''
    print("Q: What are her office hours?")

def printQ3():
    '''Asks where her office is'''
    print("Q: Where is her office?")

def printQ4():
    '''Asks if laptops should always be brought to labs'''
    print("Q: Should you always bring your laptop to the lab?")

def printQ5():
    '''Asks for the dates and times of the midterms'''
    print("Q: What are the dates and times of the midterms?")

def printQ6():
    '''Asks which class period the midterms are given in'''
    print("Q: What class period are the midterms given?")

def printQ7():
    '''Asks what day and time the aforementioned class period is'''
    print("Q: What day and time is that?")

def printQ8():
    '''Asks the percentage of the final grade the midterms are'''
    print("Q: What percentage of your final grade do these count?")

def printQ9():
    '''Asks which class period the final exams are'''
    print("Q: What is the period during which final exams are given?")

def printQ10():
    '''Asks the percentage of the final grade the final exam is'''
    print("Q: What percentage of your final grade does the final exam count?")

def printQ11():
    '''Asks if not taking the final exams results in automatically failing the course'''
    print("Q: If you do not take the final exam will you automatically fail the course?")

def printQ12():
    '''Asks the percentage of the final grade the lectures are'''
    print("Q: What percentage of your final grade does your lecture attendance and participation count?")

def printQ13():
    '''Asks how lectures affect the letter grade'''
    print("Q: How does it affect your letter grade?")

def printQ14():
    '''Asks the percentage of the final grade the labs are'''
    print("Q: What percentage of your final grade do the labs count?")

def printQ15():
    '''Asks how the labs affect the letter grade'''
    print("Q: How does it affect your letter grade?")

def printQ16():
    '''Asks the minimum number of lectures attended needed to pass'''
    print("Q: What is the minimum number of lectures you must attend to pass this course?")

def printQ17():
    '''Asks the grade if the minimum number of lectures isn't met'''
    print("Q: If you do not meet that minimum number what grade will you get for the course?")

def printQ18():
    '''Asks the minimum lab score needed to pass'''
    print("Q: What is the minimum score in the labs you must attain to pass this course?")

def printQ19():
    '''Asks the grade if the minimum lab score isn't met'''
    print("Q: If you do not meet that minimum score what grade will you get for the course?")

def printQ20():
    '''Asks if emailed homework is accepted'''
    print("Q: Do we accept emailed homework?")

def printA1():
    '''Answers Professor Kletenik'''
    print("A: Professor Kletenik")

def printA2():
    '''Answers Mondays: 11:30 AM - 12:30 PM and Wednesdays: 11:30 AM - 12:30 PM'''
    print("A: Mondays: 11:30 AM - 12:30 PM and Wednesdays: 11:30 AM - 12:30 PM")

def printA3():
    '''Answers 2 MTC 10.054M'''
    print("A: 2 MTC 10.054M")

def printA4():
    '''Answers Yes'''
    print("A: Yes")

def printA5():
    '''Answers Tuesday, October 21, November 18, and December 9, 2014 at 12:00 pm'''
    print("A: Tuesday, October 21, November 18, and December 9, 2014 at 12:00 pm")

def printA6():
    '''Answers Examination Hour'''
    print("A: Examination Hour")

def printA7():
    '''Answers Tuedays from 12:30 pm to 2:20 pm'''
    print("A: Tuedays from 12:30 pm to 2:20 pm")

def printA8():
    '''Answers 25% each'''
    print("A: 25% each")

def printA9():
    '''Answers Examination Hour'''
    print("A: Examination Hour")

def printA10():
    '''Answers 35%'''
    print("A: 35%")

def printA11():
    '''Answers Yes'''
    print("A: Yes")

def printA12():
    '''Answers 0%'''
    print("A: 0%")

def printA13():
    '''Answers A minimum of 21 out of 26 lectures must be attended or the student will receive an F.'''
    print("A: A minimum of 21 out of 26 lectures must be attended or the student will receive an F.")

def printA14():
    '''Answers 0%'''
    print("A: 0%")

def printA15():
    '''Answers A minimum score of 83.33% (200 points) must be earned or the student will receive an F. There are 12 counted labs worth 20 points each'''
    print("A: A minimum score of 83.33% (200 points) must be earned or the student will receive an F. There are 12 counted labs worth 20 points each")

def printA16():
    '''Answers 21'''
    print("A: 21")

def printA17():
    '''Answers The student will fail the course.'''
    print("A: The student will fail the course.")

def printA18():
    '''Answers 83.33% (200 points)'''
    print("A: 83.33% (200 points)")

def printA19():
    '''Answers The student will fail the course.'''
    print("A: The student will fail the course.")

def printA20():
    '''Answers No'''
    print("A: No")

def printQandA1():
    '''Prints question and answer 1 with a line break after the answer'''
    printQ1()
    printA1()
    printLineBreak()

def printQandA2():
    '''Prints question and answer 2 with a line break after the answer'''
    printQ2()
    printA2()
    printLineBreak()

def printQandA3():
    '''Prints question and answer 3 with a line break after the answer'''
    printQ3()
    printA3()
    printLineBreak()

def printQandA4():
    '''Prints question and answer 4 with a line break after the answer'''
    printQ4()
    printA4()
    printLineBreak()

def printQandA5():
    '''Prints question and answer 5 with a line break after the answer'''
    printQ5()
    printA5()
    printLineBreak()

def printQandA6():
    '''Prints question and answer 6 with a line break after the answer'''
    printQ6()
    printA6()
    printLineBreak()

def printQandA7():
    '''Prints question and answer 7 with a line break after the answer'''
    printQ7()
    printA7()
    printLineBreak()

def printQandA8():
    '''Prints question and answer 8 with a line break after the answer'''
    printQ8()
    printA8()
    printLineBreak()

def printQandA9():
    '''Prints question and answer 9 with a line break after the answer'''
    printQ9()
    printA9()
    printLineBreak()

def printQandA10():
    '''Prints question and answer 10 with a line break after the answer'''
    printQ10()
    printA10()
    printLineBreak()

def printQandA11():
    '''Prints question and answer 11 with a line break after the answer'''
    printQ11()
    printA11()
    printLineBreak()

def printQandA12():
    '''Prints question and answer 12 with a line break after the answer'''
    printQ12()
    printA12()
    printLineBreak()

def printQandA13():
    '''Prints question and answer 13 with a line break after the answer'''
    printQ13()
    printA13()
    printLineBreak()

def printQandA14():
    '''Prints question and answer 14 with a line break after the answer'''
    printQ14()
    printA14()
    printLineBreak()

def printQandA15():
    '''Prints question and answer 15 with a line break after the answer'''
    printQ15()
    printA15()
    printLineBreak()

def printQandA16():
    '''Prints question and answer 16 with a line break after the answer'''
    printQ16()
    printA16()
    printLineBreak()

def printQandA17():
    '''Prints question and answer 17 with a line break after the answer'''
    printQ17()
    printA17()
    printLineBreak()

def printQandA18():
    '''Prints question and answer 18 with a line break after the answer'''
    printQ18()
    printA18()
    printLineBreak()

def printQandA19():
    '''Prints question and answer 19 with a line break after the answer'''
    printQ19()
    printA19()
    printLineBreak()

def printQandA20():
    '''Prints question and answer 20 with a line break after the answer'''
    printQ20()
    printA20()
    printLineBreak()

def printLineBreak():
    '''prints a blank line'''
    print(" ")

def printAllQsAndAs():
    '''prints all the questions and answers on new lines with a space between each question and answer set'''
    printQandA1()
    printQandA2()
    printQandA3()
    printQandA4()
    printQandA5()
    printQandA6()
    printQandA7()
    printQandA8()
    printQandA9()
    printQandA10()
    printQandA11()
    printQandA12()
    printQandA13()
    printQandA14()
    printQandA15()
    printQandA16()
    printQandA17()
    printQandA18()
    printQandA19()
    printQandA20()
    

def main():
    '''prints all the questions and answers and pauses the output'''
    printAllQsAndAs()
    os.system("pause")

if __name__ == '__main__':
    main()

