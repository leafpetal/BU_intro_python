# 
# binary_decimal.py - Problem Set 4, Problem 1
#
# From binary to decimal and back!
#

# function 1
def dec_to_bin(n):
    """return decimal number to binary number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        dec_rest = dec_to_bin(n//2)
        if n // 2 >= 1:
            if n % 2 == 0:
                return str(dec_rest) + '0'
            else:
                return str(dec_rest) + '1'
        else:
            return dec_rest
#print(dec_to_bin(11))


# function 2
def bin_to_dec(n):
    """return binary number to decimal number"""
    if len(n) == 0:
        return 0
    elif n == 1:
        return 1
    else:
        bin_rest = bin_to_dec(n[:-1])
        if n[-1] == '1':
            return 2 * bin_rest + 1
        elif n[-1] == '0':
            return 2 * bin_rest
#print(bin_to_dec('1011'))
