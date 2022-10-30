"""
Problem: Given 2 BT check these are identical or not.
"""
#Solution
def identical(root1,root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.val != root2.val:
        return False
    return identical(root1.left,root2.right) or identical(root1.right,root2.right)

#Time Complexity:O(N)
#Space Complexity:O(N)