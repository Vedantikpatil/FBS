#1.pass:Neglect expected indented block error.
for i in range(1,10):
    pass

#2.Break:To terminated loop.
for i in range(1,5):
    if(i==3):
        break
    print(i)

#3.Continue:To stop current iteration.
for i in range(1,5):
    if(i==3):
        continue
    print(i)

#4.else:will executed when loop executed successfully.
for i in range(1,5):
    if(i==3):
        break
    print(i)
else:
    print("Else block executed.")