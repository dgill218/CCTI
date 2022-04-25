"""
String Compression: Implement a method to perform basic string 
compression using the counts of repeated characters. For example, 
the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the 
original string, your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a - z).
"""

def string_compression(s): 
    compressed_string = [] 
    cur_letter = s[0]
    count = 1 
    for char in s[1:]: 
        if char == cur_letter: 
            count += 1 
        else: 
            compressed_string.append(cur_letter)
            compressed_string.append(str(count)) 
            count = 1 
            cur_letter = char
    compressed_string.append(cur_letter)
    compressed_string.append(str(count)) 
    compressed_string = "".join(compressed_string)

    if len(compressed_string) < len(s):
        return compressed_string
    else: 
        return s

def test(s):
    print(string_compression(s))

test("aabcccccaaa")
test("aaaabbbccd")
        
        
    