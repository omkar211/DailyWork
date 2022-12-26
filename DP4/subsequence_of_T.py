# Problem: String subsequence of T
"""
Description:
Given a string S and find out if the string is a subsequence of a T.subsequence length must be greater than equals to 2 .

eg1:
 S = abab
 T  = ab
eg2:
 S = abcabcabc
 T = abc
eg3:
 S = abba
 T =""
eg4:
S = abba
T = bb
"""
#Approach
"""
Like Previous problem create partition at every character and find out LCS of both the string , if we get the answer return True or return False.
"""

