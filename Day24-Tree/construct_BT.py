# given Inorder and Preorder Traversal order of BT  construct the BT using this imformation.

#Solution
def construct(inorder,preorder,start,end,index):
    

    node = TreeNode(preorder[index])
    
    
    