"""
Exercise:
        find an array ,it contains every element exactly twice except one. find out that value.
        if number does not exist return -1 
"""
#Solution1:

"""
first we can sort an array and we traverse from starting and check if index first and index second 
contains same values or not .if not then return ith element else check for another pair.
"""
#Code
def find_num(A):
    A.sort()
    for i in range(0,len(A),2):
        if A[i]!=A[i+1]:
            return A[i]
    return -1
#Time Complexity:O(NlogN),N=list size
#Space Complexity:O(N)

#Solution 2:
"""
we know a XOR property A^A=0
so we XOR whole array the we left with answer
"""
def find_num2(A):
    res=0
    for i in range(len(A)):
        res^=A[i]
    return res

#Time Comlexity:O(N)
#Space Complexity:O(1)
