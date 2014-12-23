#!/usr/bin/python
# -*- coding: utf-8 -*-
class Enemy(object):
    
    def __init__(self, name, description, weakness):
        '''
        Creates an enemy with a name, a description and a weakness.
        '''
        self.name = name
        self.description = description
        self.weakness = weakness
        self.alive = True
    
    def get_name(self):
        '''
        Returns the name of the enemy.
        '''
        return self.name
    
    def get_weakness(self):
        '''
        Returns the enemy's weakness.
        '''
        return self.weakness
    
    def is_alive(self):
        '''
        Returns a boolean value indicating if the enemy is alive.
        '''
        return self.alive
    
    def get_description(self):
        '''
        Returns a description of the enemy.
        '''
        return self.description
    
    