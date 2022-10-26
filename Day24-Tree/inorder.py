def inorder(root):
    if not root:
        return root
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    

# Time Complexity:O(n), where n is number of nodes
# Space Complexity:O(n)