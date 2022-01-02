#Exercise:Subarray sum:
"""
Given an unsorted array A of size N.
return True if there is a subarry present in an array whose sum is ZERO. 
"""
#Bruteforce:
"""
1. sort the array
2. I will calculate all the sub_array and check all the sub_array sum equals to the Zero or not.
"""
# Timecomplexity:O(N^3)
#Space Complexity:O(N)

# Optimized Approach
"""
lets take an array [6,-1,2,-1,1] 
lets calculate the sum of all prefix of an above array 
                [6,-1,2,-1,1] 
                A[0]=6
                A[0]+A[1]=5
                A[0]+A[1]+A[2]=7
                A[0]+A[1]+A[2]+A[3]=6 ,As we can see here this sub_array sum and A[0] sum is equal .So if sum is repeatimg it means b/w index[1,3] sum will be zero.
So we can store prefix sum and check if it occurs twice at any point, then we can simply return the index or return True 
"""
#Code
def sub_array(A):
    dt={}
    temp=0
    for i in range(len(A)):
        temp+=A[i]
        if dt.get(temp,False):
            return True
        else:
            dt[temp]=True
    return False
print(sub_array([6,-1,2,-1,1]))

#Time complexity:O(N)
#Space complexity:O(N)
