# Exercise:Two Pairs
"""
Given an sorted array A of not distinct integer and an integer K . find out all the pair whose sum is up to k.
where i!=j
"""
#Code
def pair(A,k):
    if len(A)==0:
        return -1
    start=0
    end=len(A)-1
    while(start<end):
        if A[start]+A[end]==k:
            tmp_start=start
            tmp_end=end
            while A[tmp_start]==A[start]:
                tmp_start+=1
            while A[tmp_end]==A[end]:
                tmp_end-=1
            if A[start]==A[end]:
                /// NC2
                continue
            else:
                count+=(tmp_start-start-1)*(tmp_end-end-1)
            start=tmp_start
            end=tmp_end

        elif A[start]+A[end]>k:
            end-=1
        else:
            start+=1


#Time Compexity:O(N)
#Space Complexity:O(1)