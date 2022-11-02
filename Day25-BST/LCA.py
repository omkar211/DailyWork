# Problem
"""
Given a root node of a tree. findout the LCA of it.
"""
# Approach
"""Time
          There can be 2 cases.
1. One node can be from left subtree and another can be from right sub-tree then we return root.
2. One node can be from left side or from right side and another one is root in this case we know 
whoever node we find out first will be a LCA .
"""

# code
def find_LCA(root,n1,n2):
    if root == None:
        return root
    if root.val == n1 or root.val == n2:
        return root
    left  = find_LCA(root.left)
    right = find_LCA(root.right)
    if left and right :
        res = root
        return root
    if (left or right ) and (root.val==n1 or root.val==n2):
        return root
    return None

#Time complexity: O(N)
#Space complexity: O(N)


#Best Approach
"""
There could a few cases :
1. what if n1 & n2 not preset in tree or ever what if only n1 or n2 present . In that case 
answer will be None but it return a root node.
"""

# Code
class Result:
    def __init__(self):
        self.node_lca = None
        self.first_key = False
        self.second_key = False
def find_LCA(root,custom_obj):
    if root == None:
        return True
    if root.val == n1:
        custom_obj.first_key = True
    if root.val == n2 and :
        second_key.second_key = True
    left  = find_LCA(root.left)
    right = find_LCA(root.right)
    if left and right :
        res = root
        return root
    if (left or right ) and (root.val==n1 or root.val==n2):
        return root