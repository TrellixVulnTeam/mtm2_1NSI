from eventManager import *

if __name__ == '__main__':
    i = 1
    open('tests\input', 'r')
    fileCorrect('tests\input', 'tests\my_out1.txt')
    printYoungestStudents('tests\input', 'tests\my_out1.txt', 1)