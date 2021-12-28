#Exercise:Merge Overlapping Intervals
"""
Problem Description:
Given a collection of intervals, merge all overlapping intervals.

Problem Constraints
1 <= Total number of intervals <= 100000.

Input Format
First argument is a list of intervals.

Output Format
Return the sorted list of intervals after merging all the overlapping intervals.

Example Input
Input 1:
[1,3],[2,6],[8,10],[15,18]


Example Output
Output 1:
[1,6],[8,10],[15,18]

Example Explanation
Explanation 1:
Merge intervals [1,3] and [2,6] -> [1,6].
so, the required answer after merging is [1,6],[8,10],[15,18].
No more overlapping intervals present.
"""

#Code
def merge(A):
    res=[]
    p = pair(element[0].first,element[0].second)
    for element in range(1,len(A)):
        if p.second>=element[i].first:
            p.first=min(element[i].first,element[i+1].first)
            p.second=element[i].second
        else:
            res.append(p)
            p.first=element[i].first
            p.second=element[i].second
    if p.first!=res[-1].first:
        res.append(p)
    return res
#Time Compexity :O(N)
#Space Complexity:O(N) to collect the resulatnt either O(1)