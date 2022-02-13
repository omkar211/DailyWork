#Exercise: Min Stack
"""
Given n elements.implement
1.push operation
2.pop operation
3.Top operation
4.min_element of a stack
"""
#Bruteforce Approach
"""
Find above respectively.
Take an array insert in it of given size of stack.
1.Insert in array at size of array +1 position.
2.Detele last element from list.
3.Return last element.
4.At a perticular point empty the stack and store element in second stack in sequence and same time compare element and find min element and empty the second stack and insert it in first one .and return min element.
"""
# Time Comlexity:O(n)
# Reason
#               push-O(1)
#               pop-O(1)
#               top-O(1)
#               min_element-(n)

#Space Complexity:O(N)

# Optimized Approach1:
"""
4.Rather than finding min_element everytime.We can take another stack and store min element of every step
"""
# Time Comlexity:O(n)
# Reason
#               push-O(1)
#               pop-O(1)
#               top-O(1)
#               min_element-(1)

#Space Complexity:O(N)

# Optimized Approach2:
