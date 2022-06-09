# 
# ps2pr1.py - Problem Set 2, Problem 1
#
# More practice writing non-recursive functions
#

# function 1
def longer(s1, s2):
    """return longer string between s1 and s2"""
    if len(s1) > len(s2):
        return s1
    elif len(s1) < len(s2):
        return s2
    else:
        return s1
# print(longer('hello', 'again'))
    
    
# function 2
def swap_halves(s):
    """return second half of s + first half of s"""
    if len(s) % 2 == 1:
        a = len(s) // 2
        return s[a:] + s[:a]
    else:
        b = len(s) // 2
        return s[b:] + s[:b]
# print(swap_halves('homework'))
# print(swap_halves('carpets'))


# function 3
def repeat_one(values, index, num_times):
    """return new list repeating the element in index place for num_times"""
    a = values[index:index + 1]
    b = num_times
    x = a * b
    return values[:index] + x + values[index + 1:]
# print(repeat_one([10, 11, 12, 13], 2, 4))
# print(repeat_one([5, 6, 7], 1, 3))
