"""
Exercise: Aggressive cows

Problem Description:-
Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.
His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.
Output Format
Return the largest minimum distance possible among the cows.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 3
Input 2:

A = [1, 2]
B = 2

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:
John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
So the minimum distance will be 2.
Explanation 2:
The minimum distance will be 1.
"""

# Clarification:
"""
1.if B>N
2.if B=0
"""
#Bruteforce:
"""
Let's say we have given an array [x1,x2,x3,x4,x5,x6] and number of cows 'B=3'.Now i will place cows at x1,x2 and x3. and store min distance .Now at second time i will place these cows at x1,x2 and x4. and compare the min distance with previous one.So i will place cow at every place and record min distace.
"""

#Code
def helper(A,B,index,res,temp_store):
    if(index>=len(A)):
        return 
    if(B==0):
        local_res=temp_store[-1]
        for i in range(len(temp_store)-1):
            local_res = min(local_res,temp_store[i+1]-temp_store[i])
        res=max(local_res,res)
        return
    temp_store.append(A[index])
    helper(A,B-1,index+1)
    temp_store.pop()
    helper(A,B,index+1,temp_store)

def cow_placed(A,B):
    if B>len(A) and B==0:
        return -1
    temp_store=[]
    helper(A,B,0,0,temp_store)

#Time Complexity:O(N*2^N)
#Space Complexity:O(N)

#Optimized
"""
If we guess the min distance b/w two cows that will be in 0 and last element of the array.
so we will every time guess the min distance and check if this min is valid or not .if valid then another min diatace can be at right side of it else go for left side of it .
"""

#Code

def check(mid,A,B):
    for i in range(len(A)-1):
        if(A[i+1]-A[i]>=mid):
            B-=1
    if B<=0:
        return True
    return False
def cow_placed2(A):
    A.sort()
    low=0
    high=A[-1]
    while low<high:
        mid=(low+high)//2
        if check(mid):
            res=max(res,mid)
            low=mid+1
        else:
            high=mid-1

#Time Complexity:O(max(NlogMax,NLogN))
#Space Complexity:O(N)