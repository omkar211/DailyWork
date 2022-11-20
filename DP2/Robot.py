# Exercise:
"""
Description: ROBOT
Given matrix start and end points
find the numbers of ways using that from start point, we can reach the end point.
constraints: i,j>0 
"""

# Brute force Approach
"""
Find all possible ways one by one .
"""
# Code 
res = 0
def find_ways(m,n):
    if (m == 1 or n == 1)
        return 1
    return countPaths(m - 1, n) + countPaths(m, n - 1)


# Time Complexity:Exponential
# Time Complexity:O(N*M)



# Optimized Approach 
"""
1. Take 1*1,0 way only.
2. Take 2*2 , ans , only 2 ways.
3. Take an example of N*M ,
  1. If i stand on ith and jth column of matrix the total number of ways must be total number of mat[i-1][j]+mat[i][j-1]
4. Return mat[n-1][m-1]
"""
#Code
def helper(mat,start,end):
  for i in range(start.first,end.second):
    for j in range(start.second,end.first):
      mat = mat[i][j-1] + mat[i-1][j]
  return mat[end.first][end.second]
def number_of_ways(start,end):
  if start.first==end.first and start.second==end.second:
    return 0
  mat = [[0 for i in range(len(matrix))]]*(len(matrix[0]))
  return helper(mat,start,end)

# Time Compexity O(N*M)
# Space Compexity O(N*M)