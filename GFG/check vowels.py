"""
Python | Program to accept the strings which contains all vowels
Input : geeksforgeeks
Output : Not Accepted
All vowels except 'a','i','u' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present
"""


def check_vowels(sample):
    s = sample.lower()
    vowels = set("aeiou")
    res = set({})

    for i in s:
        if i in vowels:
            res.add(i)
        else:
            pass
    if len(vowels) == len(res):
        return "Accepted"
    else:
        return "Not Accepted"

print(check_vowels("geeksforgeeks"))
print(check_vowels("ABeeIghiObhkUul"))

