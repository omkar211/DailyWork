# Problem:
"""
Given BST by mistake 2 nodes get swapped .find out the 2 swapped nodes.
"""

# Approach:
"""

"""

# Solution
def BST(root,lst,Min,Max):
    if root==None:
        return True
    if root.val>Max or root.val<Min:
        lst.append(root)
    if len(lst)>=2:
        return False
    return BST(root.left,lst,Min,root.val)or BST(root.right,lst,root.val,Max)

lst = []
BST(root,lst,Min,Max)
print(lst)
#Time Complexity: O(N)
#Space Complexity: O(N)
