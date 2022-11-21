# Exercise 
"""
Description: find min way to reach end points
given a matrix of N*M with postive numbers filled and starting points and end point. find the min way to reach at end points,Robot can move right and down .
""""
# Bruteforce Approach 
"""
Find out all the ways and sum up and store and update the min in a global variable .
and return.

1. Lets take a last cell , if we get the answers just before of last cell then there is only a task remain to do , just add the last cell in oure answer . and we can oserve here is only 2 ways to get our answer 
one from horizontal of last cell and one from verticle of last cell. if we take the min from both of them and return the answer with sum up of last cell that will we our answer.
here i and taking starting point is 0,0 and last points are n,m
2. If we observe for the 1st row and for 1st column there is only one way.
"""


# Optimized Approach(memoization Approach or bottom-up approach)
"""
1. We can see here, we are calculating min path for every time for every cell again and again,
2. We will store our answers and return if need it .
"""
# code 
def helper(mat,dp,n,m):
    if n==0 or m==0:
        return 0
    if dp[n][m]:
        return dp[n][m]
    dp[n][m] = min(helper(n-1,m),helper(n,m-1))+mat[n][m]
    return dp[n][m]

dp = [0 for i in range(m)]*n
dp[0][0] = mat[0][0]
for i in range(1,n):
    dp[i][0]+=dp[i-1][0]
for i in range(1,m):
    dp[0][i]+=dp[0][i-1]   
helper(mat,dp,n,m)
# Time Complexity:O(N*M)
# Space Complexity:O(N*M) and stack complexity

# Most Optimized approach(Tabbulation or top-down Approach)
"""
1.Pick a mat[i][j]th cell,For that cell we can take min(dp[i][j-1],dp[i-1][j])+mat[i][j]
2. return the last cell as that will be our answer.
"""
def helper(mat,dp,n,m):
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = min(dp[i][j-1],dp[i-1][j])+mat[i][j]
    return dp[n][m]

dp = [0 for i in range(m)]*n
dp[0][0] = mat[0][0]
for i in range(1,n):
    dp[i][0]+=dp[i-1][0]
for i in range(1,m):
    dp[0][i]+=dp[0][i-1]   
helper(mat,dp,n,m)


# Time Complexity:O(N*M)
# Space Complexity:O(N*M)