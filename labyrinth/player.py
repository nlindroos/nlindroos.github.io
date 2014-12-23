'''
Created on 2.3.2013

@author: Nicke
'''


class Player(object):
    
    def __init__(self, start_position):
        
        self.position = [start_position[0], start_position[1]]   # position = [x-value, y-value]
        self.x = self.position[0]
        self.y = self.position[1]
        self.earlier = 0
        self.movable = [False, False, False, False] # North, east, south, west
        self.directions = ['north', 'east', 'south', 'west']
        
    
    
    def move(self, direction, maze):
        '''
        direction: 0 north, 1 east, 2 south, 3 west
        '''
        self.update_movable_directions(maze)
        if self.movable[direction]:   # can move
            if direction==0:
                if maze[self.x][self.y-1]==2:
                    maze[self.x][self.y] = self.earlier
                    self.earlier = maze[self.x][self.y-4]
                    self.position[1]-=4
                    self.y-=4
                    maze[self.x][self.y] = 8
                else:   # maze[self.x][self.y-1]==0
                    maze[self.x][self.y] = self.earlier
                    self.earlier = maze[self.x][self.y-1]
                    self.position[1]-=1
                    self.y-=1
                    maze[self.x][self.y] = 8
            elif direction==1:
                if maze[self.x+1][self.y]==4:
                    maze[self.x][self.y] = self.earlier
                    self.earlier = maze[self.x+4][self.y]
                    self.position[0]+=4
                    self.x+=4
                    maze[self.x][self.y] = 8
                else:
                    maze[self.x][self.y] = self.earlier
                    self.earlier = maze[self.x+1][self.y]
                    self.position[0]+=1
                    self.x+=1
                    maze[self.x][self.y] = 8
            elif direction==2:
                if maze[self.x][self.y+1]==3:
                    maze[self.x][self.y] = self.earlier
                    self.earlier = maze[self.x][self.y+4]
                    self.position[1]+=4
                    self.y+=4
                    maze[self.x][self.y] = 8
                else:
                    maze[self.x][self.y] = self.earlier
                    self.earlier = maze[self.x][self.y+1]
                    self.position[1]+=1
                    self.y+=1
                    maze[self.x][self.y] = 8
            elif direction==3:
                if maze[self.x-1][self.y]==5:
                    maze[self.x][self.y] = self.earlier
                    self.earlier = maze[self.x-4][self.y]
                    self.position[0]-=4
                    self.x-=4
                    maze[self.x][self.y] = 8
                else:
                    maze[self.x][self.y] = self.earlier
                    self.earlier = maze[self.x-1][self.y]
                    self.position[0]-=1
                    self.x-=1
                    maze[self.x][self.y] = 8
            return maze
        else:
            return False
        
    def get_position(self):
        return self.position
    
    def at_exit(self):
        if self.position[1]==0:
            return True
        else:
            return False
    
    def get_movable_directions(self):
        directions = []
        for i in self.movable:
            if i==True:
                directions.append(self.directions[i])
            i+=1
        return directions
    
    
    def update_movable_directions(self, maze):
        '''
        The players' position cannot be on a perimeter tile, unless the player has completed the maze.
        '''
        x = self.position[0]
        y = self.position[1]
        north = maze[x][y-1]
        if north==1 or north ==3 or north==4 or north==5:    # North: x, y-1
            self.movable[0] = False
        else:
            self.movable[0] = True
        east = maze[x+1][y]
        if east==1 or east==2 or east==3 or east==5:    # East: x+1, y
            self.movable[1] = False
        else:
            self.movable[1] = True
        south = maze[x][y+1]
        if south==1 or south==2 or south==4 or south==5:    # South: x, y+1
            self.movable[2] = False
        else:
            self.movable[2] = True
        west = maze[x-1][y]
        if west==1 or west==2 or west==3 or west==4:    # West: x-1, y
            self.movable[3] = False
        else:
            self.movable[3] = True
       
        
            