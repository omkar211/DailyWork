"""
Given an array,return the no of non-empty subarray such that the left most element of sub-array is not larger than other elements of the subarray return count.
eg:[1,4,2,5,3]
output:[1],[4],[2],[5],[3],[1,4],[1,4,2],[1,4,2,5],[1,4,2,5,3],[2,5],[2,5,3]
"""
#Bruteforce Approach:
"""
1. first pick every element and check it for satisfying the condition
2. pick the range in between u want to choose.
3. iterate over the range and check is left most element is smallest.then add it into result.
"""

#Code:
def subarray(A):
    count=0
    for i in len(A):
        for j in range(i,len(A)):
            if A[i]<A[j]:
                count+=1
            else:
                break
    return count+len(A)

#Time Complexity:O(N*N)
#Space Complexity:O(1)

#Optimised Approach
"""
1.take an above example,pick 2 adjacent elements where i<j and A[i]>A[j] then no need to consider it in our answer.
eg:[1,4,2,5,3]
2.pick first element and insert it in a array and add plus one in resultant and add second element 4 element and calculate the length of array that will give u the number of subarray which have left most element is smallest and add it to the resultant 
3. pick 3rd element 2. and check it is it greater than last element of the array then add the lenght of array in to the answer but it is smaller . so we remove last element because it voileting our condition ,
4.after removing it add it to array and add the length of the array in a resultant. and same for all....
"""
#Code
def subarray2(A):
    if len(A)==0:
        return 0
    tmp=[]
    count=1
    tmp.append(A[0])
    for i in range(1,len(A)):
        if A[i]>A[-1]:
            tmp.append(A[i])
        else:
            tmp[-1]=A[i]
        count+=len(tmp)
    return tmp

#Time Complexity:O(N)
#Space Complexity:O(N)