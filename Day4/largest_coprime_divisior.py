#Question:
"""
Largest Coprime Divisor
                 Problem Description
You are given two positive numbers A and B . You need to find the maximum valued integer X such that:
X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
Problem Constraints
1 <= A, B <= 109

Input Format
First argument is an integer A.
Second argument is an integer B.

Output Format
Return an integer maximum value of X as descibed above.
Example Input
Input 1:

 A = 30
 B = 12
Input 2:

 A = 5
 B = 10
Example Output
Output 1:
 5
Output 2:
 1
Example Explanation
Explanation 1:
All divisors of A are (1, 2, 3, 5, 6, 10, 15, 30). 
The maximum value is 5 such that A%5 == 0 and gcd(5,12) = 1
Explanation 2:
 1 is the only value such that A%5 == 0 and gcd(1,10) = 1
"""

#Solution2:
"""
So here if X divides A it means X is a Factor of A and so we will calculate the all the factors of A 
and from greatest to lowest factor we traverse and check which one has a gcd =1 with B.
"""

#Code
import math
def factors(A):
    lst=[]
    lst1=[]
    for i in range(1,int(math.sqrt(A))+1):
        if A%i==0:
            lst.append(i)
            lst1.insert(0,A//i)
    lst.extend(lst1)
    return lst
def LargestCoprime(A,B):
    lst=factors(A)
    for i in range(len(lst)-1,-1,-1):
        if math.gcd(lst[i],B)==1:
            return lst[i]
print(LargestCoprime(30,12))

#Time Complexity: O(N^1/2+log(max(A,B)))
#Space Complexity: O(N) uppar Bound 


#Solution2: 
"""
So we know that if we sustract GCD of (A,B) from A every time till that answer.
"""

#Code 
def LargestCoprime2(A,B):
    while(True):
        tmp=math.gcd(A,B)
        if tmp==1:
            return A
        A//=tmp
print(LargestCoprime2(30,12))

#Time Complexity : log(max(A,B))
#Space Complexity: O(1)
