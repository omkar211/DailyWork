#BT left view 

#Solution 1
def left_view1(root):
    if root == None:
        return True
    q = []
    q.append(root)
    while len(q)>0:
        print(q[0].val)
        length = len(q)
        while length>0:
            length-=1
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            del q[0]
#Time Complexity :O(N)
# Space Complexity:O(N)

global_height = 0
def left_view2(root,height=1):
    if root == None:
        return True
    if height >global_height:
        print(root.val)
        global_height = height
    left_view2(root.left,height+1)
    left_view2(root.right,height+1)
