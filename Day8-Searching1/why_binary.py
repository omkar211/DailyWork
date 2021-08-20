"""
Problem Statement:         BINARY SEARCH
When data is in order then exploit this order to search faster .
eg : We have given an array and if we find out a pattern in order to search the the key .Reject the half of the array inorder to archieve our goal . 
"""
#Code
def binary_search(A,k):
    low=0
    high=len(A)-1
    while low<high:
        mid=(low+high)//2
        if A[mid]==k:
            return mid
        elif A[mid]>k:
            high=mid-1
        else:
            low=mid+1
    return -1

"""
So here we are rejecting the half of the current array every time .
"""
#Time Complexity:O(logn)
#Space Complexity:O(1)
