###Write a program to enter P, T, R and calculate Compound Interest.

p=int(input("Enter principle(p):"))
t=int(input("Enter time(t):"))
r=int(input("Enter range(r):"))
Amount=1+r/100**t
CI=Amount-p
print("Compound interest = ", CI)