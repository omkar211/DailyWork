"""
Exercise: Combination II
Problem Description
Given an array of size N of candidate numbers A and a target number B. Return all unique combinations in A where the candidate numbers sums to B.
Each number in A may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Warning:
DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python. If you do, we will disqualify your submission and give you penalty points.


Problem Constraints
1 <= N <= 20

Input Format
First argument is an integer array A denoting the collection of candidate numbers.
Second argument is an integer which represents the target number.

Output Format
Return all unique combinations in A where the candidate numbers sums to B.

Example Input
Input 1:
 A = [10, 1, 2, 7, 6, 1, 5]
 B = 8
Input 2:
 A = [2, 1, 3]
 B = 3

Example Output
Output 1:
 [ 
  [1, 1, 6 ],
  [1, 2, 5 ],
  [1, 7 ], 
  [2, 6 ] 
 ]
Output 2:
 [
  [1, 2 ],
  [3 ]
 ]

Example Explanation
Explanation 1:
 1 + 1 + 6 = 8
 1 + 2 + 5 = 8
 1 + 7 = 8
 2 + 6 = 8
 All the above combinations sum to 8 and are arranged in ascending order.
Explanation 2:
 1 + 2 = 3
 3 = 3
 All the above combinations sum to 3 and are arranged in ascending order.
"""
#Bruteforce Approach
"""
First i will make all the combination and strore some where in an array and check sum of same is sum is equals to the target ,then i return all those combinations.
"""
#Time Complexity:O(2^N)
#Space Complexity:O(2^N)

#Optimized Approach1:
"""
If we maintain a sum veriable to sum maintaining the sum of current combination then we can reduce extra space .
Time complexity will be same.
"""

#Optimized approach2
"""
If we sort the array and maintain the sum of a combination then we know that once our sum>target then we do not traverse a whole array. at wrost case the complexity is same but still we can save some traverse.
"""
#Code
def combination(A,index,temp,total,target,flag):
    if index==len(A) or total>target:
        return
    if total==target and flag:
        print(temp)
        return
    temp.append(A[index])
    combination(A,index+1,temp,total+A[index],target,True)
    temp.pop()
    while(index+1<len(A) and A[index]==A[index+1]):
        index+=1
    combination(A,index+1,temp,total,target,False)

def helper(A,target):
    A.sort()
    combination(A,0,[],0,target,True)
helper([1,2,3,4,2,4,5,5],8)

#Time Complexity:O(2^N)
#Space Complexity:O(N)
