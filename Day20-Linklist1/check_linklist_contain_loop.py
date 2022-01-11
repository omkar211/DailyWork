#Exercise:Check linklist contains loop
"""
Given an linklist contains n element find out if it contains loop or not.
"""
#Bruteforce
"""
1. Traverse on a linklist and same time store address of node in dictonary and check this address repeating twice .then return True else return False.
"""
#Code
def find_loop(head):
    if head==None:
        return False
    dt={}
    while head!=None:
        if dt.get(head,False):
            return True
        else:
            dt[head]=True
        head=head.next
    return False

#Time Complexity:O(N)
#Space Complexity:O(N)


#Optimized Approach
"""

"""
#Code
def find_loop2(head):
    if head==None:
        return 0
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        if slow==fast:
            return True
        slow=slow.next
        fast=fast.next.next
    return False

#Time Complexity:O()
#Space Complexity:O(1)

