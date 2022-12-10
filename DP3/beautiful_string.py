# Exercise 
"""
Description: Beautiful sting
Given a string S find out the pattern S = T+T.
eg: S = abcabc
    S = abc + abc
"""
# Optimzed Approach 
"""
1.Traverse on each and every character for i=0 to n
2.Divide the string in to two parts. one if 0 to i and another one is i+1 to n.
3.Calculate the LCS of divided string and maintain a global variable and store it in res and update  every time you got LCS .
"""
# Time Complexity :O(N*N*N)
# Space Complexity :O(N*N)