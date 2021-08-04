"""
Exercise:Every number occers twice except 2 numbers .so find out these numbers.
        eg:[1,2,4,3,2,1]
        output here is 3,4
"""
#Solution1:
"""
We will sort the array and check for adjacent elements if occurance of A[i] is twice then we will move for next element of an array else we will keep the A[i] element and go for finding second element in an array.
"""
#Code
def two_numbers(A):
    A.sort()
    res=[]
    count=0
    i=0
    while(i<len(A)-1):
        if A[i]!=A[i+1]:
            res.append(A[i])
            count+=1
            if count>1:
                return res
            i+=1
        else:
            i+=2
    if count==1:
        res.append(A[-1])
    return res

#Time Complexity:O(NlogN), where N is size of an array
#Space Complexity:O(N)
print(two_numbers([1,2,3,4,2,1]))
#Solution2:
"""
1.lets take an example [1,2,8,6,2,1],here answer is 6,8.
2. we know that every element is occuring twice except these two.
3. And also know that these 2 numbers have some different set bits and different unset bits .
4. On the bases of set bit or unset bit choose any one of them , if we divide in 2 buckets according to a perticular set bit then some elements are the side of A and others will be side of B in pairs.
5. so xor  both the buckets differently and using the A^A=0, we have remained only with 1 element in each that will be our answer.
"""
#Code
def two_Numbers2(A):
    res=0
    ans1=0
    ans2=0
    bucket1=[]
    bucket2=[]
    for i in A:
        res=res^i
    index=-1
    for i in range(32):
        if (res&(1<<i))>>i:
            index=i
            break
    for i in range(len(A)):
        if (A[i]&(1<<index))>>index:
            bucket1.append(A[i])
        else:
            bucket2.append(A[i])
   

    for i in range(len(bucket1)):
        ans1=ans1^bucket1[i]

    for i in range(len(bucket2)):
        ans2=ans2^bucket2[i]
    return[ans1,ans2]

print(two_Numbers2([1,2,3,4,2,1]))

#Time Complexity:O(N),N is size of the A
#Space Complexity:O(N)