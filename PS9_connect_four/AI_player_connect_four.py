#
# AI_player_connect_four.py - Problem Set 9, Problem 4
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ look ahead some numbers of moves into the future to assess
    the impact of each possible move that it could make for its
    next move, and will assign a score to each possible move"""
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object;
        this method will override/replace the __repr__ method 
        that is inherited from Player"""
        return 'Player ' + str(self.checker) + " (" + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for eack column
        of the board and returns the index of the column with the
        maximum score; if tie, the method should apply the called
        AIPlayer's tiebreaking strategy"""
        max_list = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_list += [i]
        if self.tiebreak == 'LEFT':
            return max_list[0]
        elif self.tiebreak == 'RIGHT':
            return max_list[-1]
        else:
            return random.choice(max_list)
        
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called
        AIPlayer's scores for the columns in b 
        (either -1, 0, 50, 100)"""
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] == 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] == 0
                elif max(opp_scores) == 50:
                    scores[col] = 50
                else:
                    continue
                #scores[col] = 100 - opp_scores[opp.max_score_column(opp_scores)] 
                b.remove_checker(col)
        return scores
                
                
    def next_move(self, b):
        """ overrides the next_move method that is inherited from
        Player; this version should return the called AIPlayer's
        judgement of its best possible move"""
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
                
                
    
# test

'''
b = Board(6,7)
b.add_checkers('1211244445')

scores = [0,0,50,0,50,50,0]
p1 = AIPlayer('X', "RIGHT", 1)
print(p1.max_score_column(scores))

print(AIPlayer('X', 'LEFT', 0).scores_for(b))
print(AIPlayer('O', 'LEFT', 1).scores_for(b))
print(AIPlayer('X', 'LEFT', 2).scores_for(b))
print(AIPlayer('X', 'LEFT', 2).scores_for(b))

print(AIPlayer('X', 'RIGHT', 2).next_move(b))
'''
