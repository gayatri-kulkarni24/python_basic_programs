1. Python Program to Calculate the Area of a Triangle
b = float(input("Enter base: "))
h = float(input("Enter height: "))
area = 0.5 * b * h
print("Area of triangle =", area)

Enter base: 5
Enter height: 4
Area of triangle = 10.0

###################

2.Python Program to Swap Two Variables
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swap:", a, b)
a, b = b, a
print("After swap:", a, b)

Enter first number: 10
Enter second number: 20
Before swap: 10 20
After swap: 20 10

###################

3. Python Program to Generate a Random Number
import random
print("Random number:", random.randint(1, 100))

###################

4. Write a Python Program to Check if a Number is Positive, Negative or Zero
n = int(input("Enter number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

###################

5. Write a Python Program to Check if a Number is Odd or Even
n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

###################

6. Write a Python Program to Check Prime Number
n = int(input("Enter number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

###################

 7. Write a Python Program to Check Armstrong Number
num = int(input("Enter number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit * digit * digit
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")

input-153
###################

8. Write a Python Program to Find the Factorial of a Number
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("Factorial =", fact) 
