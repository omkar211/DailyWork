#Exercise: find middle node of s linklist
"""
Given an linklist you have to find the middle element of the linklist.
"""
#clarification:
"""
Middle in case of linklist size is even.
Ans:first element
"""
#Bruteforce
"""
1.Find out length of linklist and
2.Traverse on linklist till length by 2.
3.That will be our answer.
"""
#Code
def calculate_length(head):
    count=0
    while(head!=None):
        count+=1
        head=head.next
def find_middle(head):
    if head==None:
        return 0
    length=calculate_length(head)
    while length>0:
        head=head.next
        length-=1
    return head

#Time Complexity:2*N or O(N)
#Space complexity:O(1)

#Optimised Approach
"""
Suppose , we have 2 runners A and B and x distance and they start running from a same point and A have to reach at x and B have to reach to x/2 in same time . so with what speed they should start or should go.
                            T=D/V
So above we know time is constant  so to travel x/2 distance need velocity V, then for to reach to x need 2V speed.
"""
#Code
def find_middle2(head):
    if head==None:
        return 0
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow

#Time Complexity:O(N)
#Space Complexity:O(1)
