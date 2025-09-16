'''
@ASSESSME.USERID: pp9483
@ASSESSME.AUTHOR: Patrik
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL = str
INT_GLOBAL = int
FLOAT_GLOBAL = float


def print_param(pmeter):
    print(pmeter)

def print_local():
    local = "i guess"
    print(local)

def print_which():
    FLOAT_GLOBAL = "it's not"
    print(FLOAT_GLOBAL)


def main():
    print_param()
    print_local()
    print_which()


main()
