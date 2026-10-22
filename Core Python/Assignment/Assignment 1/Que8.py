###Write a program to convert days into years, weeks and days. 

total_days=int(input("Enter total days:"))
years=total_days/365
reamaining_days=total_days%365
weeks=reamaining_days//7
days=reamaining_days%7
print("years = ", years)
print("weeks = ",weeks)
print("days = ",days)