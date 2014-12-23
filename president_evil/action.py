#!/usr/bin/python
# -*- coding: utf-8 -*-
class Action(object):
    '''
    The class C{Action} represents actions that
    a player make take in a text adventure game.
    Action objects are constructed based on a textual
    commands and are, in effect, parsers for such commands.
    An action object is immutable after creation.
  
    '''
   
     
    def __init__(self, command):
        '''
        Creates a new action object based on the given command.
          
        @param command: a textual game command, e.g. "go east", "rest"
        '''
        command = command.strip().split(' ', 1)       
        self.command_type = command[0]          # fixed value
        if len(command) == 1:
            self.parameters = ''          # fixed value
        else:
            self.parameters = command[1]
        
    
     
     
    def execute(self, actor):
        '''
        Causes the given player to take the action represented
        by this object.
          
        @param actor: a player who is to take action
        @return: a description of the results of the action,
                or C{None} if the command was not known
        '''
        if self.command_type == 'go':
            return actor.go(self.parameters)
        elif self.command_type == 'use':
            return actor.use(self.parameters)
        elif self.command_type == 'search':
            return actor.search()
        elif self.command_type == 'help':
            return actor.help()
        elif self.command_type == 'get':
            return actor.get(self.parameters)
        elif self.command_type == 'drop':
            return actor.drop(self.parameters)
        elif self.command_type == 'examine':
            return actor.examine(self.parameters)
        elif self.command_type == 'inspect':
            return actor.inspect()
        elif self.command_type == 'inventory':
            return actor.make_inventory()
        elif self.command_type == 'combine':
            return actor.combine()
        elif self.command_type == 'rest':
            return actor.rest()
        elif self.command_type == 'quit':
            actor.quit()
            return ''
        else:
            return None
      
