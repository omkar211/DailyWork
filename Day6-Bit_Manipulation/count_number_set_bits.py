"""
Exercise: Count number of set bits of N .
"""
#solution:
"""
if we right shift N by 1 and added up using AND operator with 1 if the output is 1 it means it is set bit and till N is equals to zero.
"""
#Solution:
def count_number(N):
    count=0
    for i in range(32):
        if (N>>i)&1:
            count+=1
    return count
#Time Complexity : O(N),N = 32
#Space Complexity : O(1)

#Solution 2:
"""
We know that N&N-1 unsets the right most bit. so we try to unset all the bit till N==0 and same time we maintain count.
"""
def count_number(N):
    count=0
    while(N):
        count+=1
        N=N&(N-1)
    return count
#Time Complexity: O(1)
#Space Complexity :O(1)

