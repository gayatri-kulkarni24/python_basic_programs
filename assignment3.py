1. Write a Python function to find the Max of three numbers.
def maximum(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Maximum =", maximum(x, y, z))
###################

2. Write a Python function to sum all the numbers in a list.
def sum_list(lst):
    s = 0
    for i in lst:
        s += i
    return s

numbers = [1, 2, 3, 4, 5]

print("Sum =", sum_list(numbers))

###################

3. Write a Python program to reverse a string.
def reverse_string(s):
    return s[::-1]

text = input("Enter string: ")

print("Reverse =", reverse_string(text))

###################

4. Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5]

print("Unique =", unique_list(numbers))

###################

5. Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input("Enter number: "))

if prime(num):
    print("Prime")
else:
    print("Not Prime")

###################

6. Write a Python function to check whether a number is perfect or not.
def perfect(n):
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s += i

    if s == n:
        return True
    else:
        return False


num = int(input("Enter number: "))

if perfect(num):
    print("Perfect number")
else:
    print("Not perfect number")
