# Problem:Max sum of sub matrix
"""
Description:
Given a matrix ,You need to find out the sub-matrix which have maximum sum.
"""
#   clarification:
"""
Matrix contains negative numbers.
if no negative return sum of matrix
"""
# Bruteforce Approach 
"""
1. Traverse on a matrix from UP ,DOWN,LEFT and RIGHT, every time you increase it will give you a new matrix.
2.To get every time the sum of it we have to traverse for every submatrix. 
"""
# Code:
def max_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    res = 0,_sum = 0
    for top in range(rows):
        for down in range(top+1,rows):
            for left in range(cols):
                for right in range(left+1,cols):
                    for i in range(top,down+1):
                        for j in range(left,right+1):
                            _sum +=matrix[i][j]
                    res =max(res,_sum)
                    _sum = 0
    return res
# Time Complexity:O(N*6) 
# Space Complexity:O(1) 

#Optimized Approach:
"""
1.I we observe for specific top and down , we are moving left and right and calculate the sum from starting, and same for if make constant for left and right.
take an example:

eg1:
if we have a single element matrix.
return the same

eg2:
if we have 2 elements in matrix = [a,b]
1. Take a matrix [a,a+b], we csan return which have contains maximum.

eg3:
if we have 4 elements 
          [a,b]
          [c,d]
1.We can  do [a,a+b]
             [a+c,a+b+c+d]
             return max

eg:
[a,b,c]
[d,e,f]
[g,h,i]
"""
# Time complexity:O(N*N)
# Space complexity:O(N*N)