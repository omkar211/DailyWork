"""
Question: Enumerating GCD
                 Problem Description
You are given a number A and a number B. Greatest Common Divisor (GCD) of all numbers between A and B inclusive is taken (GCD(A, A+1, A+2 ... B)).
As this problem looks a bit easy, it is given that numbers A and B can be in the range of 10100.
You have to return the value of GCD found.
Greatest common divisor of 2 numbers A and B is the largest number D that divides both A and B perfectly.

Problem Constraints
1 <= A <= B <= 10100

Input Format
First argument is a string denoting A.
Second argument is a string denoting B.

Output Format
Return a string which contains the digits of the integer which represents the GCD. The returned string should not have any leading zeroes.
Example Input
A = "1"
B = "3"

Example Output
1
Example Explanation
Greatest divisor that divides both 1 and 3 is 1.
"""

#Solution 1:
"""
take a pointer which starts from A goes till B. and calculate the gcd of every number.
gcd(gcd(A,B),C)...
"""
#Code
def gcd(A,B):
    if B==0:
        return A
    return gcd(B,A%B)
def enumerating(A,B):
    res=A
    for i in range(A+1,B+1):
        res=gcd(res,i)
    return res
#Time Complexity:O(N*log(max(A,B))) ,where N = B-A
#Space Complexity:O(log(max(A,B)))

#Solution 2:
"""
let say A=even & B = even/odd
then A+1 must be a odd or vice versa.
so gcd(odd,even)=always be a 1.
if both of the number are equal then return A else it will always be '1'.
"""

#Code 
def enumerating2(A,B):
    if A==B:
        return A
    return '1'
#Time Complexity: O(1)
#Space Complexity:O(1)