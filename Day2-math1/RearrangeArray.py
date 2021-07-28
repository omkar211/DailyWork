"""
Question: Rearrange the array
            Problem Statement:
Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)].
Rearrange the array such that A[i] = j is changed to A[j] = i for all i and j form 0 to N-1.
Note: Try solving this with O(1) extra space.

Input Format
The only argument given is the integer array A.

Output Format
Return the rearranged array A.

Constraints
1 <= N <= 100000
0 <= A[i] < N
For Example

Input 1:
    A = [1, 2, 3, 4, 0]
Output 1:
    [4, 0, 1, 2, 3]

Input 2:
    A = [2, 0, 1, 3]
Output 2:
    [1, 2, 0, 3]

"""
# Solution 1:
"""
1.Create an array of same size of A and pre-initialize  it with Zero all the index let's array called 'arr'.
2.Traverse the array A from zero till N.
3.Assign the value in arr (arr[A[index]]=index).
4.Return arr
"""
#Code 
def rearrange(A):
    arr=[0]*len(A)
    for i in range(len(A)):
        arr[A[i]]=i
    return arr

print(rearrange([1, 2, 3, 4, 0]))

#Solution 2:
"""
.
"""