import math
def odd_or_even(arr):
    total = sum(arr)
    if total%2==0:
        return True
    else:
        return False
arr = [2, 7, 9, 23, 8, 7, 33, 49, 22, 17, 3]
if odd_or_even(arr):
    print("even")
else:
    print("odd")



