###Program to Find the Roots of a Quadratic Equation

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=b*b-4*a*c
x1=(-b+d**0.5)/2*a
x2=(-b-d**0.5)/2*a
print("first root = ", x1)
print("second root = ", x2)