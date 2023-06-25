"""
Python program to print even length words in a string
Input: s = "This is a python language"
Output: This is python language
"""


def check_even_len(sample):
    l1 = sample.split(" ")
    new = []
    for i in l1:
        if len(i) % 2 == 0:
            new.append(i)
    result = " ".join(new)
    return result
print(check_even_len("This is a python language"))


