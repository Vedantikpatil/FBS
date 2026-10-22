###Write a program to calculate the percentage of student based on marks of any 5 subjects.

M1=int(input("Enter marks of subject 1:"))
M2=int(input("Enter marks of subject 2:"))
M3=int(input("Enter marks of subject 3:"))
M4=int(input("Enter marks of subject 4:"))
M5=int(input("Enter marks of subject 5:"))
Total=M1+M2+M3+M4+M5
Percentage=(Total/500)*100
print("Percentage of the student is:",Percentage)