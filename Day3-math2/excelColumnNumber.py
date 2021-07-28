"""
Question:Excel Column Number
            Problem Description
Given a column title as appears in an Excel sheet, return its corresponding column number.

Problem Constraints
1 <= length of the column title <= 5

Input Format
Input a string which represents the column title in excel sheet.

Output Format
Return a single integer which represents the corresponding column number.

Example Input
Input 1:
AB
Input 2:
ABCD
Example Output
Output 1:
28
Output 2:
19010
Example Explanation
Explanation 1:
 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28
"""
#Solution:
"""
if we observe here so here we get a equation f(n)=26^i+ascii(char) where i start from 0 to n from right to left.
"""
def excel(string):
    res=0
    index=1
    for i in range(len(string)-1,-1,-1):
        res+=index*(ord(string[i])-64)
        index*=26
    return res
print(excel('ABCD'))

#Time Complexity : O(N)
#Space Complexity : O(1) 