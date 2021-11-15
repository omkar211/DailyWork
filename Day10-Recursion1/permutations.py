"""
Exercise: Permutations
Problem Description
Given an integer array A of size N denoting collection of numbers , return all possible permutations.

NOTE:No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
Return the answer in any order
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.

Problem Constraints
1 <= N <= 9

Input Format
Only argument is an integer array A of size N.

Output Format
Return a 2-D array denoting all possible permutation of the array.

Example Input
A = [1, 2, 3]

Example Output
[ [1, 2, 3]
  [1, 3, 2]
  [2, 1, 3] 
  [2, 3, 1] 
  [3, 1, 2] 
  [3, 2, 1] ]

Example Explanation
All the possible permutation of array [1, 2, 3].
"""

#Brute Force 
"""
So i will pick an element and tell the rest collection to find the permutaion and append an picked element to all the calculated rest permutation.

Base case :- if index==collection.lenght print the permutation or store it an array. 
"""
#Code 
def permutation(A,index):
    if index==len(A):
        print(A)
        return None
    for i in range(index,len(A)):
        A[i],A[index]=A[index],A[i]
        permutation(A,index+1)
        A[i],A[index]=A[index],A[i]
permutation([1,2,3,4,5],0)

#Time Complexity:O(N2)
#Space Complexity:O(1)