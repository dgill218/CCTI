# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?
# abcdeff

# O(n) time O(n) space 
from re import T


def isUnique(s): 
    s = s.lower(); 
    charSet = set() 
    for char in s: 
        if char in charSet:
            return False
        else:
            charSet.add(char) 
    return True

# O(n) time O(1) space 
def isUniqueOptimal(string):
    checker = 0
     
    for i in range(len(string)):
        bitAtIndex = ord(string[i]) - ord('a')
 
        if ((bitAtIndex) > 0):
            if ((checker & ((1 << bitAtIndex))) > 0):
                return False
                 
            # Otherwise update and continue by
            # setting that bit in the checker
            checker = checker | (1 << bitAtIndex)
 
    # No duplicates encountered, return True
    return True
        


def test(s):
    if (isUniqueOptimal(s)):
        print("True")
    else:
        print("False")

test("Hello") # False
test("Hi bro") # True 
test("See ya") # False 