#Exercise: Longest Sub-array sum k
"""
Given an unsorted array of length N and K intger ,find out the longest length subarray of sum is equals to K.
"""
#Bruteforce
"""
1.Find out all the subarrays and check whose sum is equals to k and also checkits length and update it.
"""
#Time Complexity:O(N^3)
#Space Complexity:O(1)

#Optimized Approach
"""
lets take an array [x1,x2,x3,x4,x5,x6,x7,x8,x9],
            lets say y=x1+x2+x3+x4 and k=x5+x6
            and      prefix_sum = y+k
            so every time i store y somewhere and  check for y=PS-k if find out then store it and return.        
"""

#Code
def sub_array(A,K):
    dt={}
    total=0
    res=-1
    dt[0]=True
    for i in range(len(A)):
        total+=A[i]
        if dt.get(total-K,False):
            res=max(res,i-dt[total-K]+1)
        else:
            dt[total]=i+1
    return res+1
print(sub_array([6,1,-1,-1,6,2],7))
