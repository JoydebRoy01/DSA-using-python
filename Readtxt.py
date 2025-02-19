#Write a program to read a text file from the local drive and display the content of the file.
class content():
   with open ("ab.txt","r") as file:
     store = file.read()
   print(store)
      