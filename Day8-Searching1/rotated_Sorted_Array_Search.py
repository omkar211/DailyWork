"""
Exercise: Rotated Sorted Array Search
   Problem Description
Given a sorted array of integers A of size N and an integer B.
array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
You are given a target value B to search. If found in the array, return its index, otherwise return -1.
You may assume no duplicate exists in the array.
NOTE: Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 10^9
all elements in A are disitinct.

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return index of B in array A, otherwise return -1

Example Input
Input 1:
A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4

Input 2:
A = [1]
B = 1

Example Output
Output 1:
 0

Output 2:
 0

Example Explanation

Explanation 1:
Target 4 is found at index 0 in A.

Explanation 2: 
Target 1 is found at index 0 in A.
"""
#BruteForce approach
"""
we can check each and every element if it is equal to k then return index .else -1
"""
def find_key(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
    return -1
#Time Complexity : O(N)
#Space Complexity : O(1)

#Optimised Approach
"""
A = [4, 5, 6, 7, 0, 1, 2, 3]
So here we can see our last element of the array is always smaller than arr's first element .below are few cases
1 . if median element is smaller than the last element of the array it means median to last element of the array part every thing is sorted. and will check if our 'key' is greater than median and less than last element of the array then we can search using binary search.
2 . if our median is greater than arr's first element it means left part is sorted from median so we will check if our key lies in b/w this range then search else move to our search to the right part.
"""

#Code
def find_key(arr,key):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>arr[start]:
            if key<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if key>arr[mid]:
                start=mid+1
            else:
                end=mid-1
    return -1
#Time Complexity : O(logn)
#Space Complexiyt : O(1)

