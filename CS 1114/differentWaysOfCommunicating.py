'''demo of some ways that functions can communicate'''

def noCommunicating(nameToPrint)
    '''fn receives no info from caller and gives no info to caller'''
    print ("hi there", nameToPrint)

def main()
    name = "Mary"
    notCommunicating(name)

main()
