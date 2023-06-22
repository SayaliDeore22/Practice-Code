"""
Python program to check whether the string is Symmetrical or Palindrome
Input : amaama
Output : String is Palindrome
"""


def Check_Palindrome(sample):
    temp = sample
    rev = sample[::-1]
    if rev == temp:
        return "String is Palindrome"
    else:
        return "String is not Palindrome"

print(Check_Palindrome("amaama"))
print(Check_Palindrome("khokho"))