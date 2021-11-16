"""
Exercise:Movie threater
Problem Statement:
A student is sitting in a concentric movie threater. and has given a task to calculate all the seats in a threater and the information is given any two adjacents seats difference is 1.
"""
#Bruteforce Approach
"""
So i will solve this question using recursion ,let say student is sitting on the Nth seat so i will tell to N-1th to calculate the seats in threater and tell me the answer.So answer+1 seats present in my row.
"""
#Code
def seats(N):
    if(N==1):
        return 1
    return 2*seats(N-1)+1
#Time Complexity:O(N)
#Space complexity:O(N)
