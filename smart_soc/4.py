# write a programm for string and find the vowels 


# vowels are "aeiouAEIOU"
"""
    Define the vowels (both lowercase and uppercase)
    Initialize an empty list to store the found vowels
    Iterate through each character in the string s
    Check if the character is a vowel
    If it is a vowel, add it to the found_vowels list
    Return the list of vowels found in the string

"""

def strings(s):
    vowels = "aeiouAEIOU"
    found_vowels = [ ]
    for char in s:
        if char in vowels:
            found_vowels.append(char)
    return found_vowels

string = "Maruthi"
print("vowels:", strings(string))
    
    
