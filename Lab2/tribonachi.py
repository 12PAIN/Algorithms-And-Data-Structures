#     |1 2 3 4 5  6  7
#0 0 1 1 2 4 7 13 24 44

def tribonachi(n):
    if n < 0: return 0
    if n in (0,1): 
        return 1
    return tribonachi(n-1) + tribonachi(n-2) + tribonachi(n-3)

print(tribonachi(2))