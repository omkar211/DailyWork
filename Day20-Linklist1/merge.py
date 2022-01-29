#Exercise:Merge
"""
Given 2 sorted linklist merge both of them  and return 3rd linklist.
"""
#Bruteforce Approach
"""
1.Put a pointer on both the starting of linklist and compare the element from one another and take a pointer and append it to the tail of it .
"""
#Code
def merge(ptr1,ptr2):
    if ptr1==None:
        return ptr2
    if ptr2==None:
        return ptr1
    head=tail=None
    while ptr1!=None and ptr2!=None:
        if ptr1.data>ptr2.data:
            if head==None:
                tail=head=linkNode(ptr1.data)
            else:
                tail.next=linkNode(ptr1.data)
                tail=tail.next
            ptr1=ptr1.next


        else:
            if head==None:
                head=linkNode(ptr2.data)
             else:
                tail.next=linkNode(ptr2.data)
                tail=tail.next
            ptr2=ptr2.next

    return head

#Time complexity:O(N)
#Space Complexity:O(N)

#Optimized Approach
"""
Rather than creating new pointer everytime rearrange them in order.
1. put a pointer at starting of both linklist and compare the value of it. if ptr2 value greater than ptr1 then just increase ptr2 by 1 step . and compare ptr1 and ptr2 again .suppose ptr1 value is greater than ptr2 then attatch it just before the ptr2 and increase ptr1 by just one step. and so on....
"""
#Code
def merge2(ptr1,pt2):
    if ptr1==None:
        return ptr2
    if ptr2==None:
        return ptr1
    head=tail=None
    while next1!=None and next2!=None:
        if ptr1.value<ptr2.value:
            if head==None:
                head=ptr1
            else:
                tail.next=ptr1
            ptr1=ptr1.next
        else:
            if head==None:
                head=ptr2
            else:
                tail.next=ptr2
            ptr2=ptr2.next
        tail=tail.next
    while ptr1!=None:
        tail.next=ptr1
    while ptr2!=None:
        tail.next=ptr2
    return head


#Time complexity:O(N)
#Space Complexity:O(1)
    


            
        