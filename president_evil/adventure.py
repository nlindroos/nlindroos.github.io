#!/usr/bin/python
# -*- coding: utf-8 -*-
from area import Area
from item import Item
from player import Player
from action import Action
from enemy import Enemy
  
class Adventure(object):
    '''
    The class C{Adventure} represents text adventure games.
    An adventure consists of a player, enemies, items and a number of areas that make
    up the game world. It provides methods for playing the game one
    turn at a time and for checking the state of the game.
    '''
   
    def __init__(self):
        '''
        Sets up a new "President Evil" game.'''
        
        
        self.key = Item("key", "A moderately sized key from the manufacturer 'Abloy'.")
        self.mark_pouch = Item("mark pouch", "A pouch which contains old marks and pennies.")
        self.detonator = Item("detonator", "Small object. But terribly destructive in the wrong hands.")
        self.explosives = Item("C4-explosives", "A neat package of EXPLOSIVES!")
        self.minaret_blueprint = Item("minaret blueprint", "Seems like a blueprint for some religious building. \n" \
                                      "I wonder where it is intended for. Disastrous things could \n" \
                                      "happen if the True Finns got their hands on this.")
        self.lotion_bottle = Item("full lotion bottle", "Not very useful in your current situation. \nIt may come in handy once you have made yourself home, so you store it in your pocket.")
        self.bomb = Item("bomb", "A homemade bomb. It's deadly.")
        self.cam = Item("video camera", "While searching through the room for food, you happen to find a video camera that has recorded the events from last night. \nTo your horror you see a video of the True Finn party members raving in the Assembly Hall. \nYou realize that the True Finns must have stages a coup d'etat and are now in control of the parliament. \nYou must escape, for the future of Finland!")
        self.map = Item("map of Karjala", "A map of a former Finnish province.")
        
        self.truefinn1 = Enemy("True Finn Party Member 1", "One of Timo Soini's loyal acolytes. He will go to any lengths to stop you.", "mark pouch")
        self.truefinn2 = Enemy("True Finn Party Member 2", "One of Timo Soini's loyal acolytes. He will go to any lengths to stop you.", "map of Karjala")
        self.teuvo = Enemy("Teuvo Hakkarainen", "Timo Soini's deadliest lieutenant. He will let you escape only over his dead body.", "minaret blueprint")
        self.timo = Enemy("Timo Soini", "Sitting on his throne is the Big Boss of the True Finns. Your knees shudder with fear. How can you get past something so monstruous?!", "bomb")
        
        office3 = Area("Prime Minister's office", "You wake up in the current Prime Minister's office after a wild presidential debate \nthat went on late into the night. A deafening roar echoes through the room \nand you realize that the roar originated from your stomach. Maybe the lunch room \nto the south still has some munchies left for you to ease your hunger with.\n\nWith the command 'help' you can get a list of all possible commands.")
        self.west3 = Area("Side Chamber", "A side chamber for the lunch room is before you. Leftovers from some kind of a party litter the room.")
        self.lunchroom3 = Area("Lunchroom", "You enter the common lunch room. Scattered remnants of food can be seen all over the place \nbut your favorite doughnuts are nowhere to be seen. An eerie silence creeps through the unusually empty room.")
        self.east3 = Area("3rd Floor Corridor", "You enter a corridor with doors leading to offices, the utility closet and towards the staircase.")
        southeast3 = Area("3rd Floor Lobby", "You enter a small 3rd floor lobby.")
        self.deto3 = Area("Janitor's Closet", "You step inside the utility closet. Covering the walls are shelves filled with the janitor's tools.")
        self.west2 = Area("West Wing Office", u"You enter an office on the west wing of the House of Parliament. On the floor you can see traces of blood which seem to form up a sentence made of shaky letters: 'Kyllä kansa tietää'.")
        self.middle2 = Area("2nd Floor Main Lobby", "You enter the main lobby of the 2nd floor.")
        east2 = Area("2nd Floor East Lobby", "You enter a small 2nd floor lobby.")
        self.soini1 = Area("Entrance Hall", "You finally find the entrance hall. You can almost smell freedom, were it not the tingling feeling of someone watching you.")
        middle1 = Area("Main Lobby", "You enter the main lobby of the 1st floor. There are holes in the form of \nfootprints on the floor, leading towards west. Something huge must have passed by here recently.")
        east1 = Area("Cloakroom", "To the east from the main lobby you find yourself in the cloakroom.")
        south1 = Area("Men's Bathroom", "A standard men's bathroom. Vomit all over the place. Just disgusting..")
        self.teuvo1 = Area("Shady Corridor", "A shadowy corridor smelling of alcohol looms before you. \nThe wall is filled with pictures of immigrants. Somebody has been throwing darts at the pictures.")
        southeast1 = Area("Southeast1", "You find a crammed meeting room filled with chairs. \nSome kind of a meeting must have been staged here. \nA map of Finland hangs on the wall with strategic arrows painted all over it.")
        self.end1 = Area("", "")
        office3.add_exit("south", self.lunchroom3)
        self.west3.add_exit("east", self.lunchroom3)
        self.east3.add_exit("west", self.lunchroom3)
        self.east3.add_exit("east", southeast3)
        self.east3.add_exit("south", self.deto3)
        southeast3.add_exit("north", self.east3)
        southeast3.add_exit("west", self.deto3)
        southeast3.add_exit("downstairs", east2)
        self.deto3.add_exit("north", self.east3)
        self.deto3.add_exit("east", southeast3)
        self.west2.add_exit("east", self.middle2)
        self.middle2.add_exit("upstairs", self.lunchroom3)
        self.middle2.add_exit("west", self.west2)
        self.middle2.add_exit("east", east2)
        self.middle2.add_exit("downstairs", middle1)
        east2.add_exit("upstairs", southeast3)
        east2.add_exit("west", self.middle2)
        self.soini1.add_exit("east", middle1)
        middle1.add_exit("upstairs", self.middle2)
        middle1.add_exit("west", self.soini1)
        middle1.add_exit("east", east1)
        middle1.add_exit("south", south1)
        east1.add_exit("west", middle1)
        east1.add_exit("east", southeast1)
        east1.add_exit("south", self.teuvo1)
        south1.add_exit("north", middle1)
        south1.add_exit("east", self.teuvo1)
        self.teuvo1.add_exit("north", east1)
        self.teuvo1.add_exit("west", south1)
        self.teuvo1.add_exit("east", southeast1)
        southeast1.add_exit("north", east1)
        southeast1.add_exit("west", self.teuvo1)
        
        
        self.soini1.add_enemy(self.timo)
        self.teuvo1.add_enemy(self.teuvo)
        self.deto3.add_enemy(self.truefinn2)
        self.west2.add_enemy(self.truefinn1)
        
        
        self.west3.add_item(self.map)
        east2.add_item(self.minaret_blueprint)
        southeast1.add_item(self.lotion_bottle)
        self.east3.add_item(self.mark_pouch)
        self.lunchroom3.add_item(self.cam)
        
        self.chosen_character = ''
        
        self.turn_count = 0        # stepper
        self.time_limit = 200        # fixed value
        self.destination = self.end1
        
        self.plot_location = self.lunchroom3
        self.enemy_locations = [self.deto3, self.west2, self.soini1, self.teuvo1]
        
        self.player = Player(office3, self.enemy_locations)
        
        
   
    def get_name(self):
        '''
        Returns the name (or title) of the adventure game.
          
        @return: the name of the game
        '''
        return "President Evil"
    
    
   
    def get_player(self):
        '''
        Returns an object representing the player character that the
        user controls.
          
        @return: player
        '''
        return self.player
    
   
    def get_turn_count(self):
        '''
        Returns the number of turns the adventure has lasted so far.
          
        @return: turn count
        '''
        return self.turn_count
    
   
   
    def play_turn(self, command):
        '''
        Plays one turn of the adventure game. This involves the
        player character executing the given command - indeed, that
        is the only thing that happens during a turn of the basic forest
        adventure game. Some more elaborate adventure games could
        have other creatures move or act after the player, or could
        feature other world events independent of the player's actions.
          
        Playing a turn advances the turn count of the adventure by one
        (though giving a command that the game does not understand does
        not count as a turn).
          
        @param command: the command given by the user to make the player character act
        @return: a "turn report" of what occurred this turn
        '''
        action = Action(command) 
        location = self.get_player().get_location()
        if command == 'examine video camera' and location == self.lunchroom3:
            location.add_exit("west", self.west3)
            location.add_exit("east", self.east3)
            location.add_exit("downstairs", self.middle2)
        turn_report = action.execute(self.player)
        if self.get_player().check_used_items():
            self.get_player().killed_enemy()
        if self.turn_count < 5:
            self.pro_tip()
        if self.turn_count == 20:
            print "Do u feel stuck and can't get further? Try the command 'help' \nand try to search new areas."
        if turn_report != None:
            self.turn_count += 1
            return turn_report
        else:
            return "I don't understand the command \"" + command + "\"."
        
    def pro_tip(self):
        '''
        Prints an important tip for new beginners.
        '''
        if self.player.get_location() == self.plot_location:
            print  "\nIMPORTANT: You should make a more thorough search in the Lunchroom with the command 'search' and examine any items you find!\n\n"
        
      
  
   
    def is_complete(self):
        '''
        Determines if the adventure is complete, i.e., if the player
        has won.
          
        @return: a boolean value indicating if the adventure is complete
        '''
        return self.player.get_location() == self.get_player().destination
    
   
   
    def is_over(self):
        '''
        Determines if the adventure is over.
          
        @return: a boolean value indicating if the game has come to an end
        '''
        return self.is_complete() or self.turn_count == self.time_limit or self.player.has_quit()
    
   
   
    def get_welcome(self):
        '''
        Prints the text to be displayed to the user at the beginning of the game.
        Stores the character name the player chooses.
        Returns the chosen character.
        '''
        print 'Welcome to "President Evil". Please choose your character to begin this adventure. You can choose between:'
        self.chosen_character = self.player.choose_character()
        return self.chosen_character
       
   
    def get_goodbye(self):
        '''
        Returns the text to be displayed to the user at the end of the game.
        The text will vary depending on whether or not the player has completed
        the quest.
          
        @return: goodbye text
        @see: #is_over()
        '''
        if self.is_complete():
            return "Finally free! Good job " + self.chosen_character + "!\nNow you must find your followers and strike back! But that will be another adventure... \nCongratulations on finishing the game!"
        elif self.turn_count == self.time_limit:
            return "Oh no! Time's up. Your home country is doomed! :( \n" + \
            "Game over!"
        else: # game over due to player quitting
            return "Lame choice, friend! Your home country is disappoint."
        