# Exercise
"""
Description:
Given N Houses and every house have some money and connnected to each other and theif has to rob teh money from houses and maximize the max-money robbed.

CONNTRAINT:
if thief rob ith house then it can not rob i-1 and i+1
"""

# Bruteforce Approach
"""
1. include ith house once and include ith not take up max and store it in global variable.
"""
res = 0
def rob(house,index,_sum):
    if index == len(house):
        return True
    res = max(res,_sum)
    rob(house,index+2,_sum+house[index])
    rob(house,index+1,_sum)
    
rob(house,0,0):


# Time Complexity:O(2^N)
# Space Complexity:O(N)



# Optimized Approach
"""
let's make recurrence relation:
1. if house = 1 ,then return 1
2. if house = 2 ,then return max(house[0],house[1])
3. if house = i , there will 2 cases, first case is if  house[i] include then it will be house[i-2]+house[i] and for second case if we do not include house[i], then simply robbed money will be till house[i-1]
4. Recurrence Relation  = ans[i] = max(house[i-1],(house[i]+house[i-2]))
"""
def rob(house):
    res = [0]*(len(house))
    res[0] = house[0]
    res[1] = max(house[0],house[1])
    for i in range(2,len(house)):
        res[i] = max(res[i-1],(res[i]+res[i-2]))
    return res[n-1]

#Time Complexity:O(N)
#Space Complexity:O(N)