# 
# ps3pr1.py - Problem Set 3, Problem 1
#
# Algorithm design
#

# function 1
def abs_list_lc(values):
    """return the absolute values of the elements 
    in list values, using list comprehension"""
    return [abs(x) for x in values]
#print(abs_list_lc([2,-3,4,-20]))


# function
def abs_list_rec(values):
    """return the absolute values of the elements 
    in list values, using recursion"""
    if len(values) == 0:
        return []
    else:
        abs_list = abs_list_rec(values[1:])
        if values[0] < 0:
            return [-1 * values[0]] + abs_list
        else:
            return [values[0]] + abs_list
#print(abs_list_rec([2,-3,4,-20]))


# function 3
def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest
    
def most_vowels(words):
    """return the element with the most vowels"""
    v_list = [num_vowels(x) for x in words]
    return words[max(v_list)-1]
#print(most_vowels(['obama','are','amazing']))


 # function 4
def num_multiples(m, values):
    """return the number of elements which are the multiple of m"""
    return len([x for x in values if x % m == 0])
#print(num_multiples(3, [2,4,6]))


# function 5
def begins_with(prefix, wordlist):
    """return only the elements that has the prefix"""
    a = len(prefix)
    return [x for x in wordlist if prefix == x[:a]]
#print(begins_with('D', ['Alex', 'Alison', 'Adriel','Alina']))
