"""
Given an stack reverse it and return the same stack. and use only stack for any purpose
"""
#Bruteforce Approach:
"""
1.Take a S1 stack store all the element of given stack and for S1 pick all the element insert it into S2 and take all the elements insert back in given stack that will be our answer. 
"""
#Code
def reverse_stack(S):
    S1=[]
    S2=[]
    while len(S)>0:
        S1.append(S.pop())
    while len(S1)>0:
        S2.append(S1.pop())
    while len(S2)>0:
        S.append(S2.pop())
    return S

#Time Complexity:O(N)
#Space Complexity:O(N)