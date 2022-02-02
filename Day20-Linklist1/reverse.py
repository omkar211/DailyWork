#Exercise:Find address of starting loop
"""
Given an linklist contains n element reverse the linklist.
"""
#Bruteforce
"""
1.lets take an example 1->2->3->4->5->6 .
2.we create a node and append it to the head of linklist.
"""
#code
def reverse(head):
    if head==None or head.next==None:
        return head
    new_head=None
    while(head!=None):
        temp=ListNode(head.val)
        if new_head==None:
            new_head=temp
        else:
            temp.next=new_head
            new_head=temp
        head=head.next
    return new_head

#Time Complexity:O(N)
#Space Complecity:O(N)


#Optimized Approach A 
"""
Rather than creating new node everytime we can append at head the current node and before appending it we will save current.next somewhere not to lost rest linklist. 
"""
def reverse2(head):
    if head==None or head.next==None:
        return head
    new_head=head
    next_ele=current=head.next
    head.next=None
    while curr!=None:
        next_ele=current.next
        current.next=new_head
        new_head=current
        current=next_ele
    return new_head
#Time Complexity:O(N)
#Space Complexity:O(N)


#Optimized Approach B
"""
Rather than pick element and attatched it to head. We can pick a pointer prev that will point just to current previous element and so every time append to current's next=prev and not to loose rest linklist we have to atore the current.next pointer in variable .we will do that till we reached the last.
"""
def reverse3(head):
    if head==None or head.next==None:
        return head
    prev=None
    curr=next_element=head
    while curr!=None:
        next_element=curr.next
        curr.next=prev
        prev=curr
        curr=next_element
    return prev
#Time Complexity:O(N)
#space Complexity:O(1)
