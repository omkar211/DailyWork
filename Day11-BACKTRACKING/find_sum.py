"""
Exercise : Find sum
problem statement:
we have given N find the sum from 1 to N
"""
#Bruteforce Approach
"""
If we calculate the sum from 1 to n-1 and add up N into it and return the answer.
"""
#Code
def find_sum(N):
    if(N==1):
        return 1
    return N+find_sum(N-1)

#Time Complexity:O(N)
#Space Complexity:O(N)