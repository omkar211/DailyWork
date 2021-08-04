"""
Exercise:
        Unset the last bit of N.
"""

# Solution1:
"""
lets take an example N=5
so we expand bit of N and N-1
N=5   00101
M=4   00100
res   00100
if we added up N and N-1 using AND operator then resultant will be unset the last bit   
"""
def set_bit(N):
    return N&(N-1)