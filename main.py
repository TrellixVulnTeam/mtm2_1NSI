from eventManager import *

if __name__ == '__main__':
    i = 1
    open('tests\input', 'r')
    fileCorrect('tests\input', 'tests\my_out1.txt')
    avg = correctAgeAvg('tests\input',3)
    printYoungestStudents('tests\input', 'tests\my_out2.txt', 9)
    testPrintEventsList('tests\my_out3.txt')
