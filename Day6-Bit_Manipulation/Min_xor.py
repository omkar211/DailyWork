"""
Exercise: Min XOR value
        Problem Description
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.
Problem Constraints
2 <= length of the array <= 100000
0 <= A[i] <= 109

Input Format
First and only argument of input contains an integer array A.

Output Format
Return a single integer denoting minimum xor value.

Example Input
Input 1:
 A = [0, 2, 5, 7]
Input 2:
 A = [0, 4, 7, 9]
Example Output
Output 1:
 2
Output 2:
 3
Example Explanation
Explanation 1:
 0 xor 2 = 2
"""
#Solution:
"""
We will go through with all the possible pairs and find xor and update it in a variable if
xor is minimum.
"""
#Code:
def min_xor(A):
    res=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            res=min(res,A[i]^A[j])
    return res
#Time Complexity:O(N*N)
#Space Complexity:O(1)

#Solution2:
"""
Lets take three elements A>B>C. there are some cases.
the most significant bit of A is like 0 1 0 .....
                         of B is like 1 1 0 .....
                         of C is like 1 1 1 ......
                         if calculate here A^B which will never be greater than A^C .so answer can be 
                         minimum of A^B or B^C

"""
def min_xor(A):
    A.sort()
    res=0
    for i in range(len(A)-1):
        res=min(res,A[i]^A[i+1])
    return res
#Time Complexity:O(n)
#Space Complexity:O(1)
