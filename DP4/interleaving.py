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
