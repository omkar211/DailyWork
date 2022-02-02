#Exercise:Insert on tail
"""
Insert an element on tail ypu have only accessonly head of link list.
"""

"
#Code
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

def helper(head,data):
    if head==None:
        head=ListNode(data)
        return head
    temp=head
    while(temp.next!=None):
        temp=temp.next
    temp.next=ListNode(data)
    return head


def insert(head):
    print("Please enter data ")
    d=input()
    while d!="-1":
        head=helper(head,d)
        print("Please enter data ")
        d=input()
        
    return head

def print_linklist(head):
    while(head!=None):
        print(head.data,end=" ")
        head=head.next
    print()
head=None
head = insert(head)

print_linklist(head)


#  Time Complexity:O(1)
#  Space Complexity:O(1)
