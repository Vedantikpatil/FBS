#1.To neglect positional para concept.
#2.Assign value to para in function call

def emp(id,name,sal,dept):
    return f'ID:{id}\nNAME:{name}\nSALARY:{sal}\nDEPt:{dept}'

res=emp(name='ABC',sal=30000,dept='IT',id=29)
print(res)