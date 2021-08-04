"""
Exercise:
     find last set bit from the right of 2 numbers. if not found return -1.
"""
#Solution 1:
"""
If we right shift N by 1 and checked that most right bit is one or not if 1 then count how many times we shifted right and return it.
finding the bit is one or not we added up it using AND operator. 
"""
#Code
def set_bit(N):
    count=0
    for i in range(32):
        if (N>>1)&1:
            return count+1
        count+=1
    return -1
#Time Complexity:O(N),where N=32
#Space Complexity:O(1)
#Solution2:
"""
Let's take an example
N=10
binary = 1010
we know AND property if 1&1 gives you 1
so here we put 1 at place place if (1010&1)=0 it means at this place 0 bit exit and same time 
we update count varible.
so we chck at second place . if at second place bit is 1 then return count.
"""
#Code
def set_bit2(N):
    count=0
    if N&(1<<i):
        return count
    count+=1

#Time Complexity:O(N),where N=32
#Space Complexity:O(1)