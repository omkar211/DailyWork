# Given the BT where for a node we have properties
    #   1. data
    #   2. left
    #   3. right
    #   4. next
# At begaining next pointer is null , point it to the left to right on same level.

def binary_tree(root):
    if root == None:
        return root
    q = []
    q.append(root)
    while len(q)>0:
        temp = q[0]
        del q[0]
        length = len(q)
        while length:
            q.append(temp.left)
            q.append(temp.right)
            length-=1
            temp.next = q[0]
            temp = q[0]
            del q[0]
    return root