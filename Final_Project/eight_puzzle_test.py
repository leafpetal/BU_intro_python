#
# eight_puzzle_test.py - Final project
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Soomin Oh
# email: soh0223@bu.edu
#


from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
            
# p6, 1
def process_file(filename, algorithm, param):
    """ filename: specifying the name of a text file in which each
    line a digit string for an eight puzzle
    algorithm: specifies which state-space search algorithm should
    be used to solve the puzzles
    param: allows to specify a parameter for the searcher(either
    depth limit or heuristic)"""
    file = open(filename, 'r')
    t_moves = 0
    t_trials = 0
    n = 0
    for line in file:
        line = line[:-1] #chop off newline at end
        #print(len(line), 'ygyg')
        
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return

        soln = None
       
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print(line + ':', 'search terminated, ', end = '')
        
        
        if soln != None:
            moves = soln.num_moves
            trials = searcher.num_tested
            t_moves += soln.num_moves
            t_trials += searcher.num_tested
            n += 1
            print(line + ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested')

        if soln == None:
            print('no solution')
        
    print('solved', n,' puzzles')
    print('averages:', t_moves/n, 'moves,', t_trials/n, 'states tested')
