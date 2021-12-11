"""
Exercise:lexographically sorted permutation 
Problem statement:
    Given an string of alphabet character with repeatative character .we need to find out all the unique lexographically sorted permutations.
"""
#Bruteforce Approach 
"""
If we sort the string after every swap for remaining permutation calculation and calculate the permutation like file permutation2.py than will we our answer
"""
#Time Complexity:O(n!logn!*n!n^2)
#Space complexity:O(n)

#Optimized Approach 
"""
let's take an example "CABA". 
1. take an array of size 26.and take store the count of 'A' at zero place and B at 1st place and so on.
2. so it will be look like  A  B  C
                            2  1  1
3. my approach is, At first place i place first element at from the 0th index to 25th index whose   count is greater than 0. and substract its count and call to calculate remain permutation and once permutation calcullated then after control return. i increse the count at same place.
"""

#Code 
def permutation(A,perm,size):
    if size==len(perm):
        print(perm)
        return 
    
    for i in range(26):
        if(A[i]>0):
            perm=perm+chr(i+65)
            A[i]-=1
            permutation(A,perm,size)
            A[i]+=1
            perm=perm[:-1]

def helper(string):
    A=[0]*26
    string=string.upper()
    for i in range(len(string)):
        A[ord(string[i])-65]+=1
    permutation(A,"",len(string))
helper("AAC")

#Time Complexity:O(N*N!)
#space Complexity:O(N)