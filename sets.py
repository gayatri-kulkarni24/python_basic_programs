1. Write a Python program to create a set.
lst = [1, 2, 3, 3, 4]

s = set()

for i in lst:
    s.add(i)

print(s)

s = {1, 2, 3, 3, 4}

print(s)
##############

2. Write a Python program to iterate over sets.
s = {1, 2, 3, 4}

for i in s:
    print(i)
##############

3. Write a Python program to create set difference.
A = {1, 2, 3, 4}
B = {3, 4, 5}

print(A - B)

Output:{1, 2}
##############

4. Write a Python program to check if a set is a subset of another set.
A = {1, 2}
B = {1, 2, 3, 4}

if A.issubset(B):
    print("Subset")
else:
    print("Not subset")

##############

5. Write a Python program to find maximum and the minimum value in a set.
s = {5, 2, 8, 1}

print("Max =", max(s))
print("Min =", min(s))

##############

6. Write a Python program to find the length of a set.
s = {1, 2, 3, 4}

print(len(s))
