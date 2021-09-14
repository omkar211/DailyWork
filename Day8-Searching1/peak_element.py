"""
Exercise: you have Given an array contains n elements .you have to find the PEAK element in the array
Peak element condition.
1. if A[i-1]<A[i]>A[i+1]
2.if i==0,A[i]>A[i+1]
3.if i==len-1,A[i]>A[i-1]
"""
#BruteForce:
"""
We will pick an element and will check if it's just right and just left number is less than the choosen one .then return choosen number. if not then i will check for another number. 
"""
#code
def find_peak(arr):
    if len(arr)==0:
        return -1
    if len(arr)<2:
        return arr[0]
    if arr[0]>arr[1]:
        return arr[0]
    if arr[-1]>arr[-2]:
        return arr[-1]
    for i in range(1,len(arr)-1):
        if(A[i-1]<A[i] and A[i]>A[i+1]):
            return A[i]
    return -1

#Optimized approach
"""
Here are some cases lets choose M.
                           Left < M > Right  ----->return M
                           Left < M < Right  ----->then peak will be at right side
                           Left > M > Right  ----->then peak will be at left side
                           Left > M < Right  -----> then move in any direction.
"""
# Code
def find_peak2(arr):
    if len(arr)==0:
        return -1
    if len(arr)<2:
        return arr[0]
    if arr[0]>arr[1]:
        return arr[0]
    if arr[-1]>arr[-2]:
        return arr[-1]

    low=1
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return arr[mid]
        elif arr[mid]<arr[mid-1]:
             high=mid-1
        else:
            low=mid+1
    return -1
    
            