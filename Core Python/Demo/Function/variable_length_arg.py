def add(*data):
    sum=0
    for val in data:
        sum+=val
    return sum

res=add(10,20,30,50,40,80)
print(res)