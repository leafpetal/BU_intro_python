#
# string_and_list_functions1.py - Problem Set 1, Problem 3
#
# Functions on strings and lists, part 1
#


# function 1
def last_first(values):
    """create a list containing the last and first elements of values """
    last = values[-1]
    first = values[0] 
    return [last, first]


# function 2
def every_other(values):
    """returning every other value from the original list"""
    return values[::2]
    
    
# function 3
def begins_with(word, prefix):
    """checking if prefix matches with the word"""
    if prefix == word[:len(prefix)]:
        return True
    else:
        return False
