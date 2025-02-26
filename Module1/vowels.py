#Write a program that create a dictionary with the frequency of the vowel
class Vowel:
    def Count(self, s):
        d = {}
        vowels = "aeiouAEIOU"
        
        for i in range(len(s)):
            if s[i] in vowels:
                if s[i] in d:
                    d[s[i]] += 1
                else:
                    d[s[i]] = 1
        print(d)

ob = Vowel()
s = input("Enter The char: ")
ob.Count(s)
