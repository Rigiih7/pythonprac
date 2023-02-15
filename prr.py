#riggih = {
         #'Mwende' : {'phone': '0710710', 'email': 'hotcake@gmail.com'},
         #'Seven' : 7
     #}
#print(riggih['Mwende'])
#print(list(riggih.keys()))

from array import *
arr = array ('i', [3, 7, 6, 8, 2, 4, 9])
arr.reverse()
print(arr)

for i in arr:
     print(i)

newarr = array(arr.typecode, [a*a for a in arr])
print(newarr)
 

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
#print(digits[5:9])
#for i in range(len (digits)):
     #print(digits[0:i])
   #print(digits[0:10:3])

windowsize=5
for i in range(len(digits)- (windowsize-1)):
     print(digits[i:i+windowsize])