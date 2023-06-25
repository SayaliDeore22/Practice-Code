"""
Uppercase half string
Input : test_str = 'geeksforgeek'
Output : geeksfORGEEK
Explanation : Latter half of string is uppercased
"""


def convert_upper(sample):
    result = len(sample) // 2
    res = sample[:result] + sample[result:].upper()
    return res
print(convert_upper("geeksforgeek"))
