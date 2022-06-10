# 
# recursion2.py - Problem Set 2, Problem 3
#
# Fun with recursion, part 2
#

# function 1
def dot(vals1, vals2):
    """dot product of lists vals1 and vals2"""
    if len(vals1) != len(vals2):
        return 0.0
    elif len(vals1) == 0 and len(vals2) == 0:
        return 0.0
    else:
        rest = dot(vals1[1:], vals2[1:])
        if len(vals1) == len(vals2):  
            return rest + (vals1[0] * vals2[0])
        else:
            return rest
#print(dot([1, 2, 3, 4], [10, 100, 1000, 10000]))



# function 2
def any_odd(vals):
    """check if the list vals contain any odd numbers"""
    if len(vals) == 0:
        return False
    elif vals[0] % 2 == 1:
        return True
    else:
        odd_check = any_odd(vals[1:])
        if vals[0] % 2 == 0:
            if 0 + odd_check == 0:
                return False
            else:
                return True
        else:
            if 1 + odd_check > 0:
                return True
            else:
                return False    
#print(any_odd([8, 4, 5]))



# function 3
def process(vals):
    """replace odd elements in list vals with square of them"""
    if len(vals) == 0:
        return vals
    else:
        sq_odd = process(vals[1:])
        if vals[0] % 2 == 1:
            return [vals[0] ** 2] + sq_odd
        else:
            return [vals[0]] + sq_odd
#print(process([6, 3, 7]))
