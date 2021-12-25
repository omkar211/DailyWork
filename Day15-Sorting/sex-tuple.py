#Exercise:SEX-Tuple
"""
Given an array A of length N with all element find the number of sex-tuple such that   
           A+B+C)/D - E=F

           number can be repeated.
"""
#Brute force :
"""
"""
#Code
def sex_tuple(A):
    count=0
    for a in range(len(A)):
        for b in range(a,len(A)):
            for c in range(b,len(A)):
                for d in range(c,len(A)):
                    for e in range(d,len(A)):
                        for f in range(e,len(A)):
                            if (A[a]+A[b]+A[c])==A[d](A[e]+A[f]):
                                count+=1

    return count


#Time Complexity:O(N^6)
#Space Complexity:O(1)


#Optimize Approach
def sex_tuple2(A):
    dt={}
    count=0
    for a in range(len(A)):
        for b in range(a,len(A)):
            for c in range(b,len(A)):
                dt[A[a]+A[b]+A[c]]=True
    for d in range(len(A)):
        for e in range(d,len(A)):
            for f in range(b,len(A)):
                if dt.get(A[d]*(A[e]+A[f]),False):
                    count+=1
    return count
#Time Complexity:O(N^3)
#Space Complexity:O(1)