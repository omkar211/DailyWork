"""
Question : Prime Factors
Problem Description
You are given a Task as described below :
You are given A queries. For each query (1<=i<=A) you are given a prime number B[i], you need to give the count of all numbers in range 1 to 10^6 inclusive which have minimum prime factor B[i] for each query.

Problem Constraints
1 <= A <= 105
1 <= B[i] <= 106

Input Format
The first argument consists of an integer A, the number of queries.
The second argument consists of an array B of size A.

Output Format
Return an array which contains the count of all numbers in range 1 to 106 (inclusive), which have minimum prime factor B[i] for each query.
Example Input
 A = 1
 B = [11]

Example Output
 20779
Example Explanation
 The numbers with minimum prime factor as 11 are: 11, 121, 143, ...
"""

#Solution1 :
"""
So to find out the min count factor for all the queries we have to traverse on a A and calculate all the factors from B to 10^5 and simulteniously we will maintain the count.
1. so if a number with range B[i] to 10^5 Contains the factor of B[i] means divided by B[i] then we will increase the count .that will we our answer.
so my approach is we have to reach at every element within a range and have to check out that is a factor of B[i] or Not if yes then we will increase the count .
"""
#Code 
import math
def prime_factor(A,B):
    count = 0
    N=1000000
    result=[]
    for i in B:
        count = 0
        for j in range(i,N):
            if j%i==0:
                count+=1
        result.append(count)

#Time Complexity : O(N*len(B))
#Space Complexity : O(1)

#Solution 2:
"""
We Know the limit of Queries so what if we precalculate the factors of every number and for B[i] just return answer in O(1)
1. So we will take an array of an integer of size 10^5 and pre-initilize with the zero.
2. so we will pick an element from an array and check onward all the numbers which are divisible by picked number we simply increment by 1 at the position of picked element. 
"""
def sieve(lst,N):
    for i in range(N):
        if 
def prime_factor(A,B):
    lst=[]
    sieve(lst,A)
    for i in B:
        res.append(lst[i])
    


