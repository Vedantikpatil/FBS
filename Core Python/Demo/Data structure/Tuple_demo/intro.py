#1.Structure-()

tu=(10,20,20,30,3.14,'abc')
#tu=(10)
#tu=10,20,30,40,50

#2.Type of data - Hetrogeneous

#3.Sequence - Ordered

#4.Changable - Immutable

#5.Duplication - Allowed

#tu[0]=50 #raise error

#print(type(tu))
#print(tu)

#6.Tuple is faster than list.

import sys

tu=()
li=[]
print(sys.getsizeof(tu))
print(sys.getsizeof(li))