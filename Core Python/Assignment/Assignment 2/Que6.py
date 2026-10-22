###WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic. 

basic=int(input("Enter basic salary:"))
DA=(basic*10)/100
TA=(basic*12)/100
HRA=(basic*15)/100
total_salary=basic+DA+TA+HRA
print("Total salary = ", total_salary)