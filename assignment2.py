# 1. Write a python program to check whether the string is Symmetrical or Palindrome
s = input("Enter string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

s[::-1] means
take the string from start to end with step -1
which reverses the string

Python internally goes through all characters, just like a loop

###################

2. Write a python program to Reverse words in a given String
s = input("Enter sentence: ")

words = s.split()
words.reverse()

print("Reverse words:", " ".join(words))
I/P:
Enter sentence: I love python
O/P:
Reverse words: python love I

###################

3. Write a python program to remove ith character from string in different ways
s = input("Enter string: ")
i = int(input("Enter index: "))

new = s[:i] + s[i+1:]

print("New string:", new)

###################

4. Write a python program to print even length words in a string
s = input("Enter sentence: ")

words = s.split()

for w in words:
    if len(w) % 2 == 0:
        print(w)

###################

5. Write a python program to accept the strings which contains all vowels
s = input("Enter string: ")

s = s.lower()

if ('a' in s and
    'e' in s and
    'i' in s and
    'o' in s and
    'u' in s):
    print("Contains all vowels")
else:
    print("Does not contain all vowels")

###################

6. Write a python program to Count the Number of matching characters in a pair of string
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = set(s1) & set(s2)

print("Matching characters:", len(common))

Python internally loops through the string and makes a set.
