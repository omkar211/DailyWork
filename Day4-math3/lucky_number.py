"""      Question:Lucky Numbers
           Problem Description
A lucky number is a number which has exactly 2 distinct prime divisors.
You are given a number A and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).

Problem Constraints
1 <= A <= 50000

Input Format
The first and only argument is an integer A.

Output Format
Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.

Example Input
Input 1:
 A = 8
Input 2:
 A = 12

Example Output
Output 1:
 1
Output 2:
 3

Example Explanation
Explanation 1:
 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.
Explanation 2:
 Between [1, 12] there are 3 lucky number: 6, 10 and 12.
"""
#Clarification
"""
1-Does it contains negative numbers?
"""
#Solution1:
"""
so i will start from i= 1 to A and check how many prime numbers can divides 'i' 
and maintain a count if that ith number has exactly 2 prime factors then print it.
if i>2, then i will quit the calculation and increment the i by 1 and same process.
"""
#Solution2:
"""
1.lets say we precalculate the prime factor and store some where .
2.We pick a number and calculate the prime all its prime factors it means calculating its divisors 
3. So i will make an array of size A and pick a first prime number and increment by 1 in all the elements which has contain the factor of prime number.
4.so here i can find all the exactly 2 numbers in just by going through a single loop.
"""

def sieve(A,lst):
    for i in range(2,A//2):
        for j in range(i*i,A,j+i):
            lst[j]+=1
def lucky_number(A):
    lst=[0]*A+1
    for i in range(A):
        if lst[i]==2:
            ans.append(i)
    return ans

#Time Complexity: O(loglogA+A)
#Space Complexity: O(A)
