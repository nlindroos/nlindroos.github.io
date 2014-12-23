'''
Created on 2.3.2013

@author: Nicke
'''

import random
from stack import Stack
    
    
class Labyrinth(object):

    def __init__(self, size):
        self.size = [size[0], size[1]]
        # self.size = [x-value, y-value]
        self.x_size = self.size[0]
        self.y_size = self.size[1]
        #random.seed(13)
        self.x = random.randint(1, self.x_size-2)   # x-coordinate for the current square. Does not choose perimeter squares
        self.y = random.randint(1, self.y_size-2)   # y-coordinate for the current square. Does not choose perimeter squares
        self.bridge_count = 0
        
        self.total_cells = self.x_size*self.y_size
        self.matrix = list(list(1 for i in range(self.y_size)) for j in range(self.x_size))

        '''
        matrix = columns*[len(column)*1]
        The matrix is a list containing the columns
        The columns are lists containing len(column) number of 1's
        To manipulate (2,3) in matrix: matrix[2][3]
        7 means exit, 0 means passage, 1 wall, 2 bridge north, 3 south, 4 bridge east, 5 bridge west and 8 means player
        '''
        self.visited = list(list(0 for i in range(self.y_size)) for j in range(self.x_size))
        self.matrix = self.generate()
        #self.matrix_copy = self.matrix
        
        
    def generate(self):
        '''
        Depth-first search

        1. Pick a random starting location as the "current cell" and mark it
           as "visited".  Also, initialize a stack of cells to empty (the stack
           will be used for backtracking).  Initialize VISITED (the number of
           visited cells) to 1.
        2. While VISITED < the total number of cells, do the following:
             If the current cell has any neighbors which haven't yet been visited,
               pick one at random.  Push the current cell on the stack and set the
               current cell to be the new cell, marking the new cell as visited.
               Knock out the wall between the two cells.  Increment VISITED.
             If all of the current cell's neighbors have already been visited, then
               backtrack.  Pop the previous cell off the stack and make it the current
               cell.
        '''
        
        i = 0
        while i<len(self.visited[0]):
            self.visited[0][i] = 1   # First column
            self.visited[self.x_size-1][i] = 1   # Last column
            i+=1
        i = 0
        while i<len(self.visited):
            self.visited[i][0] = 1   # First row
            self.visited[i][self.y_size-1] = 1   # Last row
            i+=1
            
        stack = Stack()
        x_stack = Stack()   # Contains x-values for squares in stack
        y_stack = Stack()   # Contains y-values for squares in stack
        total_bridges = self.total_cells/80  # total_bridges = (maximum amount of bridges in the maze - 1)
        current = self.matrix[self.x][self.y]
        visited_count = 1
        self.visited[self.x][self.y] = 1
        
        while 1:
            choices = []
            while True:
                # Checks that square not out of bounds, not visited and no passage next to the square
                if (self.y-1)>=1 and not self.visited[self.x][self.y-1] and self.matrix[self.x][self.y-2] and self.matrix[self.x-1][self.y-1] and self.matrix[self.x+1][self.y-1]:
                    choices.append(1)   # North
                if (self.x+1)<=(self.x_size-1) and not self.visited[self.x+1][self.y] and self.matrix[self.x+1][self.y-1] and self.matrix[self.x+1][self.y+1] and self.matrix[self.x+2][self.y]:
                    choices.append(2)   # East
                if (self.y+1)<=(self.y_size-1) and not self.visited[self.x][self.y+1] and self.matrix[self.x][self.y+2] and self.matrix[self.x-1][self.y+1] and self.matrix[self.x+1][self.y+1]:
                    choices.append(3)   # South
                if (self.x-1)>=1 and not self.visited[self.x-1][self.y] and self.matrix[self.x-2][self.y] and self.matrix[self.x-1][self.y-1] and self.matrix[self.x-1][self.y+1]:
                    choices.append(4)   # West
                if len(choices)>0:
                    choice = random.choice(choices)
                if len(choices)==0:
                    break
                if choice==1:   # North
                    stack.push(current)
                    x_stack.push(self.x)
                    y_stack.push(self.y)
                    current = self.matrix[self.x][self.y-1]
                    self.visited[self.x][self.y-1] = 1 # Marks the cell as visited
                    self.matrix[self.x][self.y-1] = 0 # Removes the wall in the square
                    self.y = self.y-1 # Updates the y-value
                    visited_count+=1
                            
                elif choice==2: # East
                    stack.push(current)
                    x_stack.push(self.x)
                    y_stack.push(self.y)
                    current = self.matrix[self.x+1][self.y]
                    self.visited[self.x+1][self.y] = 1 # Marks the cell as visited
                    self.matrix[self.x+1][self.y] = 0 # Removes the wall in the square
                    self.x = self.x+1 # Updates the x-value
                    visited_count+=1
                            
                elif choice==3: # South
                    stack.push(current)
                    x_stack.push(self.x)
                    y_stack.push(self.y)
                    current = self.matrix[self.x][self.y+1]
                    self.visited[self.x][self.y+1] = 1 # Marks the cell as visited
                    self.matrix[self.x][self.y+1] = 0 # Removes the wall in the square
                    self.y = self.y+1 # Updates the y-value
                    visited_count+=1
                
                elif choice==4: # West
                    stack.push(current)
                    x_stack.push(self.x)
                    y_stack.push(self.y)
                    current = self.matrix[self.x-1][self.y]
                    self.visited[self.x-1][self.y] = 1 # Marks the cell as visited
                    self.matrix[self.x-1][self.y] = 0 # Removes the wall in the square
                    self.x = self.x-1 # Updates the x-value
                    visited_count+=1
                choices = []
                if self.bridge_count<=total_bridges:
                    self.set_bridge()   # Checks for, and sets possible bridges
                
            current = stack.pop()
            if current:
                self.x = x_stack.pop()
                self.y = y_stack.pop()
                
            else:
                break
            
        
        # Adds the exit to the labyrinth
        exit_square = random.randint(1, len(self.matrix)-2)
        while self.matrix[exit_square][1]:  # Loops while not passage south of exit_square
            exit_square = random.randint(1, len(self.matrix)-2)
        self.matrix[exit_square][0] = 7
        return self.matrix
        
        
    def set_bridge(self):
        
        bridges = [2, 3, 4, 5]  # List containing numbers representing bridges
        
        # North-south bridges
        # Check that not out of bounds and no passage on or next to this square
        #if (self.y-4)>=1 and self.matrix[self.x][self.y] not in bridges and self.matrix[self.x-1][self.y] not in bridges and self.matrix[self.x+1][self.y] not in bridges and self.matrix[self.x][self.y+1] not in bridges:
        if (self.y-4)>=1 and self.matrix[self.x][self.y-1] not in bridges and self.matrix[self.x-1][self.y-1] not in bridges and self.matrix[self.x+1][self.y-1] not in bridges and self.matrix[self.x][self.y] not in bridges:
            # Wall north, horizontal passage, wall and empty square
            if self.matrix[self.x][self.y-4]==0:    # Empty square
                if self.matrix[self.x][self.y-1]==1 and self.matrix[self.x][self.y-3]==1:   # Walls
                    if self.matrix[self.x][self.y-2]==0 and (self.matrix[self.x-1][self.y-2]==0 or self.matrix[self.x+1][self.y-2]==0): # Crosses over horizontal passage
                        self.matrix[self.x][self.y-1] = 2     # Sets passage north
                        self.matrix[self.x][self.y-3] = 3   # Sets passage south
                        self.visited[self.x][self.y-1] = 1  # Sets wall as visited
                        self.visited[self.x][self.y-3] = 1  # Sets wall as visited
                        self.bridge_count+=1
                        
        # East-west bridges
        # Check that not out of bounds and no passage on or next to this square
        #if (self.x+4)<=(len(self.matrix)-2) and self.matrix[self.x][self.y] not in bridges and self.matrix[self.x][self.y-1] not in bridges and self.matrix[self.x][self.y+1] not in bridges and self.matrix[self.x-1][self.y] not in bridges:
        if (self.x+4)<=(len(self.matrix)-2) and self.matrix[self.x+1][self.y] not in bridges and self.matrix[self.x+1][self.y-1] not in bridges and self.matrix[self.x+1][self.y+1] not in bridges and self.matrix[self.x][self.y] not in bridges:
            if self.matrix[self.x+4][self.y]==0:    # Empty square
                if self.matrix[self.x+1][self.y]==1 and self.matrix[self.x+3][self.y]==1:   # Walls
                    if self.matrix[self.x+2][self.y]==0 and (self.matrix[self.x+2][self.y-1]==0 or self.matrix[self.x+2][self.y+1]==0): # Crosses over vertical passage
                        self.matrix[self.x+1][self.y] = 4     # Sets passage east
                        self.matrix[self.x+3][self.y] = 5   # Sets passage west
                        self.visited[self.x+1][self.y] = 1  # Sets wall as visited
                        self.visited[self.x+3][self.y] = 1  # Sets wall as visited
                        self.bridge_count+=1
                
                
                
                
    def solve(self, coordinates):
        '''
        Solves the maze, beginning from the coordinates the player is located at.
        'coordinates' is a list of length 2 with the current x-coordinate
        at index 0 and the current y-coordinate at index 1.
        Solves the maze by following the wall on the left hand side.
        Always turns left if it is possible. Second choice is going straight.
        Third choice turning right. Not possible to go back, but will pop an element
        from the list if at a dead-end.
        '''

        matrix_copy = self.matrix
        x_intersect = [] # Stack containing the x-coordinates
        y_intersect = [] # Stack containing the y-coordinates
        forbidden_list = [1, 2, 3, 4, 5, 9]
        directions = []
        moving_counter = 0  # Counter used in retracking
        moving_dir = 0   # Current moving direction
        #TODO: Change the initial moving_dir
        x = coordinates[0]
        y = coordinates[1]
        while matrix_copy[x][y]!=7: # While not at the end. This loop appends the possible moving directions to the list 'directions'.
            if matrix_copy[x][y-1] not in forbidden_list:
                directions.append(0)    # North
            if matrix_copy[x+1][y] not in forbidden_list:
                directions.append(1)    # East
            if matrix_copy[x][y+1] not in forbidden_list:
                directions.append(2)    # South
            if matrix_copy[x-1][y] not in forbidden_list:
                directions.append(3)    # West
            matrix_copy[x][y] = 9
            if len(directions)>1:   # Intersection
                x_intersect.append(x)
                y_intersect.append(y)
                '''
                moving_dir = moving_dir%3-1
                while moving_dir not in directions:
                    moving_dir = moving_dir%3+1
                '''
        
                if moving_dir==0: # Previously moved north
                    if matrix_copy[x][y-1]==7:
                        moving_dir = 0
                    elif 3 in directions:
                        moving_dir = 3
                    elif 0 in directions:
                        moving_dir = 0
                    elif 1 in directions:
                        moving_dir = 1
                elif moving_dir==1: # Previously moved east
                    if 0 in directions:
                        moving_dir = 0
                    elif 1 in directions:
                        moving_dir = 1
                    elif 2 in directions:
                        moving_dir = 2
                elif moving_dir==2: # Previously moved south
                    if 1 in directions:
                        moving_dir = 1
                    elif 2 in directions:
                        moving_dir = 2
                    elif 3 in directions:
                        moving_dir = 3
                elif moving_dir==3: # Previously moved west
                    if matrix_copy[x][y-1]==7:
                        moving_dir = 0
                    elif 2 in directions:
                        moving_dir = 2
                    elif 3 in directions:
                        moving_dir = 3
                    elif 0 in directions:
                        moving_dir = 0
                # Updates the x- or y-value
                if moving_dir%2==0:
                    if moving_dir==0:
                        y-=1
                    else:
                        y+=1
                else:
                    if moving_dir==1:
                        x+=1
                    else:
                        x-=1
            elif len(directions)==0 and len(x_intersect):
                #TODO: Add backtracking to remove the marked cells from a dead end
                #matrix_copy[x][y] = 0
                x = x_intersect.pop()
                y = y_intersect.pop()
            elif len(directions)==1:   # One possible direction to move in
                # Updates the x- or y-value
                moving_dir = directions[0]
                if moving_dir==0:
                    y = y-1
                elif moving_dir==1:
                    x = x+1
                elif moving_dir==2:
                    y = y+1
                elif moving_dir==3:
                    x = x-1
            directions = []
        return matrix_copy
        
        
        
    
    
    def to_file(self, file_name):
        '''
        file_name = the file's name without the ending (.txt).
        If the file doesen't exist, a new file with the name 'file_name' is created.
        '''
        file = open(file_name+'.txt', 'w+')
        word = str(self.x_size) + ' ' + str(self.y_size) + '\n'
        file.write(word)
        i = 0
        word = ''
        while i<self.y_size:
            for j in self.matrix:
                word+=str(j[i])
                word+=' '
            if self.y_size-i!=1:    # If not the last line
                word+='\n'
            file.write(word)
            word = ''
            i+=1
        file.close()
    
    
    def from_file(self, file_name):
        '''
        file_name = the file's name without the ending (.txt).
        Returns True at a successful load and False if something went wrong.
        '''
        
        try:
            file = open(file_name+'.txt', 'r')
            line = file.readline()
            line = line.rstrip()
            line = line.split(' ')
            self.x_size = int(line[0])
            self.y_size = int(line[1])
            self.matrix = list(list(0 for i in range(self.y_size)) for j in range(self.x_size))
            
            j = 0
            z = 1
            while z<=self.y_size:
                line = file.readline()
                line = line.rstrip()
                line = line.split(' ')
                k = 0
                while k<self.x_size:
                    self.matrix[k][j] = int(line[k])
                    k+=1
                j+=1
                z+=1
            file.close()
            
            return True
        
        except:
            return False
    
    
    