"""
Exercise:Permutations
Problem:
find the permutation of a string which have distinct character?

Input:string="ABC"

output:
    ABC
    ACB
    BAC
    BCA
    CAB
    CBA
"""
# Bruteforce Approach
"""
we will go through with the basic rule of Backtracking.
if i fix every character at a palce and find out the permutation of remaining string and append with the fixed character and take union of all that will be my answer.
like:
    A+P(B,C)
    B+P(A,C)
    C+P(A,B)
"""
#Code
def permutation(A,index):
    if(index==len(A)):
        st=""
        print(st.join(A))
        return 
    for i in range(index,len(A)):
        A[index],A[i]=A[i],A[index]
        permutation(A,index+1)
        A[index],A[i]=A[i],A[index]



permutation(['A','B','C'],0)
#Explanation of code :
"""
Take an example 'ABC' and index=0
when index = 0:
    1.    I will check the is index equals to the size of string .so here Not we will go for next step.
             Now we will enter in aloop and swap the characters at place of i and at place index so both the character is zero.
             So string remains same "ABC"
    2.    Now call for remaining caluculation of permutation of string(B,C) by incresing the index by1
             So in second call index will be 1.and we will check the if index equals to the string length.in this it is not .
             So we will enter in a loop and swap the string of index and ith character. In this case both are same so after swapping our string will be "ABC".
    3.  Now call for remaining string permutation (C) so here index equals to 2 .So here we will 
            check if index equals to size of string or not .in this case Not .
            so we will go inside the loop and and swap the C with the C because index and i are pointing same index.
    4.  And call for function for calculating remaining permutation with index equals to the 3.
            so we will check if the index equal to the size of the string .In this it is so we will print the string and return the control on 3.step
            So result will be prined "ABC".
    5.  And We will now in inside of the loop and we will swap the C to C and increase the i by 1
            and i will be 3 and index equal to 2 . 
            So in this case we will return so the step 2 and swap the B to B because index and ith value is same which is one but when inside loop code completed so i will be increament by 1 . It will be 2 and now we will swap the character at index equal to 1 and i equal to 2.So the string will we ACB and we go for nxt steps like above and print all the permutations.



"""
#Time Complexity:O(N!*N),Nis size of a string
#Space Complexity:O(N)


#Explanation of time complexity
"""
if go to first iteration then inner goes till N and inside it it carries a function to calculate th the remaining permutation of the string time
so here
        T(N)=N*T(N-1)
            =N*N-1*T(N-2)
            =........
            =.....
            =N*N-1*N-2*n-3*...............*T(1)
We know that if n==1 it means index is equals to the size of the string .
Now it will print all the string of size N.
so final equation will be 
            =N*N-1*N-2*N-3*N-4*N-5*...........N
            =N!N

"""