'''
@ASSESSME.USERID: fa6375
@ASSESSME.AUTHOR: Faraj Aliyev
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''


def add_char(c1,c2):
    chrt1 = ord(c1)   
    chrt2 = ord(c2)
    sum = chrt1 + chrt2
    print("Sum of a and b: ",str(sum), "\nCharacter: ", chr(sum), "\n")

    


def subtract_char(c3,c4):
    chrt3 = ord(c3)
    chrt4 = ord(c4)
    diff = chrt3 - chrt4
    print("Difference of ", c3, " and ", c4, " = ", str(diff), "\nCharacter: ", chr(diff), "\n")



"""
When i firsly ran the code it didnt show the characters for both sum and diffrence, 
it was just an empty space, i thought i made a mistake, however, then i checked the ASCII table and saw
the numbers which are less than 33 and more than 127 are not symbols, therefore it doesnt display
So then i ckecked which decimals of ASCII tables plus and minus is not exceeding the table it self to check whether my code works, and those characters are: Z and !
"""

def main():
    input_1 = input("Enter the first character: ")
    input_2= input("Enter second character: ")
    
    #Here for input is recommended to put for a = Z and for b = !. because in this case you can see that code works, otherwise the vlaue of either plus or minus is gettig out of the ASCII table
    add_char(input_1,input_2)
    subtract_char(input_1,input_2)


"""
When the user enters two or more characters the code can not insert it to the parameters
because, there are only 2 parameters
i did not inserted the code to google, because i usually try to do it myself withouth google
i copied whole code inserted it to PYCHARM, because i thought its an error in Visual studio. 

"""
if __name__ == "__main__":
    main()