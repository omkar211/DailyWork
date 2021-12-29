#Exercise: Count of pairs with the given sum
"""
Given a sorted array of distinct integers A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.
Input Format
The first argument given is the integer array A.
The second argument given is integer B.
Output Format
Return the number of pairs for which sum is equal to B.
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
1 <= B <= 10^9
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
    B = 5
Output 1:
    2

Input 2:
    A = [5, 10, 20, 100, 105]
    B = 110
Output 2:
    2
"""

#Code
def count_pair(A,B):
    start=0
    end=len(A)-1
    count=0
    while(start<end):
        tmp=A[start]+A[end]
        if tmp==B:
            count+=1
            start+=1
            end-=1
        elif tmp>B:
            end-=1
        else:
            start+=1
    return count
print(count_pair([1,2,3,4,5,6,7],6))

#Time Complexity:O(N)
#Space Complexity:O(1)