#Exercise:generate_number
"""
Given an sorted array of integers and a value k. so print first N numbers that can be generated many digits inside given array.
eg: Input: 1 3 5 and k=6
    Output: 1,3,5,11,12,15

"""
#Bruteforce
"""
let say K is 10000, then we will generate numbers 10000 numbers by fixing 1st place like 1,3,5 and 11,13,15.....
and then we will fix 1st place and 2nd also like 111,113,115,131,133.......
and so on.
"""
#Code
def calculate(fix,A):
    for i in range(len()):
        res.append(str(1)+A[i])
def generate_number(A):
    if len(A)<=0:
        return A
    res=[]
    for i in len(A):
        calculate(i,A)
        temp=1