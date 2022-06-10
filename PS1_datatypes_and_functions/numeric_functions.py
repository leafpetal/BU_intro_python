# 
# numeric_functions.py - Problem Set 1, Problem 2
#
# Functions with numeric inputs
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x


# function 1
def root(x):
    """returns the square root of its input"""
    return x ** 0.5

# function 2
def gap(num1, num2):
    if num1 > num2:
        return num1 - num2
    elif num1 < num2:
        return num2 - num1
    else:
        return 0
    
#function 3
def larger_gap(a1, a2, b1, b2):
    a = gap(a1, a2)
    b = gap(b1, b2)
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a
    
# function 4
def median(a, b, c):
    if a <= b <= c:
        return b
    elif a <= c <= b:
        return c
    elif b <= a <= c:
        return a
    elif b <= c <= a:
        return c
    elif c <= a <= b:
        return a
    else:
        return b


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
