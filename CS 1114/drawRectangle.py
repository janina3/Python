import random

def drawRectangle(numRows, numColumns):
    '''Draws a rectangle made up of random digits.
       Rectangle has length numColumns and height numRows.'''

    for i in range(numRows):
        #print string of random digits of length numColumns

        string = ''

        for j in range(numColumns):
            string += str(random.randint(0, 9))

        print(string)

def drawTriangle(numRows):
    '''Draws right triangle of random digits. Base and height have size numRows'''

    for i in range(numRows):
        #print string of random digits of length i+1

        string = ''

        for j in range(i+1):
            string += str(random.randint(0, 9))

        print(string)


def main():
    drawRectangle(5, 7)
    drawTriangle(6)

main()
