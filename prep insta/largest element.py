"""
Find largest element in an array using Python
"""

 
def largest(a):
    max_ = a[0]
    for i in range(1, len(a)):
        if a[i] > max_:
            max_ = a[i]
    return max_

a = [10, 89, 9, 56, 4, 80, 8]
print(largest(a))
