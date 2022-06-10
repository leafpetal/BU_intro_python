#
# 2D_lists.py - Problem Set 6, Problem 5
#
# 2-D Lists
#
# Computer Science 111
# 

import random

def create_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = []
    
    for r in range(num_rows):
        row = [0] * num_cols     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form, with each row on its own line.
        input: grid is a 2-D list
    """
    num_rows = len(grid)
    for r in range(num_rows):
        if r == 0:
            print('[', end='')
        else:
            print(' ', end='')
        if r < num_rows - 1:
            print(str(grid[r]) + ',')
        else:
            print(str(grid[r]) + ']')

def random_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions in which each cell is assigned a random integer from 0-9.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = random.choice(range(10))
            
    return grid

# function 1
def row_index_grid(num_rows, num_cols):
    """
        creates and returns a 2-D list with the specified dimensions in which each cell has as its value.
        the index of the row to which the cell belongs
    """
    grid = []
    
    for r in range(num_rows):
        row = [r] * num_cols
        grid += [row]

    return grid
#print(row_index_grid(5, 4))


# function 2
def num_between(grid, n1, n2):
    """
        takes a 2-D list of integers grid and two integers n1 and n2, and returns the number of values in grid that are between n1 and n2
    """
    i = 0
    if n1 > n2:
        return 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            val = grid[r][c]
            if val >= n1 and val <= n2:
                i += 1
    return i
#print(num_between([[0, 4, 8], [6, 10, 5]], 11, 7))


# function 3
def copy(grid):
    """
        creates and returns the deep copy of grid, not a reference of grid
    """
    new_grid = []
    new_grid += [[]]*len(grid)
    for i in range(len(grid)):
        new_grid[i] = grid[i][:]
    #new_grid[0][0] = 1
    return new_grid

#print(copy([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]]))


# function 4
def double_with_cap(grid, cap):
    """
        return the grid with its elements doubled, but return cap when the doubled values are greater than cap
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] * 2 < cap:
                grid[i][j] *= 2
            else:
                grid[i][j] = cap
    #return grid
#print(double_with_cap([[1, 3, 4], [6, 0, 5]], 9))


# function 5
def sum_evens_in_col(grid, colnum):
    """
        return the sum of even numbers in the according column
    """
    even_sum = 0
    for i in range(len(grid)):
        if grid[i][colnum] % 2 == 0:
            even_sum += grid[i][colnum]
    return even_sum
#print(sum_evens_in_col([[1, 3, 4], [4, 5, 6], [8, 9, 10]], 2))
    
