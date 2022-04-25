"""
One Away: There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

def one_away(s1, s2): 
    if abs(len(s1) - len(s2)) > 1: 
        return False 
    p1 = 0
    p2 = 0
    madeEdit = False 
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1 
            p2 += 1 
        elif not madeEdit: 
            # replacement 
            if len(s1) == len(s2):
                madeEdit = True 
                p1 += 1
                p2 += 1 
            # Deletions 
            elif len(s1) > len(s2):
                p1 += 1  
            elif len(s1) < len(s2):           
                p2 += 1           
        else:
            return False 
    return True 

def test(s1, s2): 
        if (one_away(s1, s2)): 
            print("True")
        else: 
            print("False")

test("Pale", "Ple") # True 
test("Pale", "Bale") # True 
test("Pale", "Bake") # False 
