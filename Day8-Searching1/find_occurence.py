"""
 Exercise:Given an sorted array .every element occuring twice except 1 so find out that element.
eg:[1,1,2,3,3,5,5]
output:  2
"""
#Bruteforce Solution
"""
we know the XOR property A^A=0.So xor the whole array they will cancel out with each other 
and remaining one will be our answer.
"""
def single_element(A):
    res=0
    for i in range(len(A)):
        res=res^A[i]
    return res
#Time Complexity:O(N)
#Space Complexity:O(1)

#Optimized Solution:
"""                         0 1 2 3 4 5 6
Lets take an above example [1,1,2,3,3,5,5]
1. If we observe that before 2 every element's first occurence is at even position and after 2 all the element's first occurence is at odd index .so using this patten we can find out the solution.
"""
def single_element2(A):
    low=0
    high=len(A)-1
    while low<high:
        mid=(high+low)//2
        if mid==len(A)-1 and A[mid]!=A[mid-1]:
            return mid
        elif mid==0 and A[mid]!=A[mid+1]:
            return mid
        elif A[mid]<A[mid+1] and A[mid]>A[mid-1]:
            return mid
        elif (mid==len(A)-1 or mid==0):
            return -1
        elif mid%2==0 and A[mid]==A[mid+1]:
            low=mid+1
        else:
            high=mid-1

#Time Complexity:O(log N)
#space Complexity:O(1)
