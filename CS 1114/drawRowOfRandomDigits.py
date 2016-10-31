import random

def drawRectangle(numRows, numColumns):
    '''Draws a rectangle made up of random digits.
       Rectangle has length numColumns and height numRows.'''

    for i in range(numRows):
        #print string of random digits of length numColumns

        string = ''

        row = drawRowOfRandomDigits(numColumns)

        print(row)

        

def drawTriangle(numRows):
    '''Draws right triangle of random digits. Base and height have size numRows'''

    for i in range(numRows):
        #print string of random digits of length i+1

        string = ''

        row = drawRowOfRandomDigits(i+1)

        print(row)

def drawRowOfRandomDigits(rowLength):
    '''Draws row of random digit. Length of row is rowLength'''

    string = ''

    for j in range(numColumns):
            string += str(random.randint(0, 9))

        print(string) 
    


def main():
    drawRectangle(5, 7)
    print
    print
    drawTriangle(6)

main()
