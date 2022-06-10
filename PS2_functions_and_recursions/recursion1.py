# 
# recursion1.py - Problem Set 2, Problem 2
#
# Fun with recursion, part 1
#

# function 1
def mult(vals):
    """return values obtained by multiplying all the elements of list vals"""
    if len(vals) == 1:
        return vals[0]
    else:
        product_rest = mult(vals[1:])
        return vals[0] * product_rest
# print(mult([5, 3, 2]))
   

# function 2     
def add_stars(s):
    """adding stars between characters of the string"""
    if len(s) == 1:
        return s
    else:
        str_rest = add_stars(s[1:])
        return s[0] + '*' + str_rest
# print(add_stars('hangman'))
