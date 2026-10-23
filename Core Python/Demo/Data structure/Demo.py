###String inbuilt Function

##upper method.

s="hi i am good in python"
upc = s.upper()
print (upc)

##lower method
print(upc.lower())
print (upc.capitalize())
print (s.capitalize())
#print (s. ti)

s="PYTHON java"
print (s.swapcase())


##Searching method.

#Find:
Str = " Good in Python"

print(Str.find("in")) #It returns the starting inder 
print (Str.find ("on")) # -1
print (Str.find ("Good")) #returns last matching index Otherwise return -1

#Index:
print (Str.index ("in"))
print (Str.index ("Good"))

#Count:
print (Str.count ("Good")) #it will print the count of matching String if not Found then it will return -1

#Replace:
str="I Love Java Java Java Java"
print(str.replace("Java","python",2))
print(str)

#Split:
str="I:am:from:FBS"
print(str.split(":"))



