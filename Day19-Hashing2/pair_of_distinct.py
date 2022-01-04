#Exercise:Palindrome pair
"""
Given list of words(unique),find all the pairs of distinct indeces(i,j)
 word[i]+word[j]=palindrome .
 eg: [abcd,dcba,lls,s]

 Constaint:0>=N<=10^6
           1>=K<=50
 output:
       [(0,1),(1,0),(3,2)]
"""
#Bruteforce Approach:
"""
make all the pairs and check it for palindrome.
"""
#Code:
def is_palindrome(word):
    start=0
    end=len(word)-1
    while start<end:
        if word[start]!=word[end]:
            return False
        start+=1
        end-=1
    return True
def palindrome_pair(A):
    res=[]
    for i in range(len(A)):
        for j in range(len(A)):
            if i!=j:
                word=A[i]+A[j]
                if is_palindrome(word):
                    res.append([i,j])
    return res

# print(palindrome_pair(["abcd","dcba","lls","s"]))

#Time Complexity:O(N^2*K)
#Space Complxity:O(1),Exclude the res space

#Optimized Approach
"""
1.lets take an example ["abcd","dcba","lls","s"], if i  take 'lls' word from suffix if i pick "s" and rest word "ll" is palindrome.
2. And i will check by appending to word then it can be my answer.
lets take another example('dcba') is sub-word is:"",d,dc,dcb,dcba
lets if i find the reverse of sub-word then only i can say that one is palindrome :check d is present in array,same for all , if present then add to the answer. 
3.same for suffix.
4.To check word every time i will store it in dict(hashing) for getting O(1)
"""
#Code
def palindrome_pair2(A):
    res=[]
    dt={}
    dt[A[0]]=-1
    for i in range(1,len(A)):
        dt[A[i]]=i
    # prefix
    for i in range(len(A)):
        temp=""
        for k in range(len(A[i])):
            temp+=A[i][k]
            word=temp[::-1]
            # print(word)
            if is_palindrome(A[i][k+1:]) and (dt.get(word,False) and i!=dt[word]):
                if dt[word]==-1:
                    res.append([i,0])
                else:
                    res.append([i,dt[word]])
    return res
                
#T
print(palindrome_pair2(["abcd","dcba","lls","s"]))