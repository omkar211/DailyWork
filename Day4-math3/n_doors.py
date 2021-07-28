"""
Question: N-door 
     Problem Statements
     There are 100 doors intial all the doors are closed .
     at a 1st step all the doors will toggle and opened 
     at a 2nd step every door from intially toggled if there are closed 
     turnout to be open or open one will be closed.
     find the total number of gates open.
"""
#Clarification:
"""
1.if array is empty then what should be returning.
2.array limit is less than N doors what should be returning.
3. so every step we have to toggle door at every step distance.

"""
#Solution:
"""
1. So let say there are n doors so . we will take an array with size of n and default intialized by 0. zero means all doors are closed and 1 means all the doors are open
2. from first step we will jump to the step distance and toggle it. if door is open then closed. if door is open then we will closed.
"""
#Code:
def ndoors(N):
     door=[0]*N
     for i in range(1,N):
          for j in range(i,N):
               if door[j]==0:
                    door[j]=1
               else:
                    door[j]=0
     ans=[]
     for i in range(N):
          if door[i]:
               ans.append(i)
     return ans

#Time Complexity : O(NLogN)
#Space Complexity : O(N)


#Solution 2:
"""
If we observe from problem initially all the gates are closed. at first step all are opened, at second
step every second element will be toggled.and so on....
1.Those numbers who is toggled odd times will always be opened doors rest are closed.
2. lets take a number X which will only divisible by all its factors. so count the factors. find out which number has odd numbers of factor will be are answer.
"""

#Code:
def ndoors(n):
     