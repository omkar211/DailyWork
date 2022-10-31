# Given a BT return True if BST else return False.


# Approach 1
"""
Store Preorder and check if it is sorted then return True
"""
def preorder(root,lst):
    if root == None:
        return True
    lst.append(root.val)
    preorder(root.left,lst)
    preorder(root.right,lst)

def check_BST1(root):
    lst = []
    preorder(root,lst)
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True
# Time Complexity:O(N)
# Space Complexity:O(N)

#Approach 2:
"""
We know the property of BST left- subtree must be less than the root node and right sub-tree must be 
greater than root node.
initially assigned max to infinite and min to negative-infinity.
"""
def check_BST(root,Min,Max):
    if root == None:
        return True
    if root.val>=Min and root.val<=Max:
        return True
    else:
        return False
    return check_BST(root.left,Min,root.val) and check_BST(root.right,root.val,Max)

# Time Complexity:O(N)
# Space Complexity:O(N)


