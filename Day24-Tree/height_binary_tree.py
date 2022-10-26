#Calculate the height of binary tree?

def height(root):
    if root==None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return max(left,right)+1

# Time Complexity:O(N)
# Space Complexity:O(N)