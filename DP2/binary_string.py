# Exercise 
"""
Description: Binary String
lenght of n binary string given and no of string of length n that do not should consecutive 1's.return the number of string.
eg : if N=1 
    [0,1] ans  = 2
    if N=2
    [00,01,10,11] , here we find out 11 is consecutive , so we will not consider it .
    answer = 3
"""
# Bruteforce
"""
1. generate the every possible string store some where and check the patter is valid or not .
2. Same time update a count variable return count .
"""
#Time Compexity(N*2^N)
#Space Compexity(N)

# Optimized Approach:
"""
1. Take N=1 ,ans is 1 , [0,1]
2. Take N=2 ,ans is 3, [00,01,10]
3. if we are at ith position of a string and at ith element has 0  so i-1th element can be zero or one . the number of ways will be always arr[i-1] ith.
4. if at i-1th index is one then we will consider remaining ith element must be zero . so if we fix the i-1th and ith element. Then we will get arr[i-2] answers.
5 .Recurrence Relation : arr[i] = arr[i-1]+arr[i-2]
"""
# code
def binary_string(n):
    if n==0:
        return 1
    arr = [0]*n
    arr[1] = 2
    arr[2] = 3
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]
# Time Comlexity:O(N)
# Space Comlexity:O(N)

