#
# markov_text_generator.py - Problem Set 8, Problem 1
#
# Markov text generation       
#

import random

# function 1
def create_dictionary(filename):
    """ takes a string representing the name of a text file and
    that returns a dictionary of key-value pairs in each """
    file = open(filename, 'r') # bigbang.txt or brave.txt or edited_mission.txt
    text = file.read()
    words = text.split()
    
    D = {}
    current_word = '$'
    punc = ['.', '!', '?']
    for next_word in words:
        if current_word not in D:
            D[current_word] = [next_word]
        else:
            D[current_word] += [next_word]
            
        if next_word[-1] in punc:
            current_word = '$'
        else:
            current_word = next_word
    return D
            

# function 2
def generate_text(word_dict, num_words):
    """ takes as parameters a dictionary of word transitions 
    (generated by the create_dictionary function) named word_dict
    and a positive integer. The function must print the words
    it generates, not returning a value"""
    current_word = '$'
    punc = ['.', '!', '?']
    #gen_text = ''
    for next_word in range(num_words): # next_word right?
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word, end = ' ')
        #gen_text += next_word + ' '
        if next_word[-1] in punc:
            current_word = '$'
        else:
            current_word = next_word
    #return gen_text


# test
'''
word_dict = create_dictionary('brave.txt')
print(generate_text(word_dict, 20))
#print(word_dict) 
'''
