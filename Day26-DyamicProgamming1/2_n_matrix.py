# Exercise:
"""
Description:
Given 2*N matrix ,it has +ve numbers,
Constraint: 
1. you can not choose horizontal immediate , vertical immediate and diagonally immediate.
"""
# Approach
"""
1.We Know that, if i choose first row's ith element then We will not choose i-1 and i+1 and second row's i-1 and i+1 and ith 
2. If we choose the second row's ith element then we do not consider same for first row.
3. there is surity , i will always one of the ith element from first and second row.
4. so design a sigle array and pick max(first_row[i],second_row[i]).
5. and Now it is converted in house rob same problem.
"""