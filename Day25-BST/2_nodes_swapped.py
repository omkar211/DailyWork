# Problem:
"""
Given BST by mistake 2 nodes get swapped .find out the 2 swapped nodes.
"""

# Approach1:
"""
So store inorder and make a same copy of inorder and sort it and compare it . 
point out those elements are not same and that will be our answer.
"""
# Code
def In(root,lst):
    if root==None:
        return True
    inorder(root.left)
    lst.append(root.val)
    inorder(root.right)

lst1 = []
inorder(root,lst1)
lst2 = list(lst1)
lst2.sort()
for i in range(len(lst1)):
    if lst1[i]!=lst2[i]:
        print(lst1[i])
#Time Complexity:O(NlogN)
#Space Complexity:O(N)

# Approach 2
"""
Store an inorder array and count the inversion pairs 
form first inversion pair take max value and from second take min.
but there will be a case where we have only 1 inversion pair.
Case when both the swapped nodes share an edge.In this case print both the nodes
"""
def inorder(root,lst):
    if root==None:
        return True
    inorder(root.left)
    lst.append(root.val)
    inorder(root.right)
lst = []
inorder(root,lst)
index = 0
res = []
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        index = i
        res.append(max(lst[i],lst[i+1]))
if len(res)!=2:
    res = lst[i:i+2]
print(res)

#Time Complexity: O(N)
#Space Complexity: O(N)


#Approach3
"""

"""