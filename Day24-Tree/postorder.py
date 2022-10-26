def postorder(root):
    if not root:
        return root
    postorder(root.left)
    postorder(root.right)
    print(root.val)

    

# Time Complexity:O(n), where n is number of nodes
# Space Complexity:O(n)