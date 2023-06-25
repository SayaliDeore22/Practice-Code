"""
Find length of a string in python (6 ways)
Input : 'hello world !'
Output : 13
"""

def cal_length(sample):
    count = 0
    for i in sample:
        count += 1
    return count

print(cal_length('hello world !'))