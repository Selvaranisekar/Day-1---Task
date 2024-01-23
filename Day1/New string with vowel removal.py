#write a python program that takes a string and returns a new string with all the vowels removed?

#Enter a string

data = input("Enter a string: ")

Vowels=['a','e','i','o','u','A','E','I','O','U']

newstr=""
Strlen=len(data)

for i in range (Strlen):
    if data[i] not in Vowels:
        newstr=newstr+data[i]
#print new String after removing Vowels
print("\nString after removing vowels: ")
data = newstr
print(data)

