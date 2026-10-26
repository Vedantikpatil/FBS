#3.A list contains sublist with Emp information as follows : Data = [[101,”Seema”,45000],[340,”Rajani”,13000],[210,”Tannu”,14000],[320,”Suresh”,35000]]
#Write a program to sort the list based on salary.

Data = [[101, "Seema", 45000],
        [340, "Rajani", 13000],
        [210, "Tannu", 14000],
        [320, "Suresh", 35000]]

for i in range(len(Data)):
    for j in range(len(Data) - 1 - i):
        if Data[j][2] > Data[j+1][2]:
            temp = Data[j]
            Data[j] = Data[j+1]
            Data[j+1] = temp

print("Sorted list according to salary:")

for i in Data:
    print(i)