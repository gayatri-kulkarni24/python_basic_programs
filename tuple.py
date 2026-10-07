1. Write a Python program to create a tuple.
t = (1, 2, 3, 4)

print(t)
##
t = tuple([1, 2, 3, 4])

print(t)
###################

2. Write a Python program to create a tuple with different data types.
t = (1, "hello", 3.5, True)

print(t)

###################

3. Write a Python program to check whether an element exists within a tuple.
t = (1, 2, 3, 4)

x = 3

if x in t:
    print("Exists")
else:
    print("Not exists")

###################

4. Write a Python program to convert a list to a tuple.
lst = [1, 2, 3]

t = ()

for i in lst:
    t = t + (i,)

print(t)
##
lst = [1, 2, 3]

t = tuple(lst)

print(t)
###################

5. Write a Python program to remove an item from a tuple.
t = (1, 2, 3, 4)

lst = list(t)

lst.remove(3)

t = tuple(lst)

print(t)

###################

6. Write a Python program to slice a tuple.
t = (1, 2, 3, 4, 5)

print(t[1:4])
###################

7. Write a Python program to find the length of a tuple.
t = (1, 2, 3, 4)

count = 0

for i in t:
    count += 1

print(count)
##
t = (1, 2, 3, 4)

print(len(t))
