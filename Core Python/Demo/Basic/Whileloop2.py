i=1
while(i<=10):
    print(i)
    i+=1

#print multiplication table (HW)
#O/P:simple table 
i=1
while(i<=10):
    print(2*i)
    i+=1

#O/P:2*1=2
n=2
i=1
while(i<=10):
    print(n,'*',i,'=',n*i)
    i+=1


#Extra Example

#1 to 10 no sum 
sum=0
i=1
while(i<=10):
    sum=i+sum
    i+=1
    print(sum)

#2.print divisible by 5 no in 1 to 100 
i=1
while i<=100:
    if i %5==0:
        print(i)
    i+=1

#3.Smallest No
n=int(input("Enter Number:"))
smallest=9
while n>0:
    digits=n%10
    if digits<smallest:
        smallest=digits
    n=n//10
print("smallest number=",smallest)

#4.Largest No
n=int(input("Enter Number:"))
largest=0
while n>0:
    digits=n%10
    if digits>largest:
        largest=digits
    n=n//10
print("largest number=",largest)


    