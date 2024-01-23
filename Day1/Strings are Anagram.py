'''write a python program that takes a string
 and returns True if it is an anagram of another string, false otherwise'''

def check(s1,s2):

    if(sorted (s1)==sorted(s2)):
        print(" The given string are Anagram")
    else:
        print(" The given string are not Anagram")

s1="listen"
s2="silent"

check(s1,s2)
