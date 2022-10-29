#BT left view 

#Solution 
global_height = 0
def right_view(root,height = 1):
    if root == None:
        return True
    if height>global_height:
        print(root.val)
        global_height = height
    right_view(root.right,height+1)
    right_view(root.left,height+1)
# Time Complexity:O(N)
# Space Complexity:O(N)
