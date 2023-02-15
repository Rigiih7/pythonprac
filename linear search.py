def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            return True
        i = i + 1 
    return False
list = [3, 56, 23, 7, 9, 2, 45]
n = 2
if search (list, n):
    print('found')
else:
 print('not found')