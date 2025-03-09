# Write a function that takes a string as a parameter and returns a string
# with every successive repetitive character replaced with a star(*). For
# example, ‘balloon’ is returned as ‘bal*o*n’.

class Repalce:
    def __init__(self, input):
        self.input = input

    def replace_repeats(self):
        if not self.input:
            return "" 

        result = self.input[0]  

      
        for i in range(1, len(self.input)):
            if self.input[i] == self.input[i - 1]:
                result += "*"  
            else:
                result += self.input[i]

        return result


input= input("Enter a string: ")
pr = Repalce(input)
output= pr.replace_repeats()
print(f"Input: {input}\nOutput: {output}")