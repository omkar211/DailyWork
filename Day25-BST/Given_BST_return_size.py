# Given BT return the size of maximum BST SubTree.

#Approach1
"""
store pre-order and update res at discontinuity.
"""
def preorder(root,lst):
    if root==None:
        return True
    lst.append(root.val)
    preorder(root.left,lst)
    preorder(root.right,lst)
max_count,res,i,j = 0
while i<=j and j<len(lst):
    if lst[i]>lst[j]:
        max_count = 0
        i = j
    j+=1
    res = max(res,max_count)
print(res)

#Time Complexity:O(N)
#Space Complexity:O(N)

#Approach2
"""
We will ask left subtree are you  BST recursively then check condition for root and same for 
right sub-tree.
"""
#Solution
res = 0
def check_BST(root,Min,Max,size):
    if root == None:
        return True
    if root.val>=Min and root.val<=Max:
        size = +1 
        return True
    else:
        res = max(size,res)
        size = 1
        return False
    return check_BST(root.left,Min,root.val,size) and check_BST(root.right,root.val,Max,size)


