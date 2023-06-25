"""
Ways to remove i’th character from string in Python
test_str = "GeeksForGeeks"
output = "GeksForGeeks"
"""


def remove_element(sample):
    result = sample[:2] + sample[3:]
    return result
print(remove_element("GeeksForGeeks"))