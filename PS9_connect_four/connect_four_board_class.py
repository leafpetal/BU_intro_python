#
# connect_four_board_class.py - Problem Set 9, Problem 1
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        """ constructs a new board object by initializing an attribute
        height, width, and slots """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
        
    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '-' * (2 * self.width + 1)     # 2n + 1
        s += '\n'
        for c in range(self.width):
            s+= ' '
            if c < 10:
                s += str(c)
            else:
                s += str(c % 10)
        
        return s
    

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0
        while self.slots[row][col] == ' ':
            row += 1
            if row == self.height - 1:
                break
        if self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker

    
    ### add your reset method here ###
    def reset(self):
        """ reset the Board object on which it is called by setting
        all slots to contain a space character"""
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """ return False if the checker is not placed in a valid space
        and otherwise return True"""
        if col < 0 and col >= self.width:
            return False
        else:
            #row = self.height
            if self.slots[0][col] == ' ':
                return True
            else:
                return False
            
    def is_full(self):
        """ return True if the called Board object is completely
        full of checkers, and return False otherwise"""
        for c in range(self.width):
            if self.can_add_to(c):
                return False
        return True
    
    def remove_checker(self, col):
        """ removes the top checker form column col of the called
        Board object and if the column is empty, then the method 
        does nothing"""
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                self.slots[r][col] = ' '
                break
            
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ checks for a vertical win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                        return True
        return False
    
    def is_down_diagonal_win(self, checker):
        """checks for a downward diagonal win for the checker"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                        return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """checks for an upward diagonal win for the checker"""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker:
                        return True
        return False
    
    
    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'O' or 'X'
        and returns True is there are four consecutive slots
        containing checkers on the board"""
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        else:
            return False
    
                

'''
# test
board = Board(4,11)
board.add_checker('O', 3)
board.add_checker('X', 4)
board.add_checker('O', 4)
board.add_checker('X', 5)
board.add_checker('X', 5)
board.add_checker('O', 5)
board.add_checker('X', 6)
board.add_checker('X', 6)
board.add_checker('X', 6)
board.add_checker('O', 6)
print(board.__repr__())
#board.reset()
#print(board.__repr__())
#print(board.can_add_to(3))

print(board.is_win_for('O'))

b2 = Board(2,2)
b2.add_checkers('0011')
print(b2.is_full())
'''
