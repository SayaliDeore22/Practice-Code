"""
Find Smallest element in an array using Python
"""


def smallest(arr):
    min_ = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_:
            min_ = arr[i]
            
    return min_

arr = [10, 89, 9, 56, 4, 80, 8]
print(smallest(arr))