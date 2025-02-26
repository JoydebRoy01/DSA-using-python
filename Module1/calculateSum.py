#Write a program to calculate sum 1+2+3....+N
class Sum:
    def s(self, n):
        x = 0
        for i in range(n + 1):
            x += i
        print(x)

n = int(input("Enter the Number: "))    
ob = Sum()
ob.s(n)

   