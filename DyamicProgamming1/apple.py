# Exercise:
"""
Given an apple that are hanging selling in a house.and there are 2 types of person one who can party in pair and one who can party alone.
How many ways can they party?
"""
# Approach:
"""
Note: We are assumming we already calculated the number of ways till i-1th people inorder to calculate the ways for ith people.
1. We will pick the ith people and ask the number of ways.
2. So for ith boy there 2 possibility one is:- first possibility ith people can party single for that the number of ways will be (i-1)th people ways. And for second possibility , pair with someone the number of ways will be , ith people can be pair with (i-1) people and let's say if it makes pair with i-1 th people then the number of ways for remaining people will be (i-2)th people ways.
3. So if We calculate the same for every group it will be (i-1)*arr[i-2]
RECURRENCE RELATION will be : arr[i] = arr[i-1]+i-1*(arr[i-2])
"""
# Code
def ways(n):
    arr = [0]*(n+1)
    arr[1] = 1
    arr[2] = 2
    for i in range(3,n+1):
        arr[i] = arr[i-1]+(i-1)*arr[i-2]
    return arr[n]
#Time Complexity:O(N)
# Space Complexity:O(N)