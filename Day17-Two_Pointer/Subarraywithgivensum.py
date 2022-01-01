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
# Bruteforce Approach
"""
lets take an example [x1,x2,x3,x4,x5]. So to find out the sub-array i have to move i and j and same time i have to calculate the sum .
"""
#Time Complexity:O(N^3)
#Space Complexity:O(1)
def sub_array1(A,B):
    for i in range(len(A)):
        for j in range(len(i,len(A))):
            for k in range(i,j+1):
                total+=A[k]
            if total==B:
                return [i,j]
    return[-1]

# Approach 2
"""
In previous approach ,We are calculating the sub-array sum every time after deciding the sub-array.Rather than calculating seperately we can calculate it while we deciding it .
"""
#Code
def sub_array2(A,B):
    if len(A)==0:
        return [-1]

    for i in range(-1,len(A)):
        total=0
        for j in range(i+1,len(A)):
            total+=A[j]
            if(total==B):
                return [i+1,j]
            if total>B:
                break
    return[-1]

#Time Complexity:O(N^2)
#Space Complexity:O(1)

# Optimised Approach
"""

"""