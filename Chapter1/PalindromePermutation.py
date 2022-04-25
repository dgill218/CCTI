"""
4 Palindrome Permutation: Given a string, write a function to check if 
it is a permutation of a palindrome. A palindrome is a word or phrase that 
is the same forwards and backwards. A permutation is a rearrangement of letters.
 The palindrome does not need to be limited to just dictionary words. 
"""
# If len(s) is odd, only count of a single char can be odd. 
# If len(s) is even, counts of all chars have to have same freqency. 
from re import T


def palindrom_permutation(s):
    dict = {}
    for char in s: 
        if char == ' ': 
            continue
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1 
    hasOdd = False 
    for key in dict:
        if dict[key] % 2 == 1: 
            if hasOdd == True: # If odd char already 
                return False 
            hasOdd = True
    return True 

def test(s):
    if (palindrom_permutation(s)):
        print("True")
    else: 
        print("False")
test("caabb") # True 
test("a") # True 
test("caabbb") # False 
