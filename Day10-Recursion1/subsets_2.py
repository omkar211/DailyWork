"""
Exercise: Subsets II
Problem Description
Given a collection of integers denoted by array A of size N that might contain duplicates, return all possible subsets.
NOTE:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.

Problem Constraints
0 <= N <= 16

Input Format
Only argument is an integer array A of size N.

Output Format
Return a 2-D vector denoting all the possible subsets.



Example Input
Input 1:
 A = [1, 2, 2]
Input 2:
 A = [1, 1]

Example Output
Output 1:
 [
    [],
    [1],
    [1, 2],
    [1, 2, 2],
    [2],
    [2, 2]
 ]
Output 2:
 [
    [],
    [1],
    [1, 1]
 ]

Example Explanation
Explanation 1:
All the subsets of the array [1, 2, 2] in lexicographically sorted order.
"""
#Bruteforce Approach
"""
I will sort the array and every time i will consider an element once and once not .Inorder to archiving lexicographically sorted order .i will print at while i consider an element and i will not print while while not considering and to archieve unique combination i will not consider same element from the perticular index.
"""
#Code
def subset2(A,index,flag,temp):
    if index==len(A):
        return 
    if flag:
        print(temp)
    temp.append(A[index])
    subset2(A,index+1,True,temp)
    temp.pop()
    while(index+1<len(A) and A[index]==A[index+1]):
        index+=1
    subset2(A,index+1,False,temp)
subset2([1,2,3,4],0,True,[])

#Time Complexity:O(2^N)
#Space Complexity:O(N)
