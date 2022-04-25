/*
URLify: Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to
 hold the additional characters, and that you are given the "true"
length of the string. 
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
Doing this in C++ b/c strings are mutable 
*/ 
#include <string> 
#include <iostream> 
using namespace std; 

string urlify(string s, int len) {
    int p1 = s.length() - 1; 
    int p2 = len - 1; 
    string token = "02%"; 
    while (p1 >= 0 && p2 >= 0) {
        if (s.at(p2) == ' ') {
            for (int i = 0; i < 3; i++) {
                s.at(p1) = token.at(i); 
                p1--; 
            }
            p2--; 
        }
        else {
            s.at(p1) = s.at(p2); 
            p1--;
            p2--; 
        }
    }
    return s; 
}

int main() {
    string s = "Mr John Smith    "; 
    string newString = urlify(s, 13); 
    cout << newString << endl; 
}