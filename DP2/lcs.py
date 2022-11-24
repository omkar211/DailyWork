# Exercise:
"""
Description:Least common subsequence
Given 2 string S and T find the LCS of both the strings.
"""
# Bruteforce Approach:
"""
1. find all possible subsequence and check 
"""
# Code
def lcs(S,T,n,m):
    if n==0 or m==0:
        return 0
    if S[n]==T[m]:
        return 1+lcs(n-1,m-1)
    return max(lcs(n,m-1),lcs(n-1,m))
# Time Complexity:O(2^N)
# Space Complexity:O(N)

# Otpimized Approach(memoization Approach or bottom-up Approach)
"""
1.we know the many times we are calculating lcs of sub-strings inorder to find the answer.
2. so we store the subproblem solution till index wise and return to append it in answer else we will calculate and store it in array or cache it .
"""
# code
def lcs(s,t,n,m,dp):
    if m==0 or n==0:
        return 0
    if dp[n][m]!=-1:
        return dp[n][m]
    if s[n]==t[m]:
        dp[n][m] = 1+lcs(n-1,m-1)
    else:
        dp[n][m] = max(lcs(n-1,m),lcs(n,m-1))
    return dp[n][m]

#Time Compexity:O(N*M)
#Space Compexity:O(N*M)

# Most Optmized Approch(Tabulation Approach or Top-Down Approach)
# Rules
"""
To solve tabulation problem there are few rules:
1. Dimension.
2. Size.
3. Cell Repeat.
4. Populate the DP Array.
"""
# Approach
"""
1. We know that,we compare ith element to all the other's string elements.
2. size of 2-D matrix will be (n+1)*(m+1).
3. if we pick the ith and jth column of a matrix , it will show the maximum LCS of string from ith and string2 till jth substring .
4. To get dp[i][j] there are two possibility 
   1. if s[i]==t[j] then dp[i][j] = 1 + dp[i-1][j-1]
   2. else dp[i][j] = max(dp[i-1][j],dp[i][j-1])
"""
# Code 
def lcs(s,t):
    s = " "+s
    t = " "+t
    dp = [[0]*(len(t)) for i in range(len(s))]
    for i in range(1,len(s)):
        for j in range(1,len(t)):
            if s[i] == t[j]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[i][j]
#Time Complexity:O(N*M)
#Space Complexity:O(N*M)