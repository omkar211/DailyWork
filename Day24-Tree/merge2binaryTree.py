# Given 2 tree's root node  merge these 2 nodes based on below criteria
# 1. if node overlap make the sum of both the nodes at same place.
# 2. if node not overlapped then create new node and then create a node.

#Solution
def merge(root1,root2):
    if root1==None and  root2==None :
        return True
    elif root2==None:
        return True
    elif root1!=None and root2!=None :
        root1.val+=root2.val

    if root1.left==None:
        root1.left = root2.left
    if root1.right==None:
        root1.right = root2.right

    merge(root1.left,root2.left)
    merge(root2.right,root2.right)

#Time Complexity:O(N), N is number of nodes
#Space Complexity:O(N)

    