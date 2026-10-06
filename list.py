1. Write a Python program to sum all the items in a list.
lst = [1, 2, 3, 4, 5]

s = 0

for i in lst:
    s = s + i

print("Sum =", s)
##
lst = [1, 2, 3, 4, 5]

print("Sum =", sum(lst))
###################

2. Write a Python program to multiplies all the items in a list.
lst = [1, 2, 3, 4]

mul = 1

for i in lst:
    mul = mul * i

print("Multiplication =", mul)

##
import math

lst = [1, 2, 3, 4]

print("Multiplication =", math.prod(lst))
###################

3. Write a Python program to get a list, sorted in increasing order by the last element in each tuple
from a given list of non-empty tuples.
lst = [(1,3), (2,1), (4,2)]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):

        if lst[i][1] > lst[j][1]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(lst)
Output-[(2,1), (4,2), (1,3)]
##
lst = [(1,3), (2,1), (4,2)]

lst.sort(key=lambda x: x[-1])

print(lst)
###################

4. Write a Python program to remove duplicates from a list.
lst = [1, 2, 2, 3, 4, 4, 5]

new = []

for i in lst:
    if i not in new:
        new.append(i)

print(new)
##
lst = [1, 2, 2, 3, 4, 4, 5]

new = list(set(lst))

print(new)

###################

5. Write a Python program to check a list is empty or not.
lst = []

if len(lst) == 0:
    print("List is empty")
else:
    print("List is not empty")
