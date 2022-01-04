#Longest sub string 
"""
Given an string A size of N.find the largest substring with all distict character.
"""
#Bruteforce 
"""
We will take all the substring and check the every substring with distinct character and longest also .
"""
#Code:
def longest_substring(A):
    if len(A)==0:
        return 0
    res=0
    for i in range(len(A)):
        for j in range(i,len(A)):
            flag=True
            sub_string=A[i:j+1]
            sub_string=list(sub_string)
            sub_string.sort()
            sub_string = ''.join(sub_string)
            for k in range(len(sub_string)-1):
                if sub_string[k]==sub_string[k+1]:
                    flag=False
                    break
            if flag:
                res=max(res,len(sub_string))
            else:
                break
    return res
# print(longest_substring("abcdefcghitmpq"))

#Time Complexity:O(N^3logN+N)
#Space Complexity:O(N)

#Optimized Approach 
"""
In above approach we are dividing a string into substring for checking duplicate character in a string .If we already know at every index for duplicate character. then simply we can calculate the length of current substring by exclude the on which index we found the character +1 till index. and also we set a global varibale for updating result.
"""
#Code 
def longest_substring2(A):
    dt={}
    res=0
    starting_index=0
    for i in range(len(A)):
        if dt.get(A[i],False):
            starting_index=dt[A[i]]+1
            res=max(res,(i-starting_index+1))
            temp=starting_index
            while(temp>=0):
               del dt[A[temp]]
               temp=-1
        else:
            dt[A[i]]=i
            res=max(res,(i-starting_index+1))
    return res

print(longest_substring2("abcdefcghitmpq"))

#Time Complexity:O(N)
#Space Complexity:O(N)

