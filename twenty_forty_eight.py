"""
Clone of the original 2048 game.
Created by Egbie Anderson Uku
created on the 29th May 2016
"""

#import poc_2048_gui        
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 

COORDINATES = {UP:[],  DOWN:[], LEFT:[], RIGHT:[]}
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = filter(None, line)
    
    for var_i in xrange(1, len(new_line)):
        if new_line[var_i -1] == new_line[var_i]:
            new_line[var_i -1] <<=  1
            new_line[var_i] = 0
                        
    new_line = filter(None, new_line)
    return (new_line + ([0]*( len(line) - len(new_line)))) # add zeroes to the end of new list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width =  grid_width
        self._grid = self.reset()
     
        print "[+] Initializing please wait ..."

        # pre-computing the values for the right, left, down and up and store
        # in dictionary
        for var_i in xrange(self._width):
            COORDINATES[UP].append((0, var_i))
            COORDINATES[DOWN].append((self._height-1, var_i))
            
        for var_j in xrange(self._height):
            COORDINATES[RIGHT].append((var_j,0))
            COORDINATES[LEFT].append((var_j, self._height-1))
                                     
        # generate all coordinates and store in coordinates only needs to be computed once
       # self._grid = [[8,4,4,2,0],[0,2,2,16,0],[0,0,0,4,0],[0,0,0,0,0]]
        
                    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str("There are %d rows and %d columns." %(self.get_grid_height(), self.get_grid_width()))
    
    def get_grid_height(self):
        """get_grid_height(void) -> return(int)
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """get_grid_width(void) -> return(int)
        Get the width of the board.
        """
        return self._width

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.rows, self.cols = self.get_grid_height(), self.get_grid_width()
        return([[0 for dummy_col in range(self.cols)] for dummy_row in range(self.rows)])

    def get_grid(self):
        """get_grid(void) -> returns(list)
        Returns the entire board
        """
        return self._grid
    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self.offset, self.moved = OFFSETS[direction], False
        self.coordinates = COORDINATES[direction]
        
        print self.coordinates
        print self.offset
        for coordinate in self.coordinates:
            self.values, self.board =[coordinate], [self.get_tile(coordinate[0], coordinate[1])]
            for dummy_i in xrange(len(self.coordinates)-1):
                self.x, self.y = (coordinate[0] + self.offset[0]) , (coordinate[1] + self.offset[1])
                coordinate = (self.x, self.y)
                self.values.append(coordinate)
                self.board.append(self.get_tile(coordinate[0], coordinate[1]))
                
            self.tmp = merge(self.board)
            
            # restore grid
            for num, pairs in enumerate(self.values):
                self.set_tile(pairs[0], pairs[1], self.tmp[num])

            if self.tmp != self.board: self.moved = True
        if self.moved: self.new_tile()

        
    def get_empty_cells_coordinates(self):
        """get_empty_cells_cordinates(void) -> return(list)
        From the matrix returns only the empty cells.
        Returns a list of tuples containing the coordinates of the
        empty cells in the form of (i,j).
        """
        self.row, self.col = self.get_grid_height(), self.get_grid_width()
        self.grid = self.get_grid()
        
        return ([(cell_row, cell_height) for cell_row in xrange(self.row) \
                     for cell_height in xrange(self.col) if not self.grid[cell_row][cell_height]])
                
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        self.cells = random.choice(self.get_empty_cells_coordinates())   # pick a random coordinate 
        self.row, self.col = self.cells

        # returns 2 90 percent of the time and 4 10 percent of the time.
        if random.randint(1, 10) <= 9:
            self.set_tile(self.row, self.col, 2)
            return
        self.set_tile(self.row, self.col, 4)
                
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        if row < self.get_grid_height()  or col < self.get_grid_width() :
            self.get_grid()[row][col] = value
        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        if row < self.get_grid_height()  or  col < self.get_grid_width():
            return self.get_grid()[row][col]
 
    
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
