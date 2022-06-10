# 
# binary_functions1.py - Problem Set 4, Problem 2
#
# Functions that process binary numbers
#

# function 1
def count_evens_rec(binvals):
    """return the numbers of even binary numbers 
    using recursion"""
    if len(binvals) == 0:
        return 0
    else:
        bin_rest = count_evens_rec(binvals[1:])
        if binvals[0][-1] == '0':
            return bin_rest + 1
        else:
            return bin_rest
#print(count_evens_rec(['1100', '10011', '101', '010']))


# function 2
def count_evens_lc(binvals):
    """return the numbers of even binary numbers
    using list comprehension"""
    even_bin = [i for i in binvals if i[-1] == '0']
    return len(even_bin)
#print(count_evens_lc(['1100', '10011', '101', '010']))


# function 3
def add_bitwise(b1, b2):
    """return the addition result of binary numbers,
    b1 and b2"""
    if len(b1) == 0:
        return b2
    elif len(b2) == 0:
        return b1
    else:
        bit_rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] != b2[-1]:
            return bit_rest + '1'
        else:
            if b1[-1] == '0' and b2[-1] == '0':
                return bit_rest + '0'
            else:
                """1 + 1"""
                return add_bitwise(bit_rest, b2[-1]) + '0'         
        
#print(add_bitwise('11', '100'))
