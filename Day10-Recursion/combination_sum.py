"""
Exerise :Cobination sum
Problem Description
Given a set of candidate numbers A and a target number B, find all unique combinations in A where the candidate numbers sums to B.
The same repeated number may be chosen from A unlimited number of times.
Note:
1) All numbers (including target) will be positive integers.
2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
3) The combinations themselves must be sorted in ascending order.
4) CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR ... (a1 = b1 AND a2 = b2 AND ... ai = bi AND ai+1 > bi+1)
5) The solution set must not contain duplicate combinations.

Problem Constraints
1 <= |A| <= 20
1 <= A[i] <= 50
1 <= B <= 500

Input Format
First argument is the vector A.
Second argument is the integer B.

Output Format
Return a vector of all combinations that sum up to B.

Example Input
Input 1:
A = [2, 3]
B = 2
Input 2:
A = [2, 3, 6, 7]
B = 7

Example Output
Output 1:
[ [2] ]
Output 2:
[ [2, 2, 3] , [7] ]

Example Explanation
Explanation 1:
All possible combinations are listed.
Explanation 2:
All possible combinations are listed.
"""
#Brute Force 
"""
I will take an array and add same element till sum equals to the target sum if greater then i will simply return .and try new combination and to remove duplicate combination ,I'll check if ith element i considered previously exist or not .
"""
#Code
def combination_sum(A,index,res,temp_list,total,B):
    if total>B:
        return 
    if index>=len(A):
        return 
    if total==B:
        temp=[]
        # print(temp_list)
        for i in range(len(temp_list)):
            temp.append(temp_list[i])
        res.append(temp)
        return
    while(index<len(A)-1):
        if A[index]!=A[index+1]:
            break
        index+=1
    temp_list.append(A[index])
    combination_sum(A,index,res,temp_list,total+A[index],B)
    temp_list.pop()
    combination_sum(A,index+1,res,temp_list,total,B)
res=[]
temp_list=[]
combination_sum([1,2,3,5,6],0,res,temp_list,0,3)
print(res)

#Time Complexity:O()
#Space Complexity:O(N)