import math
listz = [3, 4, 16, 8, 25, 26, 1, 4, 3]
total = sum(listz)
if total%2 == 0:
    print("Even")
else:
    print("odd")

number = '123456789'

lasttwo = number[-2:]
lastthree = number[-3:]
lastfour = number[-4:]

masked = lasttwo.rjust(len(number), "#")
masked1 = lastthree.rjust(len(number), "#")
masked2 = lastfour.rjust(len(number), "#")

print(masked)
print(masked1)
print(masked2)




