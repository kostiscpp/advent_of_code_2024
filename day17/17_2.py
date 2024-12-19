O = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]
N = len(O)

def check_iteration(A_i, a_i, O_i):
    B1 = a_i ^ 7
    denom = 2**(7 - a_i)
    C = A_i // denom
    return ( (a_i ^ C) & 7 ) == O_i

from functools import lru_cache

@lru_cache(None)
def backtrack(i, A_ip1):
    if i < 0:
        return (True, A_ip1) 
    
    start = 1 if i == N-1 else 0
    for a_i in range(start,8):
        A_i = 8*A_ip1 + a_i
        if check_iteration(A_i, a_i, O[i]):
            ok, A_0_val = backtrack(i-1, A_i)
            if ok:
                return (True, A_0_val)
    return (False, None)

ok, A_0 = backtrack(N-1,0)
if ok:
    print(A_0)
