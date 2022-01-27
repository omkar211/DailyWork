#Exercise:Find address of starting loop
"""
Given an linklist contains n element find address of starting loop if loop exit.
"""
#Bruteforce
"""
1. Traverse on a linklist and same time store address of node in dictonary and check this address repeating twice .then return address else return False.
"""
#Code
def find_loop(head):
    if head==None:
        return False
    dt={}
    while head!=None:
        if dt.get(head,False):
            return head
        else:
            dt[head]=True
        head=head.next
    return False

#Time Complexity:O(N)
#Space Complexity:O(N)

#Optimized Approach
"""
1.Take 2 pointer one is slow another one is fast and start traversing from starting of a linklist and increse slow pointer by 1 step and 2 steps by faster pointer .
2. When they meet at a certain point ,then start increamenting slow pointer by 1 and take a varible that will count all the numbers of steps to reach at faster pointer .All this will return you a length of loop.
3.So take 2 pointer one put at starting of linklist and other one at length of 'l'.Than we have 2 cases.
4. One case is linklist length till loop starting point is greater than loop in this case lets say to reach at starting loop address.Take distance x.
5.increase both the pointer by one .here first pointer cover 'x' distance and second pointer covers 'l+x' extra travel is 'l' . so it means they meet at starting pointer of loop.
"""
#Code
def 