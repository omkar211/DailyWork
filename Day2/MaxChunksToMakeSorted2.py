"""
Question:    Max Chunks To Make Sorted II 
          Problem Description
Given an array of integers (not necessarily distinct) A, if we split the array into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array.
What is the most number of chunks we could have made?

Problem Constraints
1 <= N <= 100000
-109 <= A[i] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return the maximum number of chunks that we could have made.

Example Input
 A = [2, 0, 1, 2]
Example Output
 2
Example Explanation
 We can split the array into two subarray one consisting element [2,0,1] and second one with only element [2].
 Sort them individually and concat them. The result will be sorted.
 """
 #Solution:
"""
if i pick a ith element in the array to not to make chunks every element from the 0 to i-1 must be less than equals to ith element.
if not then we have to make chunk from ith element
"""
#Code 

def max_chuck(arr):
    count=0
    for i in range(len(arr)):
        for j in range(i):
            if arr[j]>arr[i]:
                count+=1
                break
    return count
print(max_chuck([2,0,1,2]))
#Time Comlexity: O(N*N)
#Space Complexity:O(1) 

#Solution 2:
"""
if store the maximum element till the i-1th index for ith index then it is easy to trace the chunck on ith iondex.
"""
#Code
def max_chunk2(arr):
    count=0
    lst=[]
    lst.append(arr[0])
    for i in range(1,len(arr)):
        lst.append(max(arr[i-1],arr[i]))
    for i in range(len(arr)):
        if lst[i]>arr[i]:
            count+=1
    return count
#Time Complexity : O(N)
#Time Complexity : O(N)


