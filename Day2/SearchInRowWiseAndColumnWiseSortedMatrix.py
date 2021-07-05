"""
Question: Search in a row wise and column wise sorted matrix
          Problem Description
Given a matrix of integers A of size N x M and an integer B.
In the given matrix every row and column is sorted in increasing order. Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.

Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.

Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
-100000 <= B <= 100000

Input Format
The first argument given is the integer matrix A.
The second argument given is the integer B.

Output Format
Return the position of B and if it is not present in A return -1 instead.

Example Input
A = [[1, 2, 3]
     [4, 5, 6]
     [7, 8, 9]]

B = 2

Example Output
1011

Example Explanation
A[1][2]= 2
1*1009 + 2 =1011

"""
#Clarification: 
"""
1.It can contains duplicate Numbers?
2.It has negative numbers?
3.What should i return when size or matrix is zero
"""
#Solution 1:
""" 
Traverse on each and every cell and if it if the key is present then return 1 if not return -1.
"""
#Code:
def findNUmber(arr,key):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==key:
                return True

    return False
#Time Complexity:O(N*M)
#Space Complexity:O(1)


#Solution 2:
"""
we have given all the columns and all the rows are sorted in ascending order.
by using this information we can solve it.
so we know that every element in the first column and in last column has value greater than key and smaller or may be equal to the key.
so we find out that cell and using binary search algorithm we can find the value .because every sell is sorted.
arr[0][col 0 to m-1]>=key and arr[n-1][col 0 to m-1]

"""
# Code
def binarysearch(arr,key):
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid=low+(high-low)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1

def findNumber2(arr,key):
    row=-1
    for i in range(len(Analystarr)):
        if arr[i][0]<=key and arr[i][len(arr[0])-1]>=key:
            row=i
    if row>=0:
        col = binarysearch(arr[i],key)
        if col==-1:
            return col
        return (row * 1009 + col)
print(findNumber2([[1,2,3,4,5],[6,7,8,9,10]],6))
#Time Complexity: O(nlogm) where n is number of rows and m is number of col.
#Space Comlexity: O(1)