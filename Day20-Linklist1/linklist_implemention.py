#Exercise: Linklist Implementation
"""
Problem statement:insert values at head in linklist , implement from the scatch.
"""
#Code
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

def helper(head,data):
    if head==None:
        head=ListNode(data)
        return head
    temp=ListNode(data)
    temp.next=head
    return temp


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


#To Insert N element:-
            #  Time Complexity:O(N)
            #  Space Complexity:O(N)
