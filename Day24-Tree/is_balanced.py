"""
Problem: Given BT check it is balanced or not 
"""
# Approach: I will get max height of left subtree and same for right substree check for balanced tree.
#Solution:
flag = True
def is_balanced(root):
    if root == None:
        return 0
    if not Flag:
        return 0
    left = is_balanced(root.left)
    right = is_balanced(root.right)
    if abs(left-right)>1:
        flag = False
    return max(left,right)+1


#Time Complexity:O(N)
#Space Complexity:O(N)