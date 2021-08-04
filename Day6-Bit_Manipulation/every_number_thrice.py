"""
Every number is occuring 3 times.except one find out that number.
eg;[1,2,1,2,1,3,3,3,2,5]
output:5
"""
#Solution1:
"""
if we sort the array and pick a element and check the occuring of elements adjacently thrice or not if not return that will be our answer else oick another element.
"""
#Code
def thrice(A):
    A.sort()
    for i in range(0,len(A)-2,3):
        if A[i]!=A[i+1]:
            return A[i]        
#Solution2:
"""
Lets take an above example [1,2,1,2,1,3,3,3,2,5].
if expand its binary representation:
    0 0 1
    0 0 1
    0 0 1
    0 1 0
    0 1 0
    0 1 0
    0 1 1
    0 1 1
    0 1 1
    1 0 1
we know that every element is occuring 3 times . so at every place if bit is set or unset will be multiple of 3 .
so we here count the set bits and divide by 3 if remainder is not zero it means at this place bit is set else bit is unset.
"""
#Code
def thrice2(A):
    res=[]
    for i in range(32):
        set_bit=0
        for j in range(len(A)):
            if (A[j]&(1<<i))>>i:
                set_bit+=1
        if set_bit%3==0:
            res.append(0)
        else:
            res.append(1)
            # print(1)

    power=1
    ans=0
    for i in range(32):
        ans+=res[i]*power
        # print(res[i])
        power*=2
    return ans
print(thrice2([1,2,1,2,1,3,3,3,2,5]))

#Time Complexity:O(N),where N is size of an array
#Space Complexity:O(1),it goes till 32 only
