#
# play_connect_four.py - Problem Set 9, Problem 3
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b):
    """ takes two parameters, p, for a Player for whose move
    is being processed and b, for a Board object on which the game
    is being played"""
    print('Player', p.checker + "'s turn")
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    if b.is_full() == True:
        if b.is_win_for(p.checker) == False and \
            b.is_win_for(p.opponent_checker()) == False:
            print("It's a tie!")
            return True
            
    else:
        if b.is_win_for(p.checker) == True:
            print('Player', p.checker, 'wins in', p.num_moves,'moves.')
            print('Congratulations!')
            return True
        else:
            return False
        

class RandomPlayer(Player):
    """ used for an unintelligent computer player that chooses
    at random from the available columns; this class should be
    a subclass of the Player class"""
    
    def next_move(self, b):
        """ overrides the next_move method that is inherited form Player;
        should choose at random from the columns in the board b
        that are not yet full and return the index of that column"""
        avail_list = []
        for c in range(b.width):
            if b.can_add_to(c) == True:
                avail_list += [c]
        self.num_moves += 1
        while True:
            col = random.choice(avail_list)
            return col
            break
    
    
    
# test
'''
b1 = Board(2, 4)
b1.add_checkers('001122')
process_move(Player('X'), b1)
#b1.remove_checker(3)
#print(process_move(Player('X'), b1))
p = RandomPlayer('X')

connect_four(Player('O'), Player('X'))
'''
