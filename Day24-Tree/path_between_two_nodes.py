# Given a BT , you have 2 calculate the path b/w nad 2 nodes such that the sum of nodes coming in that path max.

#Solution
res = -1
def distance(root):
    if root == None :
        return 0
    left =  distance(root.left)
    right =  distance(root.right)
    c1 = root.val
    c2 = root.val+left
    c3 = root.val+right
    c4 = root.val+right+left
    temp = max(c1,(max(c2,max(c3,0))))
    res =  max(res,temp)
    return temp 

# Time Complexity:O(N)
#Space Complexity:O(N)