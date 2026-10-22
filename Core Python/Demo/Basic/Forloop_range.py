#1.
for i in range(1,11):
    print(i)

#2.
for i in range(2,21,2):
    print(i)

#3.
n=18
for i in range(n,n*10+1,n):
    print(i)

#4.
for i in range(5):
    print(i)

#5.print multiplication table in reverse for any no.(HW)

n=4
for i in range(n*10,n-1,-n):
    print(i)

#Extra Example
#1.sum of 1 to n no 
n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#2.find factorial 
n=5
fact=1
for i in range(1,n+1):
    fact+=i
print(fact)



