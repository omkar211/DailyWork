"""
Exercise: Hamming Distance
    Problem Statement:
    Given an array A contains n elements . find sum of haaming distance 
    take two numbers A and B 
    A=  1 0 1 1 
    B=  1 1 0 1
   res= 0 1 1 0 
   after xor we got hamming distace is 2. 
"""
#Solution1:
"""
we will pick all the pairs from array and calculate xor them and find out the number  of set bit we have and add up to a result.
"""
#Code 
def hammming_distance(A):
    res=0
    for i in range(len(A)):
        for j in range(len(A)):
            tmp=A[i]^A[j]
            for bit in range(32):
                if (tmp&(1<<bit)>>bit):
                    res+=1

    return res

#Time Complexity:O(N*N), where N is length of a array
#Space Complexity: O(1)

#Solution2:
"""
We know that xor of 1 and 0 will always return 1. if we calculate the set bit and unset bit at every place and find N choose 2 and add up with our solution.
"""
def hamming_distance2(A):
    
    for i in range(32):
        count_set_bits=0
        count_unset_bits=0
        for j in range(len(A)):
            if ((A[j]&(1<<i))>>i):
                count_set_bits+=1
            else:
                count_unset_bits+=1
        res+=count_unset_bits*count_set_bits
    return res
#Time Complexity:O(N)
#Space Complexity:O(1)
