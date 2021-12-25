#Exercise:ANAGRAM
"""
"""
#Code:
def anagram(A,B):
    A.sort()
    B.sort()
    if len(A)!=len(B):
        return False
    for i in range(len(A)):
        if A[i]!=B[i]:
            return False
    return True

#Time Complexity:O(NlogN)
#Space Complexity:O(N)

#Optimized:
def anagram2(A,B):
    dt={}
    if len(A)!=len(B):
        return False
    for i in range(len(A)):
        dt[A[i]]=True
    for i in range(len(B)):
        if not dt.get([B[i]],False):
            return False
    return True

#Time Comlexity:O(N)
#Space Complexity:O(N)