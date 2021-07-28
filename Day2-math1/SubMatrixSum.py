"""
QUestion:             Sum of all Submatrices
               Problem Description
Given a 2D Matrix A of dimensions N*N, we need to return sum of all possible submatrices.

Problem Constraints
1 <= N <=30
0 <= A[i][j] <= 10

Input Format
Single argument representing a 2-D array A of size N x N.

Output Format
Return an integer denoting the sum of all possible submatrices in the given matrix.

Example Input
A = [ [1, 1]
      [1, 1] ]

Example Output
16
Example Explanation
Number of submatrices with 1 elements = 4, so sum of all such submatrices = 4 * 1 = 4
Number of submatrices with 2 elements = 4, so sum of all such submatrices = 4 * 2 = 8
Number of submatrices with 3 elements = 0
Number of submatrices with 4 elements = 1, so sum of such submatrix = 4
Total Sum = 4+8+4 = 16


Solution 1: I will got through each and every submatrix and maintain global variable to store the 
          sum and return the sum.
"""
# Code

def SubMatrixSum(arr):
    res=0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            for sub_row in row+1:
                for sub_col in col+1:
                    for i in (row,sub_row+1):
                        for j in range(col,sub_col+1):
                            res+=arr[i][j]
    return res
    #Time Complexity : O(n^6)
    #Space Complexity : O(1)

print(SubMatrixSum([[1,2],[3,4]]))

"""
Solution 2: if we know the contribution of every element . how many times it will add up in 
            the solution then simply go over the matrix once and multiply by number of contribution
            in matrix to the element.
            
            Using the permutation and combination we can solve this problem.
"""

  #Code 
def SubMatrixSum2(arr):
    res=0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            res+=(row+1)*(col+1)*arr[row][col]*(len(arr)-row)*(len(arr[0])-col)
    return res

#Time Complexity :O(N2)
#Space Complexity:O(1)
