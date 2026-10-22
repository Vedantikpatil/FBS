#1.
for i in range(1,6):
    for j in range(1,6):
        print("*" ,end = " ")
    print()

#2.
for i in range(1,6):
    for j in range(1,5):
        print(i, end = " ")
    print()

#3.
for i in range(1,6):
    for j in range(1,5):
        print(j, end = " ")
    print()

#4.
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = " ")
    print()

#5.
for i in range(1,6):
    for j in range(1,7-i):
        print("*", end = " ")
    print()

#6.
for i in range(1,6):
    for j in range(6-i,0,-1):
        print(j, end = " ")
    print()

#7.
k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end = " ")
        k+=1
    print()

#8.
for i in range(1,6):
    for j in range(1,6):
        print(chr(64+i),end = " ")
    print()

#9.
for i in range(1,6):
    for j  in range(1,6):
        if(i % 2==0):
            print("$",end = " ")
        else:
            print("*", end = " ")
    print()    

#10.
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print("*",end= " ")
        else:
            print(" ",end= " ")
    print()

#11.
for i in range(1,6):
    for j in range(1,6):
        if(i==5 or j==1 or i==j):
            print("*",end= " ")
        else:
            print(" ",end= " ")
    print()

#12.
for i in range(1,6):
    for j in range(1,7-i):
        if(i==1 or j==1 or i+j==6):
            print("*",end= " ")
        else:
            print(" ",end= " ")
    print()

#13.
for i in range(1,6):
    for j in range(6-i,0,-1):
        if(i==1 or j==1 or i+j==6):
            print(j,end= " ")
        else:
            print(" ",end= " ")
    print()

#14.
for i in range(1,6):
    for j in range(1,i):
        print(" ",end=" ")
    for j in range(1,7-i):
        print("*",end=" ")
    print()

#15.
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#16.
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end= " ")
    for j in range(1,i+1):
        print("*",end= " ")
    for j in range(1,i):
        print("*",end= " ")
    print()

#17.
for i in range(1,6):
    for j in range(1,6-i):
        print(" " , end= " ")
    for j in range(1,i+1):
        print("*  ", end= " ")
    print()

#18.
k=7
for i in range(1,6):   
    for j in range(1, i+1):
        print("*",end= " ")
    for j in range(1,k+1):
        print(" ",end= " ")
    k-=2
    for j in range(1,i+1):
        if(i!=5 or j!=5):
            print("*",end= " ")
    print()
    
    




 
    
    
