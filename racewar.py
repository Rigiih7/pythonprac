import math
good = "1,2,3,3,4,10"
evil = "1,2,2,2,3,5,10"
a = good.split(",")
b = evil.split(",")
print(a)
print(b)
lista = [int(i) for i in a]
listb = [int(i) for i in b]
print(lista)
print(listb)

x = ['1', '2', '3', '3', '4', '10']
y = ['1', '2', '2', '2', '3', '5', '10']
listx = [int(i) for i in x]
print(listx)

if sum(lista) > sum(listb):
    print("Battle Result: Good triumphs over Evil")
else:
    if sum(lista) < sum(listb):
        print("Battle Result: Evil eradicates all trace of Good")
    else:
        print("Battle Result: No victor on this battle field")

