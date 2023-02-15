def search(list, n):
    i = 0
    while i <= len(list):
        if i== n:
            return True
        i = i + 1
    return False

list = [0, 3, 4, 5, 6, 7, 9, ]
n = 7
if search (list, n):
    print('found')
else:
    print('not found')