#Exercise:Merse Sort
"""
"""
#Code

def merge_sort(A,low,mid,high):
    low_index=low
    high_index=mid+1
    res=[]
    while(low_index<=mid and high_index<=high):
        if(A[low_index]<A[high_index]):
            res.append(A[low_index])
            low_index+=1
        else:
            res.append(A[high_index])
            high_index+=1
    res=res+A[low_index:mid+1]
    res+=A[high_index:high+1]

    k=0
    for i in range(low,high+1):
        A[i]=res[k]
        k+=1

def merge(A,low,high):
    if low>=high:
        return 
    mid=(low+high)//2
    merge(A,low,mid)
    merge(A,mid+1,high)
    merge_sort(A,low,mid,high)


A=[1,3,4,2,2]
merge(A,0,4)
print(A)

#Time Complexity:O(NlogN)
#Space Complexity:O(N)
