"""
Exercise: Reverse Bits
    Problem Description
Reverse the bits of an 32 bit unsigned integer A.

Problem Constraints
0 <= A <= 232

Input Format
First and only argument of input contains an integer A.

Output Format
Return a single unsigned integer denoting the decimal value of reversed bits.

Example Input
Input 1:
0
Input 2:
3
Example Output
Output 1:
0
Output 2:
3221225472

Example Explanation
Explanation 1:
00000000000000000000000000000000    
00000000000000000000000000000000
Explanation 2:
00000000000000000000000000000011    
11000000000000000000000000000000
"""
#Solution:
"""
we will take the every bit from 0 to 31 and check if this bit set then put at same position from the most significant bit .
"""
#Code :
def reverse_bit(A):
    res=0
    for i in range(32):
        res|=((A&(1<<i)>>i)<<(32-i))
    return res
#Time Complexity:O(1)
#Space Complexity:O(1)
