'''
Write a program to calculate the total number of vowels and
count the each individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited"?'''

#Guvi Geeks Network Private Limited
data = input("Enter the String: ")

#calculate length of String
Vowela = ['a','A']
Vowele = ['e','E']
Voweli = ['i','I']
Vowelo = ['o','O']
Vowelu = ['u','U']
counta=0
counte=0
counti=0
counto=0
countu=0

# Iterate over the string
for x in data:
    if x in Vowela:
        counta=counta+1
    elif x in Vowele:
        counte=counte+1
    elif x in Voweli:
        counti=counti+1
    elif x in Vowelo:
        counto=counto+1
    elif x in Vowelu:
        countu=countu+1

#Pront the each vowels in given string
print ("No of 'a', 'A' vouwels in given string: ", counta)
print ("No of 'e','e' vouwels in given string: ", counte)
print ("No of 'i','I' vouwels in given string: ", counti)
print ("No of 'o','O' vouwels in given string: ", counto)
print ("No of 'u','U' vouwels in given string: ", countu)
