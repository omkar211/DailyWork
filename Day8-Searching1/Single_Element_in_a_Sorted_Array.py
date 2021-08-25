"""
Exercise:
        Single Element in a Sorted Array
Problem Description
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.
NOTE: Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9

Input Format
The only argument given is the integer array A.
Output Format
Return the single element that appears only once.

Example Input
Input 1:
A = [1, 1, 7]
Input 2:
A = [2, 3, 3]

Example Output
Output 1:
 7
Output 2:
 2

Example Explanation
Explanation 1:
 7 appears once

Explanation 2:
 2 appears once
"""
#Solution1:
"""
By using the (A XOR A) = 0 property so we xor the whole the array by picking one by one.In last we remained with only with single element.
"""
#Code
def single_element(A):
    res=0
    for element in A:
        res=res^element:
    return res
#Time Complexity:O(N)
#Space Complexity:O(1)


#Solution2:
"""
                      0 1 2 3 4 5 6 7 8 9 10 11 12
lets take an example [1,1,2,2,3,3,4,5,5,6,6, 7, 7]
1.if we observe in above example before single element occurence of every element is at even place and after the occurence of single element evey element is occuring in odd index.
2.so i can choose any element from an array and check its index+1 and index-1 if element has single occurence then return element.
3. if an element first occurence id at even place than our desired output will be at right to the index .
4. if first occurence is at odd place then our desired output will be at left of the index.
5. so for searching and key  here we use binary search , because an array is sorted and has a patterns
"""
def single_element2(A):
    low=0
    if len(A)<=1:
        return A
    high=len(A)-1
    while(low<=high):
        mid=(high+low)//2
        if mid ==0:
            if A[mid]==A[mid+1]:
                low=mid+1
            else:
                return A[mid]
        elif mid==(len(A)-1):
            if A[mid]==A[mid-1]:
                high=mid-1
            else:
                return A[mid]
        elif A[mid]!=A[mid+1] and A[mid]!=A[mid-1]:
            return A[mid]
        elif mid&1:
            if A[mid]==A[mid-1]:
                low=mid+1
            else:
                high=mid-1
        else:
            if A[mid]==A[mid-1]:
                high=mid-1
            else:
                low=mid-1
    return -1

#Time Complexity:O(logN)
#Space Complexity:O(1)