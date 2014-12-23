#!/usr/bin/python
# -*- coding: utf-8 -*-
from item import *
  
class Area(object):
    '''
    The class C{Area} represents locations in a
    text adventure game world. A game world consists of
    areas. In general, an area can be pretty much anything:
    a room, a building, an acre of forest, or something
    completely different. What areas have in common is
    that players and items can be located in them and
    that they have exits leading to other, neighboring
    areas. An area also has a name and a description.
    '''
    
    def __init__(self, name, description):
        '''
        Creates a new area with the given name and description.
        The created area has no contents and no exits (yet).
          
        @param name: area name
        @param description: a basic (non-changing) description of the area,
                           not including information about items
        '''
        self.name = name                        # fixed value
        self.description = description                 # fixed value
        self.neighbors = {}
        self.items = {}
        self.enemies = {}
    
   
   
    def get_name(self):
        '''
        Returns the name of the area.
          
        @return: area name
        '''
        return self.name
    
   
   
    def get_full_description(self):
        '''
        Returns a full description of the area as a player sees it.
        The description includes the static, non-changing description
        of the area as set by the constructor, plus a listing of the
        items currently located in the area and an enumeration of the
        available exits.
          
        @return: a description of the area
        '''
        description = self.description            # gatherer        
        #@TODO: fix text if item in area
        #if self.contains():
        #    print 'You see here: '
        if len(self.enemies) > 0:
            enemy_name = self.enemies.keys()[0]
        else:
            enemy_name = ''
        if len(enemy_name) > 0:
            description += '\nYou face enemy: ' + str(enemy_name) + '!'
 
        description += '\n\nPossible directions:'
        for exit in self.neighbors:     # most-recent holder
            description += ' ' + exit
                       
        return description
    
   
   
    def add_exit(self, direction, target_area):
        '''
        Adds an exit from this area to another given area
        (or event the same area, if there is an exit leading
        back to where one started).
          
        @param direction: the direction where one has to move
                         to get from this area to the other area
        @param target_area: another area
        '''
        self.neighbors[direction] = target_area
    

    def remove_exit(self, direction):
        '''
        Removes an exit from this area to another area in
        the given direction.
        '''
        del self.neighbors[direction]
        
   
   
    def get_neighbor(self, direction):
        '''
        Returns the area where one ends up if moving in the given direction
        from this area.
          
        @param direction: a direction (may be nonexistent)
        @return: neighboring area, or C{None} if there is no exit in the given direction
        '''
        return self.neighbors.get(direction, None)
      
      
    def add_item(self, item):
        '''Adds an item to the area.
        Parameters:
        item - the item to be placed'''
        self.items[item.get_name()] = item
        # = self.items.get(item)
        
          
    def display_items(self):
        items_in_room = []
        for item in self.items:
            items_in_room.append(item)
        return items_in_room
      
    def contains(self, item_name):
        '''Determines if the area contains an item of the given name.
        Parameters: item_name - the name of an item in the game (may be nonexistent item)
        Returns: a boolean value indicating of such an item is located here '''
        return item_name in self.items
  
  
    def remove_item(self, item_name):
        '''Removes the item of the given name from the area,
        assuming it was there to begin with.
        Parameters: item_name - the name of an item
        in the game (may be nonexistent item)
        Returns: the removed item, or None if no such item was found '''
        if self.contains(item_name):
            return self.items.pop(item_name)
        else:
            return None
        
        
    def add_enemy(self, enemy):
        '''Adds an enemy to the area.
        Parameters:
        enemy - the enemy to be placed'''
        self.enemies[enemy.get_name()] = enemy
        
    def enemy_alive(self, enemy_name):
        '''Determines if the area contains an enemy of the given name.
        Parameters: enemy_name - the name of an enemy in the game (may be nonexistent enemy)
        Returns: a boolean value indicating of such an item is located here '''
        return enemy_name in self.enemies
    
    def remove_enemy(self, enemy_name):
        '''Removes the enemy of the given name from the area,
        assuming it was there to begin with.
        Parameters: enemy_name - the name of an enemy
        in the game (may be nonexistent enemy)
        Returns: the removed enemy, or None if no such enemy was found '''
        if self.enemy_alive(enemy_name):
            return self.enemies.pop(enemy_name)
        else:
            return None
        
    def enemy_in_area(self):
        if len(self.enemies) > 0:
            return True
        else:
            return False
        
    def display_enemies(self):
        return self.enemies
