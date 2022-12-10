# Exercise:
"""
Description:Dry state 
Person selling wine,Given wine cans .every wine has its cost associated with it.
person can sell wine constraint is from extream.
and at 1st year , person can earn can_cost*year 
y=1,p*1
y=2 p*2
What is the maximum profit that he can earn.
"""
# Bruteforce Approach
"""
lets say we have an array [1,4,2,3,5],
We have 2 choices.
1. At first we can sell 1 or 5 bottles ,
2. if we sell 1 then my profit is : 1*1+profit(1,4) or
3. If we sell 5 first then the profit is: 5*year+profit(0,3)
4. If we return maximum of both point 2 and point 3 that will be our answer.
#  BASE CASE
if the array has only one element then we return only can_cost*year.,By stack
"""
# Code:
def profit(arr,i,j,year):
    if i==j:
        return arr[i]*year
    return max(arr[i]*year+profit(i+1,j,year+1),arr[j]*year+profit(i,j-1,year+1))
# Time Complexity: O(2^N)
# Space Complexity:O(N),By stack


# Optimized Approach1
"""
1. if we observe the reccurence relation and break down will find something ,so we can
optimise it .
2.Given array [1,4,2,3,5]
3.We have 2 choices.
4. 1*y+profit(1,4) or 5*y+profit(0,3), if we break down further ,will see we are calculating same profit again and again.
5.if We store it some where when we calculate it first time then we don not need to calculate it again and again.
6. Here we have 3 varible changing on every sub structure for different possiblity.DP will go for 3D dimension.
7. if we observe our will always be y=len(arr)-1-(i+j).We rerduced it in 2D.
6. we use DP's memoization Approach(Bottom-Up).
"""
# Rules
"""
1.Find go for brute force.
2.Then find sub problem that will help to calculate the answer using it.
3.Then find out optimal substructure(overlapping subproblem).
"""
# Code
def profit(arr,i,j,dp):
    y=len(arr)-1-(i+j)
    if i==j:
        return arr[i][j]*y
    if dp[i][j]!=-1:
        return dp[i][j]
    dp[i][j] = max(arr[i]*y+profit(arr,i+1,j,dp),arr[j]*y+profit(arr,i,j-1))
    return dp[i][j]
# Time Complexity:O(N*N)
# Space Complexity:O(N*N)+stack memory

# Optimized Approach 2 (Tabulation Approach (Top-Down Approach))
"""
1.In memoization Approach shell[i][j] is storing the max profit from i to j substructure.using this information:-
2. Take an 2d matrix of len(arr)*len(arr)
3. If fill base for all .After that if we will see before base case values must be zero reason is we can find data index 1 to 4 , we can find 4 to 1 reason is 1st position element will come first , if we choose 1st element .
4. if we see above reccurence relation we need profit[i+1][j] and profit[i][j-1].
5. We must proceed diagonally.
"""

# Time Complexity:O(N*N)
# Space Complexity:O(N*N)