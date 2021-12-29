#Exercise:Subarray with given sum
"""
Problem Description:
Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

If the answer does not exist return an array with a single element "-1".
First sub-array means the sub-array for which starting index in minimum.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:
 A = [5, 10, 20, 100, 105]
 B = 110

Example Output
Output 1:
 [2, 3]
Output 2:
 -1

Example Explanation
Explanation 1:
 [2, 3] sums up to 5.
Explanation 2:
 No subarray sums up to required number.
"""
#Code
def sub_array(A,B):
    prefix=[]
    if len(A)<=0:
        return "-1"
    prefix.append(A[0])
    for i in range(1,len(A)):
        prefix.append(A[i]+prefix[-1])
    start=0
    end=len(prefix)-1
    while start<end:
        if A[end]==B:
            return [start,end]
        elif A[end]-A[start]==B:
            return [start+1,end]
        elif A[end]-A[start]>B:
            end-=1
        else:
            start+=1
#Time Complexity:O(N)
#Space Complexity:O(N)

