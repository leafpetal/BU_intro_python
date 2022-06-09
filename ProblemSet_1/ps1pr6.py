# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:12:09 2021

@author: soomin oh
"""

# ps1pr5.py - Problem Set 1, Problem 6
#
# Functions on strings and lists, part 2



# function 1
def reverse(s):
    """reverse the sequences of characters in input string"""
    return s[::-1]


# function 2
def ends_match(s):
    """first letter and last letter of input should match"""
    if s[0] == s[-1]:
        return True
    else:
        return False
    
    
# function 3
def replace_start(values, new_start_vals):
    """replace first n elements of list values with new_start_vals elements"""
    a = len(values)
    b = len(new_start_vals)
    if b < a:
        return new_start_vals[:] + values[b:]
    else:
        return new_start_vals


# function 4
def adjust(s, length):
    """pad s with its last character if it is too short"""
    a = len(s)
    if a < length:
        b = length - a
        return s + s[-1]*b
    elif a == length:
        return s
    else:
        return s[:length]