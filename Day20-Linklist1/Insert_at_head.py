#Exercise:Insert at Head of Linklist
"""
Problem statements:Given an head pointer of  linklist and an element k insert a node at 0th position.
"""
# class listnode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

def insert_at_head(head,k):
    if head ==None:
        head=listnode(k)
        return head
    temp=listnode(k)
    temp.next=head
    return temp
#Time Complexity:O(1)
#Space Complexity:O(1)
