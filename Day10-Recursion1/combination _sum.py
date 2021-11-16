"""
Exercise:Combination Sum II
Problem Description
Given an array of size N of candidate numbers A and a target number B. Return all unique combinations in A where the candidate numbers sums to B.
Each number in A may only be used once in the combination.
NOTE:
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
my approach is take once in a sum element and once not if sum <target value.
I will first sort the array and lets say my array is [1,1,1,1,2] and B=3. if I sum up 1st to 3rd element then sum equals to my target value and i return to 2nd element and again not consider 3rd one so time to add element 4th in a sum ,if i add up this element then this combination is repeatative .so i wil skip this element also.and addup next element if it is not same as 3rd element.
"""
#Code 

def combination2(A,index,B,temp,total):
    if index==len(A):
        return        
    if total==B:
        print(temp)
        return
    if total>B:
        return 
    temp.append(A[index])
    combination2(A,index+1,B,temp,total+A[index])
    while(index+1<len(A) and A[index]==A[index+1]):
        index+=1
    temp.pop()
    combination2(A,index+1,B,temp,total)

combination2([1,1,1,1,2,3],0,3,[],0)