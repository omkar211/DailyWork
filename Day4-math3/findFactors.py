"""
Question: find factor 
        Problem Statement
Given a Number we have to find all the factors of N.
"""
#Clarificatio:
"""
1.if N==0, what should we returning.
2.is this contains negative numbers.

"""
#Solution:
"""
We will traverse through a loop from i=1 to N and if i divides the N We will keep in a result list.
"""
#Code
def findfactor(N):
    res=[]
    for i in range(1,N+1):
        if N%i==0:
            res.append(i)
    return res

print(findfactor(20))
# result : [1, 2, 4, 5, 10, 20],
#Time Complexity : O(N)
#Space Complexity : O(N) While returning res

#Solution 2:
"""
if we observe above result so every time second last factor of N is always <=N/2,thatswhy we have to go only till N/2 and handle last factor seperately.
"""
#Code
def findfactor2(N):
    res=[]
    for i in range(1,N//2+1):
        if N%i==0:
            res.append(i)
    res.append(N)
    return res

print(findfactor2(60))
#Time Complexity : O(N), but N=N/2,asympotically is same but have improved then previous one .
#Space Complexity : O(N)

#Solution 3:
"""
let's find out the factor of 60.
res = [1,2,3,4,5,6,10,12,15,20,30,60]
so here 
(1,60)-->forming  60 =1*60
(2,30)-->forming  60 =2*30
(3,20)-->forming  60 =3*20
(4,15)-->forming  60 =4*15
(5,12)-->forming  60 =5*12
(6,10)-->forming  60 =10*6

1.if do not need to find half of the factors because  if 'i' is a factor then 'N/i' will be another factor.
2.but challenging part is which till point  we have to calculate .so in above example the last point    6 which is middle of all the res array .in order to find second factor :
       f is first factor then N/f is second factor 
       and f and N/f is almost closest factors among all the factors .
       so we can make assumption f=N/f
       so f=N^1/2
3. To find out all the factors we only need to go till sqrt(N).
"""
#Code:
import math 
def findfactor3(N):
    res=[]
    for i in range(1,int(math.sqrt(N))):
        if N%i==0:
            res.append(i)
            res.append(N//i)
    return res 
print(findfactor3(60))

#Time Complexity : O(sqrt(N))
#Space Complexity : O(N)
 