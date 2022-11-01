# Problem:Generate BST from Inorder
"""
Generate the balanced BST from Inorder traversal array.
"""
# Approach
"""
1. Balanced means height of every subtree must be <=1.
2. So we Know that if we take mid element of the given array then height of both the sub tree 
will be <=1.
3. Ask the left subtree to generate the balanced  subtree and same for Right subtree.
"""
# Solution
def generate_BST(lst,start,end):
    mid = (start+end)>>1
    if mid == start or mid == end :
        return Treenode(lst[mid])
    left = generate_BST(lst,start,mid-1)
    right = generate_BST(lst,mid+1,end)
    node = Treenode(lst[mid])
    node.left = left
    node.right = right
    return node

# Time Complexity:O(N)
# Space Complexity:O(N)