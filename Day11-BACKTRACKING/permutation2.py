"""
Exercise: find out all the unique permutation .A case when string is repeatative 
for eg.
    Input: AAB
    Output:
          AAB
          ABA
          BAA
"""
#Bruteforce Approach
"""
We are using backtracking technique so if i will fix a A form AAB and calcute the the permutation of remaining string AB and every time i will fix every element at first place and concatinate the permutation of remaining string and take union of all .

let's see an example
          A+P(AB)
          A+P(AB)
          B+(AA)
if we see above example there is duplicate entry .so to aboid it .we will check at the time of swaping or fixing a element. Is this element is occured or not in between both that we will swap for fixing.
"""
#Code
def unique_permutation(A,index):
    if index==len(A):
        print(A)
        return
    for i in range(index,len(A)):
        flag=False
        for j in range(index,i):
            if A[i]==A[j]:
                flag=True
                break
        if flag:
            continue
        A[index],A[i]=A[i],A[index]
        unique_permutation(A,index+1)
        A[index],A[i]=A[i],A[index]

unique_permutation(['A','A','B'],0)

        
#Time Complexity:O(N2*N!) or O(N*(N!+N))
#Space Complexity:O(N)
                