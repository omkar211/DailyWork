"""
Question: A array contains N elements return 1 if the subsequence of the array contains gcd=1
else return 0
"""
#Solution: 
"""
So here we have to find all the subsequences and have to calculate the gcd if subsequence have gcd =1
return 1 else 0
"""
#Code
def gcd(A,B):
    if B==0:
        return A
    return gcd(B,A%B)
def subsequence(A,temp,index,res):
    if index==len(A):
        t=[]
        for i in temp:
            t.append(i)
        res.append(t)
        return 
    temp.append(A[index])
    subsequence(A,temp,index+1,res)
    temp.pop()
    subsequence(A,temp,index+1,res)
def helper(A):
    temp=[]
    res=[]
    subsequence(A,temp,0,res)
    for i in range(len(res)):
        if len(res[i])<=1:
            continue
        ans = res[i][0]

        for j in range(1,len(res[i])):
            ans=gcd(ans,res[i][j])
            if ans==1:
                return 1
    return 0
print(helper([2,2,4]))


#Time Compexity : (2^n+n2*log max)
#Space Complexity : O(N2)

#Solution 2:
"""
let say A=[a1,a2,a3,a4,a5,a6,a7,......,an]
lets pick two elements from array a2,a5 whose gcd(a2,a5)=1
so using commutive property  if we calculate the gcd of whole array with gcd(a2,a5) it will be always 1.
"""
#Code 
def helper2(arr):
    if len(arr)<=1:
        return "array has no 2 values"
    res=arr[0]
    for i in range(1,len(arr)):
        res=gcd(res,arr[i])
        if res==1:
            return 1
    return 0
#Time Complexity : O(n*log(max))
#Space Complexity : O(1)