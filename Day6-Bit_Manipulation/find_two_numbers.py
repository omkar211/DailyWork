"""
Exercise: Given an array A and a integer K,and find 2 numbers M and N such that M^N=Kif not exit return -1
"""
#Solution 1:
"""
lets say we have given an array [x1,x2,x3,x4,x5,x6] ,lets pick an element x3 and check in whole array 
except x3 is there any element exist that can give K after the XOR and we will check same for every element.
"""
#Code:
def two_numbers(A,k):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]^A[j]==k:
                return [A[i],A[j]]
            
    return [-1]
#Time Complexity:O(N^2),N=len(A)
#Space Complexity:O(1)

#Solution2:
"""
We know that xor property if A^B=C then A=B^C.
so if i pick an element from an array and do Xor with K then the resultant of the XOR will be let say A.
if we need to  find A in array. that is prsent or not .and we will do same thing for every elementin array
rather than finding in arrya we stored the elements in dict.
"""
def two_numbers(A,k):
    dt=dict()
    for i in range(len(A)):
        if (A[i]^k) in dt:#dt.get(A[i]^k,"message")
            return 'exist'
        else:
            dt[A[i]]=i
    return"not exist"
#Time Complexity:O(N),amotized
#Space Complexity:O(N)
    