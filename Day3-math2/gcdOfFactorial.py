"""
Question : A array contains N elements and calculate the GCD of its factorial. 
"""
#Solution 1:
"""
lets say array [x1,x2,x3,x4,x5,x6]
so pick two elements and calculate fist factorial of x1 and x2 and then calculate the gcd(x1,x2).
and using commutive property we can calculate the gcd of rest . but we have calculate factorial first.
here gcd(gcd(gcd(x1,x2),x3),x4).........
"""
def fact(A):
    if A==0 or A==1:
        return 1
    return A*fact(A-1)
def gcd(A,B):
    if A==0:
        return B
    return gcd(B,A%B)

def helper(arr):
    res=fact(arr[0])
    for i in range(1,len(arr)):
        res=gcd(res,fact(arr[i]))
    return res
#Time Complexity :N*max*log max!  => N*max2log max
#Space Complexity : max

#Solution 2:
"""
if we have to find Greatest common Divisior of an whole array .so expand it lets see what we can do.

x2<x1<x3
x1!= 1*2*3*4*5*6*-------*x1
x2!= 1*2*3*4*X2
x3!= 1*2*3*4*5*6*7*8*9------*x3

so we can observe here . if we compare the factors of all the elements in the array .we will find minimum 
element is a answer.
return the min!
"""
#Code 
def helper2(A):
    minimum=A[0]
    for i in range(1,len(A)):
        minimum = min(minimum,A[i])
    return fact(minimum)
#Time Complexity : O(N+min)