def levelorder(root):
    if root==None:
        return root
    q = []
    q.append(root)
    while len(q)>0:
        length = len(q)
        while length>0:
            length -=1
            node = q[0]
            print(node.val)
            q.append(node.left)
            q.append(node.right)
            del q[0]
# Time Complexity: O(N)
# Space Complexity: O(N)

            
