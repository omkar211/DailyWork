"""
Exercise :Unique Path II

Problem Description
Given a matrix of integers A of size N x M . There are 4 types of squares in it:
1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.
Find and return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
2 <= N * M <= 20
-1 <= A[i] <= 2

Input Format
The first argument given is the integer matrix A.

Output Format
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

example Input

Input 1:
A = [   [1, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 2, -1]   ]
Input 2:
A = [   [0, 1]
        [2, 0]    ]

Example Output
Output 1:
2
Output 2:
0

Example Explanation
Explanation 1:
We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Explanation 1:
Answer is evident here.
"""
#Bruteforce Approach
"""
1. I will find first starting and ending point and count all the zeros so that at perticular path we check all the zero covered and we also take 2D list where we will maintain all the index that we have covered.
2. and find all the possible path by going in 4 directions
3. Let's say if i find the a first path then i return to previous point and move other 3 directions to reached to the destination.
"""
#Code
def helper(A,i,j,total_zeros,traversed_path,current_zeros):
    if i>=len(A) or i<0 or j>=len(A[0]) or j<0 or traversed_path[i][j]==1 or A[i][j]==-1:
        return 0
    print(A[i][j])

    if A[i][j]==2:
        if total_zeros==current_zeros:
            print(1)
            return 1
        return 0
    # print(traversed_path)
    traversed_path[i][j]=1
    down=helper(A,i+1,j,total_zeros,traversed_path,current_zeros+1)
    up=helper(A,i-1,j,total_zeros,traversed_path,current_zeros+1)
    right=helper(A,i,j+1,total_zeros,traversed_path,current_zeros+1)
    left=helper(A,i,j-1,total_zeros,traversed_path,current_zeros+1)
   
    traversed_path[i][j]=0
    return right+left+down+up
def unique_path(A):
    total_zeros=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if(A[i][j]==0):
                total_zeros+=1
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==1:
                traversed_path=[[0]*len(A[0])]*len(A)
                return helper(A,i,j,total_zeros,traversed_path,0)

print(unique_path([[1, 0, 0, 0],[0, 0, 0, 0],[0, 0, 2, -1]]))