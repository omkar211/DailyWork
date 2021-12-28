#Exercise:Largest Number
"""
Problem Description;
Given a array A of non negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.


Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109

Input Format
First argument is an array of integers.

Output Format
Return a string representing the largest number.

Example Input
Input 1:
 A = [3, 30, 34, 5, 9]
Input 2:
 A = [2, 3, 9, 0]


Example Output
Output 1:
 "9534330"
Output 2:
 "9320"


Example Explanation
Explanation 1:
 A = [3, 30, 34, 5, 9]
 Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2:
 Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320. 

"""
#code

from fractions import Fraction

def largestNumber(self, A):
    A = sorted(A, key=lambda n: Fraction(n, 10 ** len(str(n)) - 1), reverse = True)
    i = 0
    while i < len(A) - 1:
        if A[i] != 0:
            break
        else:
            i += 1
    ret = map(lambda x:str(x), A[i:])
    return ''.join(ret)

#Time Complexity:O(NlogN)
#Space Complexiyt:O(N)