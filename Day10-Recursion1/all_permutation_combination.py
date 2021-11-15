"""
Exercise:All Unique Permutations

Problem Description
Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations.
NOTE: No 2 entries in the permutation sequence should be the same.
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.

Problem Constraints
1 <= |A| <= 9
0 <= A[i] <= 10

Input Format
Only argument is an integer array A of size N.
Output Format
Return a 2-D array denoting all possible unique permutation of the array.

Example Input
Input 1:
A = [1, 1, 2]
Input 2:
A = [1, 2]

Example Output
Output 1:
[ [1,1,2]
  [1,2,1]
  [2,1,1] ]
Output 2:
[ [1, 2]
  [2, 1] ]

Example Explanation
Explanation 1:
 All the possible unique permutation of array [1, 1, 2].
Explanation 2:
 All the possible unique permutation of array [1, 2].
"""
#Bruteforce Approach
"""
Lets take an example [1,1,2,3]
at every first place i have to swap each and every element once and tell the recursion to calculate rest permutation 
like (1+P(1,2,3)),inorder to check duplicates from the index till swaped one index i will check if the same element is exit or not if exist then i will not swap either i will swap and continue.
"""
#Code
def permutation(A,res,index):
    if(index==(len(A))-1):
        temp=[]
        for i in range(len(A)):
            temp.append(A[i])
        res.append(temp)
        # print(A)
        return 
    for i in range(index,len(A)):
        flag=False
        for j in range(index,i):
            if A[i]==A[j]:
                flag = True
                break
        if flag:
            continue
        A[i],A[index]=A[index],A[i]
        permutation(A,res,index+1)
        A[i],A[index]=A[index],A[i]

res=[]
permutation([1,1,3],res,0)
print(res)

#Time Complexity:O(2^N)
#Space Coplexity:O(N)