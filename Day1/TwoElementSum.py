"""
 Question: A array has contains no of elements and its target value B.
           you have to find the pair which has sum equals to the B.
           return True or False

clarification : 1. what should i do when array size is <=1.
                2. what shuold i return when pair is not found.
                3. can i change array?
                4. Can i use space ?
                5. array is sorted.


Solution 1:lets say array is [x1,x2,x3,x4,x5,.........xn]. we have to pick ith element and check
           for finding pair we have to it's left till Zero and right till Array size.if any pair sum 
           find out that is equals to the target return it .
"""
#Code 
def pairSum(arr,B):
    for i in range(len(arr)-1):
        for j in range(len(arr)):
            if arr[i]+arr[j]==B:
                return True
    return False
print(pairSum([1,2,3,4,5,6,7,8],15))

#Time Compexity: O(N2)
#Space Complexity:O(1)

"""
Solution 2: 
          here we have to find the X+Y=B(target)
          lets say if i chose X element from above equation.and wants to find out Y to archieve the target
          then my Y would be Y=B-X so here i will check in whole entire array execept X element's index 
          if Y is found then return True else return False
          so here finding y is taking so much time.if i retrieve the Y in minimum time.that would solve our problem.
          so for seaching in an unordered array is Dictionary in python.
        Now:
          1.lets start with an example [x1,x2,x3,x4,x5......xn],target is B = 2*x1
          2.Define dict 
          3. insert in dict
          lets say i pick x1 so here X=x1 so using the above equation we have to find only Y
          Y=2*x1-x1
          Y=x1 we have to search in dict ,so here dict will return Y is present in dict.
          so here is a problem when target is twice of any element even element occurs once in
          a array it still return true 

          so here we will solve the above problem.
          before inserting in the if i checked the does element occur in dict if yes return True
          else insert in the dict X element.
"""
# Code 
def pairSum2(arr,B):
    d={}
    for i in range(len(arr)):
        if arr[i] in d:
            return True
        else:
            d[arr[i]]=True
    return False
#Time Complexity : O(N)
#Sapce Complexity : O(1)
