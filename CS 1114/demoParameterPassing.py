'''
this program demonstrates
parameter passing

'''

def funcName(param1, param2):
    '''demo of parameter passing'''
    print('these values were passed: %s, %s' % (param1, param2)

def double5():
    doubled = 5 * 2
    return doubled

def main():
    funcName("hello", "world!")
    solution = double5()
    print(solution)

main()
