pos = - 1
def search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1 
            else:
                u = mid-1
    return False 
        

list = [11, 21, 31, 41, 51, 61, 71, 81, 91]
n = 81
if search(list, n):
    print('found')
else:
    print('not found')