#
# eight_puzzle_board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Soomin Oh
# email: soh0223@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] += digitstr[3*r + c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
        

    ### Add your other method definitions below. ###
    def __repr__(self):
        """returns a string representation of a Board object"""
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] == '0':
                    s += '_' + ' '
                else:
                    s += str(self.tiles[row][col]) + ' '

            s += '\n'  # newline at the end of the row
        return s
    
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the
        direction in which the blank should move and that attempts
        to modify the contents of the called Board object"""
        a = self.blank_r
        #print(a)
        b = self.blank_c
        #print(b)
        if direction == 'up':
            if a - 1 <= 2 and a - 1 >= 0:
                #c = self.tiles[a-1][b]
                self.tiles[a][b] = self.tiles[a-1][b]
                self.tiles[a-1][b] = '0'
                self.blank_r = a-1
                return True
            else:
                return False
        elif direction == 'down':
            if a + 1 <= 2 and a + 1 >= 0:
                self.tiles[a][b] = self.tiles[a+1][b]
                self.tiles[a+1][b] = '0'
                self.blank_r = a+1
                return True
            else:
                return False
        elif direction == 'right':
            if b + 1 <= 2 and b + 1 >= 0:
                self.tiles[a][b] = self.tiles[a][b+1]
                self.tiles[a][b+1] = '0'
                self.blank_c = b+1
                return True
            else:
                return False
        elif direction == 'left':
            if b - 1 <= 2 and b - 1 >= 0:
                self.tiles[a][b] = self.tiles[a][b-1]
                self.tiles[a][b-1] = '0'
                self.blank_c = b-1
                return True
            else:
                return False
        else:
            return False
                
        
    def digit_string(self):
        """ creates and returns a string of digits that corresponds
        to the current contents of the called Board object's tiles
        attribute"""
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':####
                    self.tiles[r][c] = '0'
                    s += self.tiles[r][c]
                else:
                    s += self.tiles[r][c]
        return s
    
    
    def copy(self):
        """ returns a newly-constructed Board object that is a 
        deep copy of the called object"""
        copy = self.digit_string()[:]
        copy_board = Board(copy)
        return copy_board
        
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called
        Board object that are not where they should be in the goal
        state. Do not include the blank cell in this count"""
        count = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != str(3*r + c) and \
                    self.tiles[r][c] != '0':
                    count += 1
                    
        return count
    
    def __eq__(self, other):
        """ called when the == operator is used to compare two 
        Board objects. Return True if self and other have the same
        values and False otherwise"""
        if self.digit_string() == other.digit_string():
            return True
        else:
            return False
        
        
    # p6, 4
    def helper_h2(self):
        """ helper function for heuristic 2 function"""
        n = 0
        for r in range(3):
            for c in range(3):
                #print(self.tiles[r][c])
                if self.tiles[r][c] != str(3*r + c) and \
                    self.tiles[r][c] != '0':
                        if int(self.tiles[r][c]) // 3 != r and\
                            int(self.tiles[r][c]) % 3 != c:
                            n += 2
                            #print('r and c misplaced')
                        elif int(self.tiles[r][c]) // 3 != r or\
                            int(self.tiles[r][c]) % 3 != c:
                            n += 1
                            #print('r or c misplaced')
                        else:
                            n += 0
        return n

'''
# test
d = Board('142358607')
d.move_blank('up')


print(d.tiles)
print(d.blank_r)
print(d.blank_c)
print(d)
str(d)

#print(d.move_blank('left'))
print(d.digit_string())
print(d.num_misplaced())

d = Board('142358607')
f = Board('142358607')
'''
