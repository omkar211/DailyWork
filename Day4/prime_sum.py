"""
Question:    Prime Sum
     Problem Description
Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
If there are more than one solutions possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.

Problem Constraints
4 <= A <= 2*107
Input Format
First and only argument of input is an even number A.
Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.
Example Input
 4
Example Output
 [2, 2]
Example Explanation
 There is only 1 solution for A = 4.
"""
#clarification:
"""
Can 2 numbers be same .
"""
#Solution Discussion :
"""
1.Given A which are sum of (X,A-X) both are the primes.
2. if Both are prime that will be are answer.
"""
#Approach1:
"""
so lets say X <-----i to A:
so here we have to check every time if X is prime then does A-X is also prime or not . if prime 
then it will be the laxicograppcally sorted.
"""
#Time Complexity: O(A*sqrt(max_element))
#Space Complexity:O(1)


#Approach2:
"""
If we pre-calculate the given range prime numbers using seive of erasthosis then we need to go for 
simply from X to A-X . if both prime that will be our answer.
"""
def sieve(A,lst):
    for i in range(2,i*i+1):
        if A[i]:
            for j in range(i*i,A+1):
                lst[j]=False
    
def prime_sum2(A):
    lst=[1]*(A+1)
    sieve(A,lst)
    for i in range(A):
        if lst[i] and lst[A-1]:
            return [i,A-i]
#Time Complexity: O(AloglogA)
#Space Complexity: O(A)