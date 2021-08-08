"""
Exercise:   Xor queries
    Problem Description
You are given an array A (containing only 0 and 1) as element of N length.
Given L and R, you need to determine value of XOR of all elements from L to R (both inclusive) and number of unset bits (0's) in the given range of the array.

Problem Constraints
1<=N,Q<=100000
1<=L<=R<=N

Input Format
First argument contains the array of size N containing 0 and 1 only. 
Second argument contains a 2D array with Q rows and 2 columns, each row represent a query with 2 columns representing L and R.

Output Format
Return an 2D array of Q rows and 2 columns i.e the xor value and number of unset bits in that range respectively for each query.
Example Input
A=[1,0,0,0,1]
B=[ [2,4],
    [1,5],
    [3,5] ]

Example Output
[[0 3]
[0 3]
[1 2]]

Example Explanation
In the given case the bit sequence is of length 5 and the sequence is 1 0 0 0 1. 
For query 1 the range is (2,4), and the answer is (array[2] xor array[3] xor array[4]) = 0, and number of zeroes are 3, so output is 0 3. 
Similarly for other queries.
"""
#Solution1:
"""
We have given Q queries in form of matrix and 2 column .so we will iterate over all queries and 
calculate the XOR from right to left and we will calculate the zeroes also .
"""
def find_xor(A,Q):
    res=[]
    for i in range(len(Q)):
        zeroes=0
        count_xor=0
        for j in range(Q[i][0],Q[i][1]+1):
            count_xor=count_xor^A[j]
            if A[j]==0:
              zeroes+=1
        res.append([zeroes,count_xor])
    return res

#Time Complexity:O(N*Q)
#Space Complexity:O(1)


#Solution2:
"""                                0  1  2  3  4  5  6
lets say we have given an array A=[a1,a2,a3,a4,a5,a6,a7] 
if we want to calculate the xor of L=2,R=5 
so it would be XOR(0 to 5) xor XOR(2,5) by using A^A=0. this property we have our desired xor values
1. So first we will store the prefix XOR in an array and prefix zeroes in another array .
and using the above property we will find results of Q queries.
"""
def find_xor2(A,Q):
    pre_zeroes=[]
    zeroes=0
    prefix_xor=[]
    res=[]
    prefix_xor[0]=A[0]
    for i in range(1,len(A)):
        pefix_xor.append(prefix_xor[-1]^A[i])
        if A[i]==0:
            zeroes+=1
        pre_zeroes.append(zeroes)
    for i in range(len(Q)):
        temp=0
        zero=0
        if(Q[i][0]!=0):
            tmp=prefix_xor[Q[i][0]-1]^prefix_xor[Q[i][1]]
            zero=pre_zeroes[Q[i][0]-1]-pre_zeroes[Q[i][1]]
        else:
            tmp=prefix_xor[Q[i][1]]
            zero=pre_zeroes[Q[i][1]]
        res.append([zero,temp])
    return res
#Time Complexity:O(N+Q)
#Space Comlexiyt:O(N)
