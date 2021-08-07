"""
Exercise:  
Different Bits Sum Pairwise
      Problem Description
We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.
You are given an array of N positive integers, A1, A2 ,..., AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.
Problem Constraints
1 <= N <= 105
1 <= A[i] <= 231 - 1
Input Format
First and only argument of input contains a single integer array A.

Output Format
Return a single integer denoting the sum.

Example Input
Input 1:
 A = [1, 3, 5]
Input 2:
 A = [2, 3]
Example Output
Ouptut 1:
 8
Output 2:
 2
Example Explanation
Explanation 1:
f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5) 
 = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8
Explanation 2:
f(2, 2) + f(2, 3) + f(3, 2) + f(3, 3) = 0 + 1 + 1 + 0 = 2
"""
#Solution:
"""
Here we find every pair and calculate the different bits using xor operators.
"""
#Code
def diff(A):
    res=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            tmp=A[i]^A[j]
            for bit in range(32):
                if (A&(1<<bit))>>bit:
                    res+=1
    return res
#Time Complexity:O(N*N),where N is size of array
#Space Complexity:O(1)


#Solution2:
"""
We know that XOR of opposite bits is always 1 . so if we calculate number os set bit and number of unset bit and make each pair choosing one by one bit from set bit and pair with it every unset bit once.
SO we are going at a time on 0th bit of every element of the array and then on 2nd and so on... 
"""
#Code
def diff2(A):
    res=0
    mod=1000000007
    for i in range(32):
        set_bit=0
        unset_bit=0
        for j in range(len(A)):
            if (A[j]&(1<<i))>>i:
                set_bit+=1
            else:
                unset_bit+=1
        res=(res%mod+(set_bit*unset_bit)%mod)%mod
    return res

#Time Complexity:O(N)
#Space Complexiyt:O(1)


