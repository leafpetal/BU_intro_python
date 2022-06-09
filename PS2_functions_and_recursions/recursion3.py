# 
# ps2pr4.py - Problem Set 2, Problem 4
#
# Fun with recursion, part 3
#

# function 1
def letter_score(letter):
    """return the lowercase alphabets with according numbers"""
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    elif letter in ['d', 'g',]:
        return 2
    elif letter in ['b', 'c', 'm', 'p']:
        return 3
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    elif letter == 'k':
        return 5
    elif letter in ['j', 'x']:
        return 8
    elif letter in ['q', 'z']:
        return 10
    else:
        return 0
#print(letter_score('a'))


# function 2
def scrabble_score(word):
    """return the sum of scrabble scores of the string word"""
    if len(word) == 0:
        return 0
    else:
        word_rest = scrabble_score(word[1:])
        if word[0] == '':
            return 0 + word_rest
        else:
            return letter_score(word[0]) + word_rest
#print(scrabble_score('python'))


# function 3
def compare(s1, s2):
    """counting the number of different letters 
    between two strings s1 and s2"""
    if len(s1) == 0 and len(s2) == 0:
        return 0
    else:
        compare_list = compare(s1[1:], s2[1:])
        if s1[0] == s2[0]:
            return 0 + compare_list
        else:
            return 1 + compare_list
#print(compare('sane', 'sime'))


def weave(vals1, vals2):
    """Alternatively repeat each list's elements"""
    if len(vals1) == 0 and len(vals2) == 0:
        return []
    elif len(vals1) == 0:
        return vals2
    elif len(vals2) == 0:
        return vals1
    else:
        weave_list = weave(vals1[1:], vals2[1:])
        if len(vals1) == 0 and len(vals2) == 0:
            return [] + weave_list
        else:
            return [vals1[0]] + [vals2[0]] + weave_list
#print(weave([4,5], [2,2,2]))
