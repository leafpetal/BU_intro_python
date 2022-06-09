# 
# ps3pr3.py - Problem Set 3, Problem 3
#
# More Algorithm design!
#

# function 1
def index(elem, seq):
    """return the index of the character elem 
    from the seq"""
    if len(seq) == 0:
        return -1
    elif seq[0] == elem:
        return 0
    else:
        index_rest = index(elem, seq[1:])
        if index_rest == -1:
            return index_rest
        elif seq[0] != elem:
            return index_rest + 1
#print(index('hi', ['hello', 111, True]))


# function 2
def index_last(elem, seq):
    """returns the index of the last occurence of elem in seq"""
    new_seq = seq[-1::-1]
    #print(new_seq)
    if len(new_seq) == 0:
        return -1
    elif new_seq[0] == elem:
        return len(seq) - 1
    else:
        index_rest = index_last(elem, new_seq[1:])
        if index_rest == -1:
            return index_rest
        elif new_seq[0] != elem:
            b = index_rest + 1
            return len(seq) - b - 1
#print(index_last(5, [4, 10, 5, 3, 7, 5]))
#print(index_last('n', 'banana'))
#print(index_last('b', 'banana'))
#print(index_last('i', 'team'))
#print(index_last(5, [4, 10, 5, 3, 7, 5]))


# function 3
def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values"""
    if values == []:
        return []
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest
    
def jscore(s1, s2):
    """return the number of characters that match between s1 and s2"""
    if len(s2) == 0 or len(s1) == 0:
        return 0
    elif s1[0] in s2:
        j_list = jscore(s1[1:], rem_first(s1[0], s2))
        return j_list + 1
    else:
        j2_list = jscore(s1[1:], s2)
        return j2_list
print(jscore('diner', 'syrup'))
print(jscore('always', 'bananas'))
