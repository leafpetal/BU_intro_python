# 
# for_loops1.py - Problem Set 5, Problem 1
#
# Processing sequences with loops
#


# function 1
def num_multiples(m, values):
    """return the number of integers in values that are the 
    multiples of m"""
    count = 0
    for i in values:
        if i % m == 0:
            count += 1
    return count
#print(num_multiples(9, [15, 18]))


# function 2 
def add_stars(s):
    """add a star between every character"""
    a = ''
    for i in range(len(s)-1):
        a += s[i] + '*'
    return a + s[-1]
#print(add_stars('hello'))


# function 3
def compare(s1, s2):
    """return the number of differences between s1 and s2"""
    diff = 0
    len_shorter = min(len(s1), len(s2))
    diff += max(len(s1), len(s2)) - len_shorter
    
    for i in range(len_shorter):
        if s1[i] != s2[i]:
            diff += 1
    return diff
#print(compare('aliens', 'alone'))


#function 4
def begins_with(prefix, wordlist):
    """return the list of all words in wordlist that
    start with the prefix"""
    pre_list = []
    for i in wordlist:
        if prefix == i[:len(prefix)]:
            pre_list += [i]
    return pre_list
#print(begins_with('on',['only', 'online', 'lily']))
