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
If loop exit it mean last of linklist does not exit .
let take an example of address of nodes .... x1,x2,x3,x4,x5,x6,x7,x8,x5
as we can see , at x5 position address loop exit.
So if take 2 pointer slow and fast and start traversing from same position.
if we made increament to slow pointer by next position and faster pointer to the 2 steps then we will see it will circulating in loop once both entered in a loop then after some time both the pointer cross each other there are 2 cases.
adjacent or 1 step away from each other if adjacent then next increment they will meet or if 1 step away then we increment 1 step then it can be next step meet .
Because there are only 2 possiblity exits 1 or 2.
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

#Time Complexity:O(N)
#Space Complexity:O(1)

