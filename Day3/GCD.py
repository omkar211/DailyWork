""" Question:  Greatest Common Divisor
            Problem Description
Given 2 non negative integers A and B, find gcd(A, B)
GCD of 2 integers A and B is defined as the greatest integer g such that g is a divisor of both A and B. Both A and B fit in a 32 bit signed integer.
Note: DO NOT USE LIBRARY FUNCTIONS.
Problem Constraints
0 <= A, B <= 109

Input Format
First argument is an integer A.
Second argument is an integer B.

Output Format
Return an integer denoting the gcd(A, B).

Example Input
Input 1:

A = 4
B = 6
Input 2:

A = 6
B = 7

Example Output
Output 1:
2
Output 2:
1

Example Explanation
Explanation 1:

2 divides both 4 and 6
Explanation 2:
1 divides both 6 and 7
 """

#Solution:
"""
1.first we find the factors of a number and store it in a list 
  and we also find the factors of second number also and will store it in list.
2.we will take common values out and multiply them that will be are answer.
"""
#Code
def gcd(A,B):
    lst1=[]
    lst2=[]
    i=1
    while(A>1):
        if A%i==0:
            lst1.append(A//i)
            A=A//i
        i+=1
    i=1
    while(B>1):
        if B%i==0:
            lst2.append(B//i)
            B=B//i
        i+=1
    res=1
    i=0
    j=0
    while i<len(lst1) and j<len(lst2):
        if lst1[i]==lst2[j]:
            res*=lst1[i]
        elif lst1[i]>lst2[j]:
            j+=1
        else:
            i+=1
    return res
#Time Complexity = O(N)
#Space Complexity = O(N)


#Solution 2: Using Recursive Appraoch
def gcd2(A,B):
    if(B==0):
        return A
    return gcd2(B,A%B)
#Time Complexity:O(N)
#Space Complexity : O(N) using stack 



