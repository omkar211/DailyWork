"""
Question: CoPrime Again
             Problem Description
You are given 2 arrays A and B of size N and M respectively and a number K.
You have to tell that how many pairs (A[i], B[j]) (1 <= i <= N and 1 <= j <= m) exists such that product of them is not CoPrime with K.
Problem Constraints
1 <= N, M <= 1e5
1 <= A[i], B[j], K <= 1e6
Input Format
Given two Arrays A and B of Type Integer, and an Integer K.

Output Format
Return a single Integer P, the number of pairs.
Example Input
 A = [1, 2, 3]
 B = [2, 3, 4, 5] 
 K = 3

Example Output
 6

Example Explanation
 There are total 12 pairs, and 6 pairs are there such that their product is not coprime with k, i.e 6.
 These Pairs are :
    (1, 3), (2, 3), (3, 3), (3, 2), (3, 4), (3, 5)
"""
#Clarification :
"""
it contains duplicate elements ?
what is i found same pair more than twice?
"""
#Solution:
"""
So we will go here pick  an element from any array lets say from A .with that multiply every element of B once and check if the product of GDC(A[i]*B[j],K)!=1 , we will check same for all the elements of A.and count the gcd !=1.
"""
def coprimeAgain(A,B,k):
    count=0
    for i in range(len(A)):
        for j in range(len(B)):
            if math.gcd(A[i]*B[j],k)!=1:
                count+=1
    return count
#Time Complexity: O(N*M*Log(max(element)))
#Space Complexity:O(1)

#Solution2: 
"""
lets say the is a pair that does not coprime (A,B) with K, 
so here are some cases:
1. Either A has a common factor.
2. B has a common factor. 
3. may be both has common factor.
lets take case 1 
we we multiply it with any positive number the resultant will be always not coprime with k.
same if B multiply with B with any number that will be always not coprime with k.

so i will find out the numbers of elements from A with not coprime with K.
and for B also.
lets say A=[x1,x2,x3,x4]
         B=[y1,y2,y3,y4]
in A=[x2,x4],B=[y2] are not coprime with k.
if we multiply all A prime numbers elements to B elements then we have 
A*B=[x2*y1,x2*y2,x2*y3,x2*y4,x4*y1,x4*y2,x4*y3,x4*y4]
B*A=[x1*y2,x2*y2,x3*y2,x4*y2]
so if we observe here we have multiply some pairs twice 
so we have to reduce it from product.
"""
import math
def coprimeAgain2(A,B,K):
    count1=0
    count2=0
    for i in range(len(A)):
        if math.gcd(A[i],k)!=1:
            count1+=1
    for i in range(len(B)):
        if math.gcd(B[i],k)!=1:
            count2+=1
    res = (count1*len(B))+(count2*len(A))-(count1*count2)
    return res

#Time Comlexity:O((N+M)*log max_element)) where N and M are length of array.
#Space Complexity: O(1)