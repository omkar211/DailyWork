# Delete perticular node from BST
"""
Given BST root and an element that is present in tree delete that node. if node not present
do nothing.
"""

# Ask 
"""
1. Is there duplicate elements.
"""
#Approach
"""
1. We know BST left sub-tree is lesser than root and right part is greater than root.
2. If we want to delete the root node . To make it BST again after deletion operation.
3. We can swap with the node root's left most right and delete root's left most right node and return
"""
# Code
def find_right_most(root):
    if root ==None:
        return None
    if root.left ==None and root.right==None:
        return root
    return find_right_most(root.right)

def deletion_BST(root,element):
    if root == None:
        return True
    if root.val == element:
        most_right = find_right_most(root.left)
        if most_right:
            root.val = most_right.val
            del most_right
        else:
            del root
            return None
    root.left = deletion_BST(root.left,element)
    root.right = deletion_BST(root.right,element)
    return root
# Time complexity:O(N)
# Space complexity:O(N)