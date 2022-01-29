#Exercise:Mirror image linklist
"""
Given an linklist contains n element and its structure is below
Node={
    value,
    random
    next
}
1.value-contains data
2.random-It's point to any pointer of linklist including self .
3.next it points to the next pointer.
you have to make deep copy of linklist.
"""
#clarificatin:
"""
Ques-linklist contain suplicate numbers?
Ans-yes it can be .
"""
#Bruteforce Approach
"""
1.First make a linklist same as given where every node random pointer is null.
2.Start from original linklist and pick 1st node.
3.and check in the linkist which node is the same address to the random pointer.
4.And calculate the length of it 
5. if length is negative it means .it present in back of current node.if zero it means it pointing to itself.
6. if length is positive it means. it occurs front of current to the node .
7.using length we can point the random pointer to the node exit in original linklist .
"""
#Time Complexity:O(N^2)
#Space Complexity:O(1),excluding space occupy by deep copy of liklist.


#Optimised Approach 
"""
1.Take original linklist and create a node insert at 1st position with same value of at 0th position and do same for rest and append it.
2.Now we have original linklist plus same length of nodes that are pointing to same adjacent nodes values
3. So start from starting of new linklist check where its random pointer is pointer .according we can append it.
"""
#Code
def mirror_node(head):
    if head==NULL:
        return head
    ptr=head
    while ptr!=None:
        tmp=ListNode(ptr.value)
        tmp.next=ptr.next
        ptr.next=tmp
        ptr=tmp.next
    ptr=head
    while ptr!=None:
        ptr.next.random=ptr.random.next
        ptr=ptr.next.next
    new_head=head.next
    head.next=head.next.next
    ptr=head.next
    while ptr!=None:
        new_head.next=ptr.next
        new_head=new_head.next
        ptr.next=ptr.next.next
        ptr=ptr.next
    return new_head

#Time Complexity:O(N)
#Space Complexity:O(1),excluding space occupy by deep copy of liklist.
