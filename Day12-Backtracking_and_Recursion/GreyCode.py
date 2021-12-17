#Code
def greycode(n,pattern):
    if n==1:
        return pattern
    temp=[]
    for i in range(len(pattern)):
        temp.append('0'+pattern[i])
    for i in range(len(pattern)-1,-1,-1):
        temp.append('1'+pattern[i])
    greycode(n-1,temp)

greycode(5,['0','1'])