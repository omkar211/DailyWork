"""
find N is even or odd without using % . 
"""
#Soultion1: 
"""
one is way is divide the number by 2 and check if remainder is zero  it means even else it is odd .
"""
#Code
def even_odd(N):
    if n%2==0:
        return "even"
    else:
        return "odd"

#Solution2:
"""
We know that if we look all the even numbers bit then we wilalways get a zero at the starting.
so if we added up using AND operator by 1 and if we got 1 it means number is even number else number id odd number.
"""
#Code
def even_odd2(N):
    if N&1:
        return "odd"
    return"even"