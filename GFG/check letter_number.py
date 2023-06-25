"""
Python program to check if a string has at least one letter and one number
Input: welcome2ourcountry34
Output: True

Input: stringwithoutnum
Output: False
"""


def check_string(sample):
    flag_alpha = False
    flag_digit = False
    for i in sample:
        if i.isalpha():
            flag_alpha = True
        if i.isdigit():
            flag_digit = True

    if flag_digit and flag_alpha == True:
        return True
    else:
        return False

print(check_string("welcome2ourcountry34"))
print(check_string("stringwithoutnum"))

