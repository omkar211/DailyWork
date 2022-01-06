#Exercise:Insert on tail 
"""
Insert an element on tail , assume you have access of tail.
""" 
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

def helper(tail,data):
    if tail==None:
        tail=ListNode(data)
        return tail
    temp=ListNode(data)
    tail.next=temp
    return tail.next

def insert(head):
    tail=None
    print("Please enter the element")
    d=input()
    while(d!="-1"):
        tail=helper(tail,d)
        if head==None:
            head=tail
        print("Please enter the element")
        d=input()
    return head


def print_linklist(head):
    while(head!=None):
        print(head.data,end=" ")
        head=head.next
    print()

head=None
head=insert(head)
print_linklist(head)

# Complexity for inserting one element 
#Time Complexity:O(1)
#Space Complexity:O(1)  