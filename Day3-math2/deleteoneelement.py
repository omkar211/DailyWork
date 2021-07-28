"""
Question : Delete Elements 
          Problem statements
          given an Array A ,contains N elements.Delete exactly one element such that GCD is maximized.
"""

#Clarification:
""" 
what should i do if :-
1.array size <=1.
2.array contains negative number.
"""
#Solution 1:
"""
Traverse on an array and remove every element once and calculate the gcd of array and storeit in a variable and compare it for getting maximum.
"""
#Code
def gcd(A,B):
    if B==0:
        return A
    return gcd(B,A%B)
def deleteoneelement(A):
    ans=-1
    index=-1
    for i in range(len(A)):
        res=0
        for j in range(len(A)):
            if j==i:
                continue
            res=gcd(res,A[j])
        if res>ans:
            index=i
            ans=res
    return [ans,index]

print(deleteoneelement([2,16,7,8,64]))


#Time Complexity: O(N*N*log(max_element))
#space Complexity: O(log(max_element)) 

#Solution 2:
"""
lets say we have given an arrray [a1,a2,a3,a4,a5].The gcd of whole array will gcd(a1,gcd(a2,gcd(a3,gcd(a5,a4))).
if we want to calculate the gcd of whole array excluding a3 element.
then it would be gcd(gcd(a1,a2),gcd(a4,a5)),because gcd follows associative and commutive properties.
1. so here we precompute the gcd from both the side of an array .
and traversing on that array and calculate the gcd of excluding ith position by gcd(i-1th and i+1th)
we can take gcd values from i-1th and i+1th position from precomputed array. 
"""

#Code
def gcd(A,B):
    if (B==0):
        return A
    return gcd(B,A%B)
def deleteoneelement2(arr):
    ans=-1
    if len(arr)<=1:
        return -1
    left=[0]*len(arr)
    right=[0]*len(arr)
    tmp=0
    for i in range(len(arr)):
        left[i]=gcd(tmp,arr[i])
    tmp=0
    for i in range(len(arr)-1,-1,-1):
        right[i]=gcd(tmp,arr[i])
    for i in range(1,len(arr)-1):
        ans=max(ans,gcd(left[i-1],right[i+1])))
    ans=max(ans,left[-2])
    return ans
#Time Complexity : O(N*log(max_element))
#Space Complexity : O(N+log(max_element))

