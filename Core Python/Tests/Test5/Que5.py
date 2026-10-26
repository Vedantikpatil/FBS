#5. Python Program to Find the Union of two Lists without using set concept.

L1 = [1, 2, 3, 4, 5, 6, 8]
L2 = [3, 4, 5, 6, 7, 9, 10]

L3 = []

for i in L1:
    if i not in L3:
        L3.append(i)

for i in L2:
    if i not in L3:
        L3.append(i)

print("Union of two lists:", L3)