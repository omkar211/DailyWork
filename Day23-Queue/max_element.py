#Exercise:max element:
"""
Given an array of integers A and value k.find the maximum element from the sub array of size K 
eg : 2 3 1 10 4 1 6 3 2 0
K=3
ans: 3,10,10,10,6,6,....
"""
#Bruteforce Approach:
"""
find all the pair size of K and check for max element .
"""
#Code
def max_element(A,K):
    ans=[]
    for i in range(len(A)-K+1):
        res=float('inf')
        for j in range(i,K):
            res=max(res,A[i])
        ans=append(res)
    return ans

#Time Complexity:O(N*K)
#Space Complexity:O(1)


#Optimized Appraoch
"""
take an above example [2,3,1,10,4,1,2] 
we will first find the max element from the k elements and store it in a array and put a pointer at index 0 and another pointer at k+1 check if front element is equals to first pointer
if not it means max element must be a part of next sub array.
"""
#Code 
def find_max_element(A,k):
    queue=[]
    max_element=float('inf')
    for i in range(k):
        max_element=max(max_element,A[i])
    queue.append(max_element)
    print(max_element)
    first_ptr=0
    for second_ptr in range(k,len(A)):
        if queue[0]==first_ptr:
            queue.remove(0)
            max_element=A[0]
        while len(queue)>0:
            if queue[-1]>A[second_ptr]:
                queue.append(A[second_ptr])
                break
            else:
                queue.pop()
        
#Time Comlexity:O(N)
#Space Complexity:O(N)

