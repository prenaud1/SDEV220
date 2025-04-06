"""
binarysearch.py
by Paul Renaud
4/6/2025
IvyTech SDEV220
Given a sorted list of integers and an integer to find, will search for the integer and return the index location.
Will return the lowest index if more than one matching value.
Will return -1 if not found.
"""

def binarysearch(arr, k):
    lower = 0
    upper = len(arr) - 1
    pos = (upper + lower) // 2
    tries = 0  # to not get stuck in infinite loop
    while lower <= upper and tries < len(arr):
        tries += 1
        pos = (upper + lower) // 2
        # print("Lower:",lower, " Pos:",pos,"("+str(arr[pos])+")", " Upper:",upper,sep="")
        if k == arr[pos] and k != arr[pos-1]:
            return pos
        elif k > arr[pos]:
            lower = pos + 1
        else:
            upper = pos - 1
    if tries >= len(arr):
        return -1
    return -1

arr = [1, 2, 3, 4, 5]
k = 4
# print(arr)
# print(k)
result = binarysearch(arr, k)
# print(result)
if result != -1:
    print("Found at position", result)
else:
    print("Not found.")
