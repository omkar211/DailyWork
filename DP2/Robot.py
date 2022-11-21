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
#Code (Memoization Approach)
def helper(dp,m,n):
  if m==0 or n==0:
    return 0
  if dp[m][n]!=-1:
    return dp[m][n]
  dp[m][n] = helper(dp,m-1,n) + helper(dp,m,n-1)
  return dp[m][n]
# Time Compexity O(N*M)
# Space Compexity O(N*M) and stack memory

# Tabulation Approach (top-down)
# code
def helper(dp,m,n):
  mat = [-1 for x in range(m+1)]*n
  mat[0] = [0]*M
  for i in range(n):
    mat[0][1] = 0
  for i in range(1,n):
    for j in range(1,m):
      mat[i][j] = mat[i][j-1]+mat[i-1][j]
  return mat[n][m]
# Time Compexity O(N*M)
# Space Compexity O(N*M)