"""
Given an array,return the no of non-empty subarray such that the left most element of sub-array is not larger than other elements of the subarray return count.
eg:[1,4,2,5,3]
output:[1],[4],[2],[5],[3],[1,4],[1,4,2],[1,4,2,5],[1,4,2,5,3],[2,5],[2,5,3]
"""
#Bruteforce Approach:
"""
1. first pick every element and check it for satisfying the condition
2. pick the range in between u want to choose.
3. iterate over the range and check is left most element is smallest.then add it into result.
"""
#Code:
def subarray(A):
    count=0
    for i in len(A):
        for j in range(i,len(A)):
            if A[i]<A[j]:
                count+=1
            else:
                break
    return count+len(A)

#Time Complexity:O(N)
#Space Complexity:O(1)

#Optimised Approach
"""
take an above example,pick 2 adjacent elements where i<j and A[i]>A[j] then no need to consider it in our answer.

"""
