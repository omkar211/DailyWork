#Exercise:Same Element in array:
"""
Given an unsorted array of size N , delete minimum number of elements to make all the element in your array same.
"""
#Bruteforce:
"""
Calculate the frequency of every element and store some where and get the maximum numbers of frequency and return length -maximum frequency.
"""
#Code
def frequency(A):
    dt={}
    for i in range(len(A)):
        if dt.get(A[i],False):
            dt[A[i]]+=1
        else:
            dt[A[i]]=1
    res=0
    for value in dt.values:
        res=max(res,value)
    return len(A)-res
#Time Complexity:O(N)
#Space Complexity:O(1)
        