pos = -1
def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = l + u // 2
        if list[mid] == n:
            globals()['pos']=mid
            return True
        elif mid < n:
            l = mid + 1
        else:
            u = mid - 1

list = [3, 4, 5, 6, 7, 9]
n = 9
if search(list, n):
    print('found')
else:
    print('not found')