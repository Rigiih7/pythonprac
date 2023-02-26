primelist = []
for num in range(2, 10000):
    for i in range(2, num):
        if (num % i == 0):
            break
    else:
        primelist.append(num)

print(primelist)

