# Problem: Shortest String
"""
Description:
Given 2 string A and B . find out the shortest string length that has both A&B as subsequence
A = AGGTAB
B = GXTXAYB
Ans = AGXGTXAYB
"""
# Approach
"""
1. Find the LCS(A,B).
2. len(A)+len(B)-LCS(A,B) , this will be our answer.
"""
#  Time Compelxity:O(N*N)
#  Space Compelxity:O(N*N)