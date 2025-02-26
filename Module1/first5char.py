#write a programm to print first 5 charecter of your name using for loop

class NamePrint:
   def __init__(self,name):
      self.name=name
      
   def PrintChar(self):
      for i in range(5):
         print(self.name[i])
         
name = input("Enter your name: ")

if len(name)>=5:
   name_print = NamePrint(name)
   name_print.PrintChar()
   
else:
   print("please Enter the name over 5 char - ")
      