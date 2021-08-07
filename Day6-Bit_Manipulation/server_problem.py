"""
Exercise: N servers
        Problem statements:
        We have given N servers. some are active some are inactive. Find out which server is active 
        you can pass only a string as many times you want.
        eg: there are 4 servers 3rd one is inactive if i pass string ="abcd" then resultant string
        will be 'abd' 
"""
#Solution:
"""
So here we pass a n bit length at every time we pass a string and set once for every server and rest bit are unset.
eg: there are 4 servers so i pass 4 different strings
              0001
              0010
              0100
              1000
here i will set ith bit 1 rest zero if all the bits is zero it means ith bit server is closed.
"""
def server(N):
    string ="0"*N
    closed_server=[]
    for i in range(N):
        string[i]="1"
        temp=send_for_servers(string)
        if(len(temp)>0 and temp[i]=="1"):
            continue
        else:
            closed_server.append(i)
    return closed_server
#Time Complexity:O(N)
#Space Complexity:O(1)

#Solution2:
"""
let's say there are 4 servers in these servers if i pass 8 strings then inactive server won't send back any character active servers will respond back.
lets say servers are given a1  a2  a3  a4  and a2 and a4 are inactive. I calculate the bits of 0 to N-1 and pass all the bits of zero at zeroth server and first bits at 1st place.

0bit  1bit 2bit 3bit  
0      1    0    1     
0      0    1    1 

So if i pass bit horizontaly then those servers which are closed will not return the whole number .
In above example  if  pass all the bits in above servers then 2bit and 4bit will be absent.
If we observe here we just need to pass only logN string.
"""
def server2(A):
    





#Time Complexity:O(logN)
#Space Complexity:O(1)



