"""
Exercise:Permutations
Problem:
find the permutation of a string which have distinct character?

Input:string="ABC"

output:
    ABC
    ACB
    BAC
    BCA
    CAB
    CBA
"""
# Bruteforce Approach
"""
we will go through with the basic rule of Backtracking.
if i fix every character at a palce and find out the permutation of remaining string and append with the fixed character and take union of all that will be my answer.
like:
    A+P(B,C)
    B+P(A,C)
    C+P(A,B)
"""
#Code
def permutation(A,index):
    if(index==len(A)):
        print(A)
        return 
    for i in range(index,len(A)):
        A[index],A[i]=A[i]=A[index]
        permutation(A,index+1)
        A[index],A[i]=A[i]=A[index]

#Time Complexity:O(N!*N),Nis size of a string
#Space Complexity:O(N)