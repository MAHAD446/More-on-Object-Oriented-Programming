# create calss
class IOSString():

    # construter to set default value
   def __init__(self):
     self.str1=""

    # function to get input from user
   def get__Strin(self):
        self.str1 = input("Enter string")
        print("result is :",self.str1.upper())

# object creation
str1 = IOSString()

# call functions
str1.get_String()
str1.print_String()



