#Exercise:Linked-List
"""
Problem Description:
Design and implement a Linked List data structure. A node in a linked list should have the following attributes - an integer value and a pointer to the next node. It should support the following operations:
insert_node(position, value) - To insert the input value at the given position in the linked list.
delete_node(position) - Delete the value at the given position from the linked list.
print_ll() - Print the entire linked list, such that each element is followed by a single space.
Note:
If an input position does not satisfy the constraint, no action is required.
Each print query has to be executed in new line.

Problem Constraints
1 <= position <= n where, n is the size of the linked-list.

Input Format
First line contains an integer denoting number of cases, let's say t.
Next t line denotes the cases.

Output Format
When there is a case of print_ll(),  Print the entire linked list, such that each element is followed by a single space.
NOTE: You don't need to return anything.

Example Input
5
i 1 23
i 2 24
p
d 1
p

Example Output
23 24
24
Example Explanation
After first two cases linked list contains two elements 23 and 24.
At third case print: 23 24.
At fourth case delete value at first position, only one element left 24.
At fifth case print: 24.
"""
#Code:
def calculate_length(head):
    count=0
    while head!=None:
        count+=1
        head=head.next
def insert_node(head,position, value):
    if position==1:
        return Linklist(value)
    length=calculate_length(head)
    if length+1>position:
        return 
    temp=head
    length=1
    while length<position:
        temp=temp.next
    temp.next=temp.next.next
    return head

def delete_node(head,position):
    temp=head
    if position==1:
        return head.next
    while position>1:
        position-=1
        if head=None:
            return 
    head.next=head.next.next
    return temp

def print_ll(head):
    while(head!=None):
        print(head.val,end="->")
        head=head.next
    print()