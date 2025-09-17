'''
@ASSESSME.USERID: fa6375
@ASSESSME.AUTHOR: Faraj Aliyev
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL = "GLOBAL STRING FOR TEST"
INT_GLOBAL = 11
FLOAT_GLOBAL = 55.5

def print_param(param):
    
    print("Value of Parametr: ", param)

def print_local():

    local_varl = "This is the local variable"   
    print("Local variable: ", local_varl)

def print_which():
    
    STRING_GLOBAL = 111
    print("Local variable which is STRING_GLOBAL is inside of print_which: ", STRING_GLOBAL)


def main():
    print_param(STRING_GLOBAL)
    print_param(INT_GLOBAL)
    print_param(FLOAT_GLOBAL)

    local_vrb = "Another local variable inside of main"
    print_local()


    print_which()
    print("Gloval STRING_GLOBAL in main: ", STRING_GLOBAL)


if __name__ == "__main__":
    main()