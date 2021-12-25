#Exercise:Partition in 2 parts
"""
Given an array A of size N and k integer partition the array in such a way if one of subarray X size is K and another one  Y is N-K and |X-Y| is maximum.
"""
#Code
def partition(A,K):
    A.sort()
    mid=N//2
    second_total=0
    first_total=0
    if(k>mid):
        for i in range(len(A)-1,K-1,-1):
            first_total+=A[i]
        for i in range(N-K):
            second_total+=A[i]
    else:
        for i in range(K+1):
            first_total+=A[i]
        for i in range(k+1,N):
            second_total+=A[i]
    return (abs(second_total-first_total))

#Time Complexity:O(N)
#Space Complexity:O(1)