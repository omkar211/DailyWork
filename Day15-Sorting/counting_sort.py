#Exercise: Counting Sort
"""
Given an array A of size N , where A=>[P,Q] ,P and Q are ranges, where array belongs to .
"""
#Code
def couting_sort(A,P,Q):
    freq=[0]*(Q-P)
    for i in range(len(A)):
        freq[A[i]-P]+=1
    prefix_sum=[]
    prefix_sum.append(freq[0])
    for i in range(1,len(freq)):
        prefix_sum.append(prefix_sum[-1]+freq[i])
    res=[0]*len(A)
    for i in range(len(A)):
        res[prefix_sum[A[i]-P]-1]=A[i]
    print(res)


couting_sort([1,2,3,5,4,6,7],1,7)