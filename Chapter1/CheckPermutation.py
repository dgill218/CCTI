# Check Permutation: Given two strings, write a method to decide 
# if one is a permutation of the other

def checkPermutation(s1, s2): 
    if (len(s1) != len(s2)):
        return False
    dict = {}
    for char in s1:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1 
    for char in s2:
        if char in dict:
            dict[char] -= 1 
            if dict[char] == 0:
                del dict[char]
        else:
            return False
    return len(dict) == 0 

def test(s1, s2):
    if checkPermutation(s1, s2):
        print("Yes")
    else:
        print("Nope")
        
test("abcd", "abc") # Nope 
test("abcd", "bcda") # Yes 
test("a", "a") # Yes
