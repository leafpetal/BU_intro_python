# 
# choosing_loop_type.py - Problem Set 5, Problem 2
#
# Choosing the correct type of loop
#

# function 1
def log(b, n):
    """return the logarithm to the base b of a number n"""
    a = 0
    if n == 1:
        return 0
    
    while True:
        print('dividing', n, 'by', b, 'gives', n // b)
        n = n // b
        a += 1
        if n <= 1:
            break
    return a
#print(log(2, 20))


# function 2
def add_powers(m, n):
    """add together the first m powers of n (from 0 to m-1)"""
    add_var = 0
    for i in range(m):
        print(n, '**', i, '=', n**i)
        add_var += n**i
    return add_var
#print(add_powers(3, -6))
        
