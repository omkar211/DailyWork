#Question:
"""
            Problem statement
Given a range of Q queries to find out the N is prime or not ?
1<=Q<=1000
return all the prime between given range 1 to 1000 .
"""
#Clarification:
"""
Is Contains negative number ?
what should i return while out of range ?
"""
#Solution1 :
"""
so we have given a range[2,N] . take a loop from  i=2 to N and find out that i is prime or not using calculateprime.py
nodule
"""
#Code
from calculateprime import*
def qprimenumbers(N):
    lst=[]
    for i in range(2,N+1):
        if(prime2(i)):
            lst.append(i)
    return lst

# print(qprimenumbers(10))

#Time Complexity: O(Q*N^1/2)
#Space Complexity: O(N)

#Solution2:
"""
if We precalculate the primes and store the range in a array and return the every Qqueries in O(1) time that will be 
our answer.
Question is How we can calculate..
lets say to finding a number is prime or not the number should not be divisible by any number except 1 and it self. so we know that every number is itself prime or contains factor of prime .so here i will mark the numbers whoever divisible by prime factor till N.so at 1st step we cross multiplwe of 2 and mark the numbers that they are not prime.so on.....
so if i take an boolean array size of N and initialize with it by 0. and
"""
import math
def sievePrime(N):
    lst=[N+1]*True
    # lst[0]=False
    # lst[1]=False
    for i in range(2,int(math.sqrt(N))+1):
        if lst[i]:
            for j in range(i*i,N+1,j+i):
                lst[j]=False
    return lst
lst=sievePrime(50)
for i in range(len(lst)):
    if lst[i]:
        print(i)

