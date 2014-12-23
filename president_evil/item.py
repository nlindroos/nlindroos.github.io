#!/usr/bin/python
# -*- coding: utf-8 -*-
class Item(object):
    '''
    The class C{Item} represents items in
    a text adventure game. Each item has a name and
    a longer description. 
    
    @note: it is assumed (but not enforced by this class)
    that items have unique names. That is, no two items in
    a game world have the same name.
    '''


    def __init__(self, name, description):
        '''
        Creates a new item with the given attributes.
        
        @param name: item name 
        @param description: item description
        '''
        self.name = name               # fixed value
        self.description = description   # fixed value
  

  
    def get_name(self):
        '''
        Returns the name of the item.
        
        @return: item name
        '''
        return self.name
  
  
  
    def get_description(self):
        '''
        Returns the description of the item.
        
        @return: item description
        '''
        return self.description
  
  

