pos = 0
def search(list, n):
    l = 0
    u = len(nums)-1
    for i in range(len(nums)-1):
        mid = (l + u) // 2
        if nums[mid] == n:
            globals()[pos]=mid
            return True
        elif nums[mid] < n:
            l = mid + 1
        else:
            u = mid - 1


nums = [23, 24, 33, 34, 43, 44, 53, 54, 63, 64, 73, 74, 83, 84, 93, 94]
n = 70
if search(list, n):
    print('found')
else:
    print('not found')