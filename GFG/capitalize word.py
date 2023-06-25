"""
Python program to capitalize the first and last character of each word in a string
Input: hello world
Output: HellO WorlD
"""


def convert_word(sample):
    l1 = sample.split(" ")
    new = []
    for i in l1:
        result = i[0].upper() + i[1:-1] + i[-1].upper()
        new.append(result)
    res = " ".join(new)
    return res

print(convert_word("hello world"))

