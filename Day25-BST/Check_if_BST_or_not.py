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


#Approach 4:
"""
If we get maximum from left Tree and minimum from right tree and check root is greater than the left retured value and less than the right returned value and recursively we check for all the sub-tree
"""
min_res = float('inf')
max_res = float('-inf')

def find_min(root):
    if root==None:
        return 0
    min_res = min(root.val,min_res)
    find_min(root.left)
    find_min(root.right)

def find_max(root):
    if root==None:
        return 0
    max_res = max(root.val,max_res)
    find_max(root.left)
    find_max(root.right)
def check_BST(root):
    if root == None:
        return 0'
    min_res = float('inf')
    max_res = float('-inf')
    find_min(root.left)
    find_max(root.right)
    if root.val<min_res or root.val>max_res:
        return False
    return check_BST(root.left) or check_BST(root.right)

#Time Complexity:O(N*N)
#Space Complexity:O(N)

#Optimized Approach of 4:
"""
To reduce time complexity rather than calculating every time . if we maintain a custom object which will contain the min ,max and is_bst and start from bottom-up solution.
"""

def check_BST(root):
    if root==None:
        return root
    left = {}
    right = {}
    if root.left == None:
        left = {is_bst : True,
                left:root.val,
                right:root.val
                }
    else:
        left  = check_BST(root.left)
    if root.right == None:
        right = {is_bst : True,
                right:root.val,
                right:root.val
                }
    else:
        right  = check_BST(root.right)
    
    if left.is_bst and root.val>=left.Max and root.val<=right.Min and right.is_bst:
        return {
            is_bst:True,
            Max:right.Min
            Min : left.Max
        }
    else:
        return {
            is_bst:False,
            Max:right.Min
            Min : left.Max
        } 
    
# Time Complexity:O(N)
# Space Complexity:O(N)
    

   


