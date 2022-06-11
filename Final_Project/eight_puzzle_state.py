#
# eight_puzzle_state.py - Final project
#
# A State class for the Eight Puzzle
#
# name: Soomin Oh
# email: soh0223@bu.edu
#


from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
    def __init__(self, board, predecessor, move):
        """constructs a new State object by initializing the following
        four fields/attributes
        board: Board object associated with this state
        predecessor: stores a reference to the State object that
                    comes before this state
        move: 0 or 1/move between current state and predecessor
        num_move: total moves that were needed to get from initial
                    state to current state"""
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if self.predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves + 1
        
        
    def is_goal(self):
        """ returns True if the called State object is a goal state,
        and False otherwise"""
        goal = ''
        for r in range(3):
            for c in range(3):
                goal += GOAL_TILES[r][c]
        if self.board.digit_string() == goal:
            return True
        else:
            return False
        
        
    def generate_successors(self):
        """ creates and returns a list of State object for all
        successor states of the called State object"""
        successors = []
        for m in MOVES:
            #print(m)
            b = self.board.copy()
            #print(b)
            c = b.move_blank(m)
            if c == True:
                new_state = State(b, self, m)
                successors += [new_state]
        return successors
        
        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    
    
    # part 3, def 7
    def print_moves_to(self):
        """ prints the sequence of moves that lead from the initial
        state to the called State object.
        follow predecessor references back up the state-space search tree
        in order to find and print the sequence of moves"""
        if self.predecessor == None:
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print('move the blank', self.move + ':')
            print(self.board)
            
        

# test
'''
b1 = Board('142358607')
s1 = State(b1, None, 'init')
print(s1)

b2 = b1.copy()
print (b2)
#print(b2.move_blank('up'))
s2 = State(b2, s1, 'up')
print(s2)

s1 = State(Board('012345768'), None, 'init')
print(s1.is_goal())

b1 = Board('142358607')
s1 = State(b1, None, 'init')
succ = s1.generate_successors()
print(succ)
'''
