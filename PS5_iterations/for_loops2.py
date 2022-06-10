# 
# for_loops2.py - Problem Set 6, Problem 3
#
# Functions that use loops
#

# function 1
def BUtify(s):
    """Turn lower case b's and u's into upper case B's and U's"""
    for i in range(len(s)):
        if s[i] == 'b':
            s = s[:i] + 'B' + s[i+1:]
        elif s[i] == 'u':
            s = s[:i] + 'U' + s[i+1:]
    return s
#print(BUtify('beautiful'))


# function 2
def diff(vals1, vals2):
    """return the list of differences between vals1 and vals2"""
    max_list = max(len(vals1), len(vals2))
    diff_list = []
    a = len(vals1)
    b = len(vals2)
    
    if a > b:
        vals2 += [0] * (a-b)
    elif a < b:
        vals1 += [0] * (b-a)
        
    for i in range(max_list):
        diff_list += [abs(vals1[i] - vals2[i])]
    return diff_list
#print(diff([3,4,2,5], [7,2,9,5]))


# function 3
def index(elem, seq):
    """return the index of the first occurence of elem in seq"""
    for i in range(len(seq)):
        if elem == seq[i]:
            return i
            break
    return -1
#print(index('i','team'))


# function 4
def square_evens(vals):
    """return even elements of vals into their square values
    and odd elements unchanged"""
    for i in range(len(vals)):
        if vals[i] % 2 == 0:
            vals[i] = vals[i]**2
    #return vals
print(square_evens([1,2,3,4,5,6]))
    
