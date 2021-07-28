"""
Question: Count of divisors
           Problem Description
Given an array of integers A, find and return the count of divisors of each element of the array.
NOTE: Order of the resultant array should be same as the input array.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 106
Input Format
The only argument given is the integer array A.
Output Format
Return the count of divisors of each element of the array in the form of an array.

Example Input
Input 1:
 A = [2, 3, 4, 5]
Input 2:
 A = [8, 9, 10]
Example Output
Output 1
 [2, 2, 3, 2]
Output 1:
 [4, 3, 4]
Example Explanation
Explanation 1:

The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
So the count will be [2, 2, 3, 2].
Explanation 2:

The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
So the count will be [4, 3, 4].
"""
#Clarification: 
"""
1. can it contains negative elements ?
"""
#Solution:
"""
So here we traverse on array and find out no of factors from 1 to A[i] and will insert in a list 
the list will be our answer.
"""
#Code
import math 
def count_factor(N):
    for i in int(math.sqrt(N)):
        if N%i==0:
            if i!=N//i:
                count+=2
            else:
                count+=1
                
def count_divisior(A):
    res=[]
    for i in A:
        res.append(count_factor(i))
    return res

# N size of A ,M is max element
#Time Complexity : O(N*N^1/2)
#Space Complexity : O(N)

#Solution 2:
"""
if i precalculate and store in an array based on their index wise . 
let say i pick index 2 . So  i will go through a range 10^5 and increament the factor of count
by 1 at index 2. 
"""
#Code
def seive(lst):
    for i in range(2,N):
        for j in range(i,N,j+i):
            if j%i==0:
                lst[j]+=1
            
def count_divisior(A):
    lst=[]
    seive(lst)
    res=[]
    for i in A:
        res.append(lst[i])
    return res

#Time Complexity : O(loglogN+len(A))
#Space Complexity : O(N)
