int1 = [1, 2, 3,]
str1 = str(int1)
print(str1)

a = 123
star = str(a)
print(star)

str2 = ["Lizzy", "Alx"]
str22 = "".join(str2)
#str23 = str2.rjust(16, "#")
print(str22)

number = '123456789'
number1 = ''

lasttwo = number[-2:]
lastthree =number[-3:]
lastfour = number[-4:]

masked1 = lasttwo.rjust(len(number), '#')
masked2 = lastthree.rjust(len(number), '#')
masked3 = lastfour.rjust(len(number), '#')

name = ["lavie", "Mwirigi"]
luv = "".join(name)
print(luv)

print(masked1)
print(masked2)
print(masked3)

print(lasttwo)