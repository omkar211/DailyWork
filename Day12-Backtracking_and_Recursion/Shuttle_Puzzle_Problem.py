#Exercise:Shuttle Puzzle Problem
"""
Problem Description:
We are given n White marbles and n Black marbles along with a strip with 2n+1 holes . The n White marbles are on the left side occupying the leftmost n holes and the n Black marbles are on the right side occupying the rightmost n holes. The middle hole i.e the n+1 hole is empty.

For example if n = 4 , then the initial configuration of the strip is - WWWWHBBBB, Where H denotes the empty hole.

Valid moves are :
Move 1 marble by 1 space (into the empty hole).
Jump 1 marble over 1 marble of the opposite color (into the empty hole).
Output set of minimum number of valid moves to achieve the transformation of n Black marbles to the left followed by a hole followed by n White marbles.

NOTE - The first move should be the slide of the White marble(At Hole number n-1) to the right.

Problem Constraints
1 <= n <= 15

Input Format
First argument is an integer n.

Output Format
Return a list of strings where each string represents the state of the strip after each move.

Example Input
Input 1:
 1

Example Output
Output 1:
 [WHB, HWB, BWH, BHW]

Example Explanation
Explanation 1:
 For n = 1, initial configuration of strip -> WHB.
 After moving white marble to the right -> HWB.
 Now, move black marble to the leftmost hole -> BWH.
 Finally move the white marble to the rightmost hole -> BHW.
"""