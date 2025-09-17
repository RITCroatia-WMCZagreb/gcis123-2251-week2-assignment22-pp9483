'''
@ASSESSME.USERID: pp9483
@ASSESSME.AUTHOR: Patrik
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL = "string global"
INT_GLOBAL = 100
FLOAT_GLOBAL = 100.5


def print_param(pmeter):
    print("value of this function is", pmeter)

def print_local():
    local = "i guess"
    print("Value of local variable",local)

def print_which():
    FLOAT_GLOBAL = "it's not"
    print(FLOAT_GLOBAL)


def main():
    print_param(STRING_GLOBAL)
    print_param(INT_GLOBAL)
    print_param(FLOAT_GLOBAL)
    local = (print_local())
    local
    print_local()
    print_which()
    print(FLOAT_GLOBAL)


main()
