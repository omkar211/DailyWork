# Exercise
"""
Problem:
Given a n ,findout the nth fibonacci.
"""
# Approach1:
"""
1. for find nth fib number we need n-1th and n-2th fib,so recurence relation will be.
   fib(n) = fib(n-1)+fib(n-2)
2. Base case: we know that 1st fib is 0 and second is 1 so if n==0 or n==1 we can return n.
"""

def fib1(n):
    if n==1 or n==0:
        return n
    return fib(n-1)+fin(n-2)
# Time Complexity:O(2^N)
# Space Complexity:O(N)

# In above approach there is lot of redundancies-> overlapping subproblems there.like we are calculating sub-part of a problems many times.

# Approach2 memoization approach(Top down Approach)
"""
What if we cache the smaller problem result inorder to solve the bigger problem. 
1. that comes Dynamic problem ->memoization approach
2. So to get the nth number of fib, we can take dict .
"""

def fib2(n,dt):
    if dt.get(n):
        return dt[n]
    dt[n-1] = fib(n-1)
    dt[n-2] = fib(n-2)
    return dt[n-1] + dt[n-2]
dt = defaultdict(lambda:0)
dt[1] = 1
fib2(n,dt)

# Time Complexity:O(N)
# Space Complexity:O(N)


# ***********************IMPORTANT************************
#  Approach3 tabulation approach( Bottom UP Approach)
"""
1.In this appoach , from the begainning maintain the solution of sub-problems and step by step 
will go solve the bigger the problem using the smaller problem solution.
2. Recurrence relation :     arr[n] = arr[n-1]+arr[n]
"""

def fib3(n):
    arr = [0]*n
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[n-1]+arr[n-2]
    return arr[n]
# Time Complexity : O(N)
# Space Compelxity : O(N)


#  Approach4 tabulation approach( Bottom UP Approach)
"""
1. More Optimzed Solution 
2. take 2 pointer to maintain to get nth fib , one pointer hold n-1th and another one will hold n-2th fib solution.
3. Every time we add up and calculate nth fib and update the pointer.
"""
def fib4(n):
    first = 0
    second = 1
    ans = 0
    for i in range(2,n+1):
        ans = first + second
        first = second
        second = ans 
    return ans
# Time Complexity:O(N)
# Space Complexity:O(1)
