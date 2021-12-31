# Exercise:Two Pairs
"""
Given an sorted array A of distinct integer and an integer K . find out all the pair whose sum is up to k. and print their indices.
where i!=j
"""

#Code
def pair(A,K):
    if len(A)==0:
        return -1
    start=0
    end=len(A)-1
    while start<end:
        if A[start]+A[end]==K:
            print("{},{}".format(start,end))
            start+=1
            end-=1
        elif A[start]+A[end]<K:
            start+=1
        else:
            end-=1
            
