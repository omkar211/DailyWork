"""Question:           Reading Newspaper
            
            Problem Description
You have a newspaper which has A lines to read.
You decided to start reading the 1st line from Monday. You are given a schedule, B, where B[i] = number of lines you can read on that day.
You are very strict in reading the newspaper and you will read as much as you can every day.
Determine and return, which day of the week you will read the last line of the newspaper.

Problem Constraints
1 <= A <= 1000
0 <= B[i] <= 1000

Input Format
The first argument contains the single integer A — the number of lines in the newspaper.
The second argument is an array B, of size 7 and those integers represent how many lines you can read on Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday correspondingly.

Note: It is guaranteed that at least one of the number in B[i] is larger than zero.

Output Format
Return a single integer — the number of the day of the week, when you will finish reading the newspaper. The days of the week are numbered starting with one in the order: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.

Example Input
A = 100, B = [15, 20, 20, 15, 10, 30, 45]

Example Output
6
-----------------------------------------------------------------------------------------------

clarification : 1. What should i return if A=0.
                2. what should i return if all the elements in B=0 when A not. 
                3. what should i return when all the values contains 0.


Solution : i will go each and every index of array B and at ith index i will reduce the B[i] value from A and move towards nth index if A still has greater that 0 .then will continue from the starting and when line in A has finished then simply i will return ith index if (index start from 0 then have to return i+1 th index).
and while reducing the value a simulteniously we have to maintain count for how many days it takes and mod(%)by 7 to get last day of finishing the book.
"""

#Code
def reading_newspaper(A,B):
    days=0
    while A>0:
        A-=B[days]
        days=(days+1)%7
    return days%7

print(reading_newspaper(100,[80, 20, 20, 15,0,0,0]))

#Time Complexity : O(A/sum(B))
#Space Complexity : O(1)

""" 
-----------------------------------------------------------------------------------------------
Solution 2: 
          There is a bit optimised approach.... if we observe in above approach we are subracting 
          ith index many times.if we know how many times do we need to subtract ith element from 
          A .then we will traverse only for in single times.so every time we are substracting
          it means we are dividing by ith element.
          so here we add the whole list and divide the A by sum of(B) if remainder is zero then return simply remainder+1
          if remainder is remained something then we have to take remainder and start thinking like 
          approach 1(solution 1).
"""
#Code
def reading_newspaper2(A,B):
    sum=0
    for i in B:
        sum+=i
    A=A%sum
    if A==0:
        return 1
    return reading_newspaper(A,B)

print(reading_newspaper2(100,[80, 20, 20, 15,0,0,0]))

#Time Complexity : O(N)
#Space Complexity :O(1)
