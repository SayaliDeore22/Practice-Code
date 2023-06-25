"""
Python – Avoid Spaces in string length
Input : test_str = ‘geeksforgeeks best’
Output : 17
Explanation : Total characters are 17 except spaces.
"""

def avoid_spaces(sample):
    result = sample.replace(" ","")
    return len(result)

print(avoid_spaces("geeksforgeeks best"))
