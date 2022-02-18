#Exercise:lexicographically_smallest
"""
Problem statement:
you are given a string.find all unique characters and must be c smallest.
eg:cbacdbbc 
output:acdb
"""
#Bruteforce:
"""
1.store all the unique character that is present in a string.
2.and generate all the subarrays and same time check for all the characters present in subarray.
3.then find the lexicographically smallest.and return it.
"""
#Optimized Approach 
"""
take an example:cbacdbbc
               1.lets say i have occuring frequency of every character.
               let say if i pick character c 
               and at second time b,i will check if frequency of c is greater than 1 . than it means c character is also after b character so i would consider it my answer rather than c before occuring to b becuase cb>bc i will choose second option. 
               2. so for implementing point 1 . i will take stack .
"""
#Code 
def laxi_smallest(string):
    stack=[]
    if len(string)<=0:
        return 0
    
    stack.appen(string[0])
    for i in range(len(1,string)):
        while len(stack)>0:
            if string[i]<stack[-1] and dt.get(string[i],False):
                stack.pop()
            else:
                stack.append(string[i])
                break
    res=""
    i=0
    while i<len(stack):
        res=res[:-1]+stack[i]
        i+=1
    return res

#Time Complexity:O(N)
#Space Complexity:O(N)
