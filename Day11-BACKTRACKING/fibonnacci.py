"""
Exercise : fibonnacci
Problem Statements:
find the nth fibonacci number.n given.
"""
#Bruteforce Approach
"""
If i find out fib(n-1)+fib(n-2) then simply return that.and we know that fibonacci of 1 is 1 and 0's 0.
"""
#Code
def fib(N):
    if N<0:
        return 0
    if N==0 or N==1:
        return N
    return fib(n-1)+fib(n-2)

#Time Complexity:O(N)
#Spac Coplexity:O(N)
    
