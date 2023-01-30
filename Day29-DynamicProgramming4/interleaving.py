# Exercise:
"""
Description:
We have given S1 ,S2 and S3 where S3 is a combination of S1 and S2.
In S3 ,S1 & S2 are interleaving.find out this s3 is interleaving of S1 &S2 or not.

eg1. 
S1:XYZ
S2:ABC
S3:XAYBZC  ans True

but if S3:XACBYZ   ans False

eg2:
S1:XYZ
S2:ABC
S3:XAYBZP  

"""
# Bruteforce Approach:
"""
We will go step by step.
case 1. If length of S1+S2!=S3:return False
Case 2. If P not match of any string last element return False(take an example 2)
Case 3. If S1[i]==S[k] and S2[j]!=S[k]: return ans of Ans[i-1,j,k-1]
Case 4. If S1[i]!=S[k] and S2[j]==S[k]: return ans of Ans[i,j-1,k-1]
Case 5. If S1[i]==S[k] and S2[j]==S[k]: return ans of case 3 or case 4.
"""
# Base case
"""
1. If i=j=k=0: it means empty string return True.
2. If k=0,i!=0 or j!=0 return False 
"""

# code
def interleaving(s1,s2,s3,i,j,k):
    if i==k==j==0:
        return True
    elif k==0 and (i!=0 or j!=0):
        return False

    if s1[i]!=s3[k] and s2[j]!=s3[k]:
        return False
    elif s1[i]==s3[k] and s2[j]!=s3[k]:
        return interleaving(s1,s2,s3,i-1,j,k-1)
    elif s1[i]!=s3[k] and s2[j]==s3[k]:
        return interleaving(s1,s2,s3,i,j-1,k-1)
    elif s1[i]==s3[k] and s2[j]==s3[k]:
        return interleaving(s1,s2,s3,i-1,j,k-1) or interleaving(s1,s2,s3,i,j-1,k-1)
# Time Complexity :O(2^(N+M))
# Space Complexity:O(N+M)

# Optimized Approach(Memoization Approach):
"""
1.Here i observe optimal substructure and overlapping problem.
2.Here i and j and k are changing at every step, so the dp array will be 3D,But we can reduce it in 2D.
3.What does every shell represents ,dp[i][j] it mean s1->0 to i answer and same for j and k for every i , j and k till this shell if is forming interleaving or not .
4. If i at s1----> 0 to i , 
           s2----> 0 to j ,
           s3----> 0 to (i+j-1)
    So F(k)=(i,j).
5. Now then we converted it into 2d matrix 
"""
# Time Complexity:O(N*M)
# Space Complexity:O(N*M)

# code
def interleaving(s1,s2,s3,i,j):
    k = (i+j+1)
    if i==j==k==-1:
        return True
    if dp[i][j]!=-1:
        return dp[i][j]
    if s1[i]!=s3[k] and s2[j]!=s3[k]:
        return False
    elif s1[i]==s3[k] and s2[j]!=s3[k]:
        dp[i][j] = interleaving(s1,s2,s3,i-1,j)
    elif s1[i]!=s3[k] and s2[j]==s3[k]:
        dp[i][j] = interleaving(s1,s2,s3,i,j-1)
    elif s1[i]==s3[k] and s2[j]==s3[k]:
        dp[i][j] = interleaving(s1,s2,s3,i-1,j) or interleaving(s1,s2,s3,i,j-1)
    return dp[i][j]

#Optimized Approach 2(Tabulation Approach)
"""
1.To get the interleaving of string till index i and j of s1 ans s2.There are 2 ways,
2.first one when either s1 and s2 perticular element matches the s2 then we can check and consider the previous index answer and based on that store it in for dp[i][j].
3.second one when s1 and s2 both the perticular element are same and mathes to s3. then we take TRUE one answer from the just vertical and from the just horizontal shell and based on that will store the answer.
4. And dp[n][m] will be our answer.
"""
