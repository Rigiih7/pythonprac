arr =[7, 9, 8, 2, 3, 5, 8, 5, 4, 6, 1, 3, 4]
k = 4
m = max(arr)

for i in range(k-1):
    arr.remove(max(arr))
print(max(arr))
