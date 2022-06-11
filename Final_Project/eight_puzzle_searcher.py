#
# eight_puzzle_searcher.py - Final project
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Soomin Oh
# email: soh0223@bu.edu
#


import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    # p3, 1
    def __init__(self, depth_limit):
        """ constructs a new Searcher object by initializing attributes
        states, num_tested, and depth_limit"""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
        
    # p3, 2    
    def add_state(self, new_state):
        """ takes a single State object called new_state and
        adds it to the Searcher's list of untested states.
        No return value!"""
        self.states.append(new_state)
            
            
    # p3, 3        
    def should_add(self, state):
        """ takes a State object called state and returns True
        if the called Searcher should add state to its list of 
        untested states, and False otherwise"""
        if self.depth_limit != -1 and self.num_tested > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True
        
     
    # p3, 4    
    def add_states(self, new_states):
        """ takes a list State objects called new_states and that 
        processes the elements of new_states one at a time"""
        for i in new_states:
            if self.should_add(i) == True:
                self.add_state(i)
            else:
                pass
            
    
    # p3, 5    
    def next_state(self):
        """chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it"""
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    
    # p3, 6 *******확실 X
    def find_solution(self, init_state):
        """ performs a full state_space search that begins at the 
        specified initial state init_state and ends when the goal
        state is found or when the Searcher runs out of untested
        states"""
        self.add_state(init_state)
        while len(self.states) > 0:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal():
                #self.num_tested += 1
                return s
            else:
                self.add_states(s.generate_successors())
        return None
        
    

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###
# p4, 1
class BFSearcher(Searcher):
    """ chooses one the untested states that has the smallest depth
    (i.e., the smallest number from the initial state).
    Subclass of class Searcher"""
    
    def next_state(self):
        """ overrides the next_state method that is inherited from 
        Searcher. Not random, it follows FIFO(first in first out"""
        s = self.states[0]
        self.states.remove(s)
        return s


# p4, 2
class DFSearcher(Searcher):
    """ perform depth-first search(DFS) instead of random search.
    Involves always choosing one the untested states that has the
    largest depth (i.e., the largest number of moves from the
    initial state)"""
    
    def next_state(self):
        """ overrides Searcher's next_state method following 
        LIFO(last in last out)"""
        s = self.states[-1]
        self.states.remove(s)
        return s


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
# p5, 1.d
def h1(state):
    """ takes a State object called state and that computes and
    returns an estimate of how many additional moves are needed
    to get from state to the goal state. Its estimate should simply
    be the number of misplaced tiles in the Board object associated with
    state"""
    return state.board.num_misplaced()

# p6, 4
def h2(state):
    """ counts misplaced tiles as either 1 or 2 based on the wrong
    positions. 2 if both rows and columns do not match and 1 if
    either row or column does not match"""
    return state.board.helper_h2()
    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    # p5, 1.b
    def __init__(self, heuristic):
        """ constructs a new GreedySearcher object"""
        super().__init__(-1)
        self.heuristic = heuristic
    

    # p5, 1.c
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    
    # p5, 1.e
    def add_state(self, state):
        """ overrides the add_state method that is inherited from
        Searcher. Rather than adding the specified state to the
        list of untested states, add a sublist that is a 
        [priority, state] pair"""
        ps_list = []
        p = self.priority(state)
        s = state
        ps_list += [p]
        ps_list += [s]
        self.states.append(ps_list)
        
        
    # p5, 1.f
    def next_state(self):
        """ overrides the next_state method that is inherited
        from Searcher. This version should choose one of the states
        with the highest priority"""
        max_list = max(self.states)
        max_p = max_list[-1]
        self.states.remove(max_list)
        return max_p
        
    

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###
# p5, 2
class AStarSearcher(GreedySearcher):
    """ informed search algorithm that assigns a priority to each
    state based on those priorities. However, when A* assigns
    priority to a state, it also takes into account the cost that
    has already been expended to get that state"""
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        #print(self.heuristic(state))
        #print(state.num_moves)
        return -1 * (self.heuristic(state) + state.num_moves)
    



# test
'''
searcher2 = Searcher(10)
print(searcher2)

searcher = Searcher(-1)
print(searcher.states)
s = State(Board('142358607'), None, 'init')
searcher.add_state(s)
print(searcher.states)

searcher = Searcher(-1)
s = State(Board('012345678'), None, 'init')
print(s)
searcher.find_solution(s)
'''
