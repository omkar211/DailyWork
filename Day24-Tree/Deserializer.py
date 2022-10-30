"""Deseraliation & serialization of BT 
    Given BT store the tree a file such that you can retrieve again from the file 
"""
#Approach
"""
Preorder
if let's there is only one root only to be stored in file .very easy insert root.val and left is null and right is null .
and if we want to store the .
same if we see if we want to insert complete binary tree in a file . just need to null for leaves nodes.

For Generic solution we will insert the null if root has not child ..l..l.
"""

#Solution
file_path = 'file/path/deserializer.txt'
def Deserializer(root):
    if root == None:
        file_path.write(-1)
        return True
    file_path.write(root.val)
    Deserializer(root.left)
    Deserializer(root.right)

def serialization(string, i):
    if len(string) == i:
        return True
     bb
    


