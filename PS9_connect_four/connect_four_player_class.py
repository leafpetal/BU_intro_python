#
# connect_four_player_class.py - Problem Set 9, Problem 2
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    """ represent a player of the Connect Four game in combination
    with the Board class"""
    
    def __init__(self, checker):
        """ constructs a new Player object by initializing the two
        attributes checker and num_moves"""
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object; the string
        returned should indicate which checker the Player object
        is using"""
        return 'Player' + ' ' + str(self.checker)
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker
        of the Player object's opponent"""
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'
        
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns
        the column where the player wants to make the next move"""
        col = int(input('Enter a column: '))
        self.num_moves += 1
        
        if b.can_add_to(col) == True:
            return col
        elif b.can_add_to(col) == False:
            return "Try again!"
    
'''    
# test
player = Player('O')
print(player)
b = Board(6, 7)
print(player.next_move(b))
'''
