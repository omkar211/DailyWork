"""
Question : Delete Elements 
          Problem statements
          given an Array A ,contains N elements .the min number of elements that you must delete such that the GCD becomes 1.
          else return -1
"""
#Solution: 
"""
if we find out the gcd = 1 exist in array then no need to delete the element. if gcd = 1 does not in array that means we have to return -1
by using associative and commutative property.we can solve it .
"""
#Code
def gcd(A,B):
    if B==0:
        return a
    return gcd(B,A%B)
def deleteelements(A):
    res=A[0]
    for i in range(1,len(A)):
        res=gcd(res,A[i])
        if res==1:
            return "No need to delete element."
    else:
        return -1
#Time Complexity : (N*log(max_element))
#space Complexity: log(max_element)