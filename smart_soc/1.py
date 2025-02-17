# Write a program for reverse string 

"""
We need to take a string

Hello --> is a string

reverse a string
olleH  --> reversed string

"""

# 1st method

def reverse_string(s):
    reversed_string = " "
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

reversed_string = "Hello"
print("reverse_string:", reverse_string(reversed_string))


"""
# 2nd method

def reverse_string(s):
    return s[::-1]
rev = "Hello"
print("reversed_string:", reverse_string(rev))
"""
