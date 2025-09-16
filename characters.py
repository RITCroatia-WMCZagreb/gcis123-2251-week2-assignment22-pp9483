'''
@ASSESSME.USERID: pp9483
@ASSESSME.AUTHOR: Patrik Pavlovic
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''
#one = input("Please enter an ASCII character:")
#two = input("Please enter another ASCII character:")

##onea = ord(one)
#twoa = ord(two)


def add_chars(onea,twoa,one,two):
    print("The sum of your ASCII characters is:",onea + twoa,"and your ASCII characters were:",one,two)


def subtract_chars(onea,twoa,one,two):
    print("The difference between the ASCII characters is:",onea - twoa,"and your ASCII characters were:",one,two)


     
    











    

def main():
    one = input("Please enter an ASCII character:")
    two = input("Please enter another ASCII character:")
    onea = ord(one)
    twoa = ord(two)
    add_chars(onea,twoa,one,two)
    subtract_chars(onea,twoa,one,two)

main()
