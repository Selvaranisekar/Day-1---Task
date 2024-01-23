#writa a program that takes a string and returns true if it is a palindrome, otherwise False

#Enter the input String
Data = input("Enter the String: ")

#Declare emplty String value variable
revstr=""

#Iterate string with or Loop
for i in Data:
    revstr=i+revstr
print("Reversed String :", revstr)

if (Data==revstr):
    print("The give String is Palindrome")
else:
    print("The give String is not a Palindrome")





