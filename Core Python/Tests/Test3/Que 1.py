#1.Write a program to print first n prime numbers.

n = int(input("Enter n: "))
num = 2
count = 0

while count < n:
    flag = 0

    for i in range(1, num + 1):
        if num % i == 0:
            flag = flag + 1

    if flag == 2:
        print(num)
        count = count + 1

    num = num + 1
