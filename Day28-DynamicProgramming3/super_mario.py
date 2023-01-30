# Exercise:
"""
Problem:Super Mario
Mario has to reach to Luigui.He has 2 options he can go right or down.
Given mashroom which increase his life.
given turtle which decrease his life.
What min health with which mario should start to reach luigui?
eg:
   [[-2,-3,3],
    [-5,-10,1],
    [10,30,-5]]
"""
#1. Very Bruteforce Approach
"""
1.Start guessing health from 0 till not found the valid health.
2.Check for all the paths .And return valid health 
"""
# Time Complexity :O(valid_health*2(M+N))
# Time Complexity :O(1)+stack

# 2. for first Approach optimize(Brute force Approach).
"""
1. To gussing the health lower limit is 0 and upper limit is 10^6.
2. Everytime i will guss health using binary search Algorithm and run it on all the paths and
3. If h health vaild on any one path then i will go for o to h-1 health.
"""
# Time Complexity :O(log(valid_health)*2(M+N))
# Time Complexity :O(1)+stack

# Bruteforce Approach
"""
1.Let's take any path to reach mario,[-2,-3,3,1,-5].
2.Ask every element from back how much health you need to reach mario and return to n-1th element.to know it that much health i need and same he add it's health that needed and so on ....
3. And calculate the path and store somewhere in a cache while reach at mario calculate the health and store it in global variable and update for min.
"""
# Time complexity:O(2^(M+N))
# Space complexity:O(M+N)+stack

# Optmized Approach(Tabulation Approach)
"""
1. Take an example
    [[-2,-3,3],
    [-5,-10,1],
    [10,30,-5]]
2. Shell arr[1][2] will be the part of the path will come through the cell of arr[1][1] and arr[0][1], if i store the min health needed to the next element.So then no need to calculate it again and again.
3.But if we see form arr[1][1] shell 2 path will goes through it ,So we can store min of both the path.
"""

def min_health(mat,i,j):
    n = len(mat)
    m = len(mat[0])
    dp = [[0]*m]*n
    if mat[n-1][m-1]<=0:
        dp[n-2][m-2] = mat[n-1][m-1]+1
    else:
        dp[n-2][m-2] = 1
    for i in range(n-3,-1,-1):
        dp[i][m-1] = dp[i+1][m-1]
    for i in range(m-3,-1,-1):
        dp[n-1][i] = dp[n-1][i+1]
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1])
    if dp[0][0]>=0:
        return 1
    return -1*dp[0][0]

# Time complexity:O(N*M)
# Space complexity:O(N*M)