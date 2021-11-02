"""
Exercise: Maximum height of staircase

Problem Description:
Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks.
The first stair would require only one block, the second stair would require two blocks and so on.
Find and return the maximum height of the staircase.

Problem Constraints
0 <= A <= 109

Input Format
The only argument given is integer A.

Output Format
Return the maximum height of the staircase using these blocks.

Example Input
Input 1:
 A = 10
Input 2:
 20

Example Output
Output 1:
 4
Output 2:
 5
"""
#Bruteforce Approach:
"""
start first step as given question first step take 1 block same time substract 1 from 'A' and second step substract A=A-2...so on.. 
"""

#Code 
def maximum_stairs(N):
    step=1
    while (N-step)>0:
        N-=step
    return step
#Time Complexity:O(N)
#Space Complexity:O(1)


#Optimized Approach
"""
if we choose randomly steps b/w 1 to N. lets say it is mid and calculated till the mid all the stairs in constant time then we can check for mid+1 to N.
"""
#Code 
def maximum_stairs2(N):
    low=1
    high=N
    res=0
    while(low<=high):
        steps=(low+high)//2
        count_blocks = steps*(steps-1)//2
        if N-count_blocks>=0:
            res=steps 
            low=step+1
        else:
            high=step-1

#Time Complexity:O(logN)
#Space Complexity:O(1)