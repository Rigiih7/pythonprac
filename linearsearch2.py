pos = -1
def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1

    return False

list = [4, 8, 16, 24, 32, 40, 48, 56, 64]
n = 40
if search(list, n):
    print('found at', pos)
else:
    print('not found')
