#Exercise:contains_consecutive_elements
"""
Given an unsorted array of size N.if it contains consecutive elements return true.
"""
#Bruteforce Approach:
"""
1.Sort the array and check A[i]==A[i-1]+1 if not return false else return true.
"""
def contains_consecutive_elements(A):
    A.sort()
    for i in range(1,len(A)):
        if A[i]!=(A[i-1]+1):
            return False
    return True
#Time Complexity:O(NlogN)
#Space Complexity:O(N)

#Optimised Approach
"""
1. lets say array is [1,4,3,2,5], If we pick 1 and want to check it consecutive element for   2 in an array.if we find it in O(1). then our complexity will be O(N)
2. So we will store the elements in dict and pick min element and check in dict and every time increase it by 1 and check it till end.
"""
#Code
def contains_consecutive_elements2(A):
    dt={}
    Max=Min=-A[0]
    for i in range(len(A)):
        Max=max(Max,A[i])
        Min=min(Min,A[i])
        dt[A[i]]=True
    for i in range(Min,Max+1):
        if False== dt.get(Min,False):
            return False
    return True

#Time Complexity:O(N)
#Space Complexity:O(N)

