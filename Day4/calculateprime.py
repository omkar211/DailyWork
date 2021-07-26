#Question 
"""
Calculate id n is prime or not ?
"""
#Clarifications:
"""
can n be a negative number?
what is the range of n?
"""
#solution1:
"""
We can call prime numbers only when a number is only have exactly 2 factors.here we will 
go from i= 1 to n and take a count if i divides n .we will increment i by 1 and if i>2 .
we will end the loop and return n is not prime. 
"""
#Code
def prime(N):
    count=0
    for i in range(1,N):
        if N%i==0:
            count+=1
        if count>2:
            return "N is Not Prime"
    return "N is Prime"

print(prime(37))
#Time Complexity : O(N)
#Space Complexity : O(1)

#Solution2 :
"""
lets take an example N=60
factors = 1,2,3,4,5,6,10,12,15,20,30,60
so here we can observe that second last factor always be <=N/2 and last factor we will handle seperately
"""
#Code :
def prime2(N):
    count =0
    for i in range(1,N//2+1):
        if N%i==0:
            count+=1
        if count>2:
            return "Not a Prime."
    return "N is Prime."

print(prime2(37))

#Solution3:
"""
N=60
factors = 1,2,3,4,5,6,10,12,15,20,30,60
if we see here above example factors are existing in pairs we can find an another factor by just dividing 
N/i if i is a factor of N.
so  the challenging part is on which point we have to go find the last factor f and N/f . so we can see in above example
6 and 10 are closed so N/f=f
so f=sqrt(N).so we have tpo till f .
"""
#Code 
import math
def prime3(N):
    count=0

    for i in range(1,int(math.sqrt(N))):
        if N%i==0:
            count+=1
        if count>2:
            return "N is Not Prime"
    return "N is Prime"

print(prime3(37))