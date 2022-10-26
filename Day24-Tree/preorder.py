def preorder(root):
    if not root:
        return root
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# Time Complexity:O(n), where n is number of nodes
# Space Complexity:O(n)