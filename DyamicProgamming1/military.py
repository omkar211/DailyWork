# Exercise :
"""
Problem : Military
Given a numbers of string .Now how many ways can this be decoded.
A:1
B:2
C:3
D:4
.
.
.
.
.
.
.
Z:26
eg:121
Possible string can be : ABA,MA,AV
ans = 3
"""
# Bruteforce Approach
"""
1. Iterate Over the string , there are 2 cases.
2. First case is pick a single number and get it's corresponding string.
3. Second case a number can be grouped with it's previous number and with it's next number.
4. and add the answers in global varible and return.
"""
# Code
ways = 0
def military(index,string):
    if index==len(string):
        ways+=1
        return True
    military(index+1,string)
    if int(string[index]+string[index+1])>=1 and int(string[index]+string[index+1])<=26:
        military(index+2,string)


# Time Comlexity:O(2^N)
# Space Comlexity:O(N)

# Optimized Approach:
"""
1. if string has once char then there is only one way .
2. if we have 2 char then there can we 2 possibility if string is in[1,26].
3. let's take an example 12,
    1. I know the ans of string till 0th index is 1.
    2. that is A if we append the last another character in all possibility the we will get same number of answers.
    3. and we include the i-1th character , themn we can say 
    ans = arr[i-1]+vailid()*ans[i-2]
"""
# Code
def valid(number):
    if number>=1 and number<=26:
        return 1
    return 0
def military(string):
    if len(string)<=1:
        return len(string)
    arr = [0]*len(string)
    arr[1] = 1
    arr[2] = 1
    if valid(int(string[0]+string[1])):
        arr[2] +=1
    for i in range(3,len(string)):
        arr[i] = arr[i]+valid(int(string[i-1]+string[i]))*arr[i-2]
    return arr[-1]


# Time Complexity:O(N)
# Space Complexity:O(N)