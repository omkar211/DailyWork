#Exercise :Count of smaller numbers after self
"""
Problem Description:
Given an array of integers A, find and return new integer array B.
Array B has the property where B[i] is the number of smaller elements to the right of A[i].

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return the new integer array B.

Example Input
A = [1, 5, 4, 2, 1]

Example Output
[0, 3, 2, 1, 0]

Example Explanation
Number of smaller elements to the right of 1 are 0.
Number of smaller elements to the right of 5 are 3 (4, 2, 1).
Number of smaller elements to the right of 4 are 2 (2, 1).
Number of smaller elements to the right of 2 are 1 (1).
Number of smaller elements to the right of 1 are 0.
"""

#Brute Force Approach
def countSmaller(A):
    res=[]
    for i in range(len(A)):
        count=0
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                count+=1
        res.append(count)
    return res
#Time Complexity:O(N^2)
#Space Complexity:O(1)

#Optimized Approach
def count_smalller(A):
    res=[]
    temp=[0]*100001
    for i in range(len(A)):
        if A[i]>100000:
            A[1]+=1
        else:
            A[1]+=1
            A[i]=-1
    for i in range(1,100001):
        temp[i]+=temp[i-1]
    for i in range(1,100001):
        if(A[i]!=A[i-1] and A[i]!=0):
            res.append(A[i])
    return res
#Time Complexity:O(100000) it means order of 1
#Space Complexity:O(100000) it means order of 1

    