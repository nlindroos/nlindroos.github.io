#!/usr/bin/python
# -*- coding: utf-8 -*-

from President_Evil.adventure import Adventure

class Adventure_text_UI(object):
    '''
    This class contains a fully text-based user interface for the 
    Adventure game project.
    
    @see: ope.adventure.ui.adventure_GUI
    '''

    def __init__(self):
        '''
        Sets up a new user interface and starts a new adventure
        from the beginning.
        '''
        self.adventure = Adventure()        # fixed value: a session only has one adventure and ends when that one finishes
        self.player = self.adventure.get_player()              # fixed value
  

  
    def run(self):
        '''
        Runs the user interface. First, a welcome message
        is displayed. Then the user is repeatedly asked to 
        play a turn until the adventure is over. Finally,
        a goodbye message is printed.
        '''
        print self.adventure.get_welcome()
        while not self.adventure.is_over():
            self.print_area_info()
            self.play_turn()
         
        print "\n" + self.adventure.get_goodbye()
  


    def print_area_info(self):
        '''
        Prints a description of the player's current location.
        '''
        area = self.player.get_location()
        print "\n\n" + area.get_name()
        print '_' * len(area.get_name())
        print area.get_full_description() + "\n"
  

  
    def play_turn(self):
        '''
        Lets the user play a turn: asks for a command,
        executes it, and prints out the consequences.
        '''
        print
        command = raw_input("Command: ")
        turn_report = self.adventure.play_turn(command)
        print turn_report
  
  

    def main(self):
        '''
        Creates a user interface and starts it.
        '''
        ui = Adventure_text_UI()
        ui.run()
  

if __name__ == '__main__':
    game = Adventure_text_UI()
    game.main()
        