#Exercise:max element:
"""
Given an array of integers A and value k.find the maximum element from the sub array of size K 
eg : 2 3 1 10 4 1 6 3 2 0
K=3
ans: 3,10,10,10,6,6,....
"""
#Bruteforce Approach:
"""
find all the pair size of K and check for max element .
"""
#Code
def max_element(A,K):
    ans=[]
    for i in range(len(A)-K+1):
        res=float('inf')
        for j in range(i,K):
            res=max(res,A[i])
        ans=append(res)
    return ans

#Time Complexity:O(N*K)
#Space Complexity:O(1)



