#Write a program to take integer inputs from a file and display sum of the integers.

class hello:
   sum=0
   with open("ac.txt",'r') as file:
      for line in file:
         sum+=int(line)
   print(sum)