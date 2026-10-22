li=[10,50,60,90,99,31]

max=li[0]
for ind in range(1,len(li)):
    if(li[ind]>max):
        max=li[ind]
print("Max:",max)