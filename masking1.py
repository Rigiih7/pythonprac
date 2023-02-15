number = '123456789'

lasttwo = number[-2:]
lastthree = number[-3:]
lastfour = number[-4:]

print(lasttwo)
print(lastthree)
print(lastfour)


masked1= lasttwo.rjust(16, "#")
print(masked1)

ip = '124.05.78.4'
strn1 = ip.split(".")
print(strn1)
print(strn1[1])
print(strn1[3])
print(strn1[0])
print(strn1[0][0])
pr

for i in strn1:
    print(i)
