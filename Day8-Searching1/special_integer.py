"""
Exercise:Special Integer
Problem Description
Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.
Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the maximum value of K (sub array length).

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 10
Input 2:
A = [5, 17, 100, 11]
B = 130

Example Output
Output 1:
 2
Output 2:
 3

Example Explanation
Explanation 1:
Constraints are satisfied for maximal value of 2.

Explanation 2:
Constraints are satisfied for maximal value of 3.
"""

#Bruteforce Approach
"""
We start check from 1 to N(array size) if lets say our testcase pass for single element then we check for subarray size 2 if it pass for it then we will check for 3 subarray.
"""
#Code
def special_integer(A,B):
    total=0
    for i in range(len(A)):
        total+=A[i]
        for j in range(i+1,len(A)):

