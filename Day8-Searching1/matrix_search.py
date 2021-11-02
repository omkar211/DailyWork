# Exercise: Matrix Search
"""
Problem Description
Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integar B in matrix A.
This matrix A has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.
NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
1 <= N, M <= 1000
1 <= A[i][j], B <= 106

Input Format
The first argument given is the integer matrix A.
The second argument given is the integer B.


Output Format
Return 1 if B is present in A, else return 0.

Example Input
Input 1:
A = [ 
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]  
    ]
B = 3

Input 2:
A = [   
      [5, 17, 100, 111]
      [119, 120, 127, 131]    
    ]
B = 3

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
 3 is present in the matrix at A[0][1] position so return 1.
Explanation 2:
 3 is not present in the matrix so return 0.
"""

#Bruteforce Approach
"""
Go through each and every shell and check if the number is equals to the 'key' and return 1 else 0.
"""
#Code 
def find_key(A,key):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==key:
                return 1
    return 0

#Time Complexity : O(N*M)
#Space Comlexity : O(1)


#Optimised Approach
"""
If first element of the Nth row is greater than the n-1 last element it means if we compare the "key" with first and last element . if key grater than equals to first element and smaller equals to the last element then key will present in this given range.
"""
#Code
def binary_search(A):
    low=0
    high=len(A)-1
    while low<=high:
        mid=(high+low)//2
        if A[mid]==key:
            return True
        elif A[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return False
def find_key2(A,key):
    for i in range(len(A)):
        if A[i][0]<=key and A[i][len(n)-1]>=key:
            if binary_search(A[i]):
                return True
            return False


#Time Complexity:O(N), N is number of Rows.
#Space Complexity:O(1)