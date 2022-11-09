# Exercise
""""
Description:
you have given n steps long stair and you can take 1 step or 2 step to reach top of stair ,In how many ways a person can reach the stair of nth height.
""""
#Appoach1
"""
1. We know that if we get the (n-1)th steps ways and (n-2)th ways and add up that will be our answer.
2. Recurrence relation step(n) = step(n-1)+step(n-2) 
"""
def fun(n):
    if n==0 or n==1 or n==2:
        return n
    return fun(n-1) + fun(n-2)
# Time Complexity:O(2^N)
# Space Complexity:O(N)

# Approach 2
"""
Let's build recurrence relation
1. For n=1 , 1 steps 
2. for n=2, 2 steps
3. for n=3 , it will take 3 steps
"""
def steps(n):
    arr = [0]*n+1
    arr[1] = 1
    arr[2] = 2
    for i in range(3,n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]

# Time Complexity:O(N)
# Space Complexity:O(N)

# We can still  optimize the inorder to space O(n) to O(1)


