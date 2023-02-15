from array import *

#vals= array('i', [6, 8, 9, 4, 3, 7, 5, 0])
#vals.reverse()

#for i in vals:
    #print(i)

#newarr = array(vals.typecode, (a*a for a in vals))

#for a in newarr:
    #print(a)


lavi = array ('i', [])
n = int(input("enter the length of your array"))

for i in range(n):
    x = int(input("enter the next value"))
    lavi.append(x)

print(lavi)

val = int(input("enter the value to be searched"))

k = 0
for e in lavi:
    if e==val:
        print(k)
        break
    k+=1

print(lavi.index(val))