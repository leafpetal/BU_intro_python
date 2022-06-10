# 
# binary_funtions2.py - Problem Set 4, Problem 3
#
# Using your conversion functions
#
from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin

# function 1
def mul_bin(b1, b2):
    """multiply two binary numbers and return the result"""
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    b = n1 * n2
    return dec_to_bin(b)
#print(mul_bin('1001', '101'))


# function 2
def largest_bin(binvals):
    """return the largest value among binvals list"""
    dec_list = [bin_to_dec(i) for i in binvals]
    dec_max = max(dec_list)
    return dec_to_bin(dec_max)
#print(largest_bin(['1100', '10011', '101', '10000']))
