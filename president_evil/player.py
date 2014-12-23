#!/usr/bin/python
# -*- coding: UTF-8 -*-
from area import *
import random
import sys
from adventure import *
from item import *
from enemy import *

class Player(object):
    '''
    A C{Player} object represents a player character
    controlled by the real-life program user in a text adventure
    game. A player object knows the player's location, possessions and enemy locations.
    '''
     
    def __init__(self, starting_area, enemy_locations):
        '''
        Creates a new player who is located in the given area
        and has no possessions.
          
        @param starting_area: the initial location of the player
        '''
        self.location = starting_area   # gatherer
        self.has_quitted = False          # one-way flag
        self.carried_items = {}
        self.characters = []
        self.character_list = [u'Sauli Niinistö', 'Eva Biaudet', 'Paavo Lipponen', u'Paavo Väyrynen', u'Paavo Arhinmäki', 'Sari Essayah']
        self.used_items = {}    # key = item name, value = area where the item was last used
        
        
        
        self.key = Item("key", "A moderately sized key from the manufacturer 'Abloy'.")
        self.mark_pouch = Item("mark pouch", "A pouch which contains old marks and pennies.")
        self.detonator = Item("detonator", "Small object. But terribly destructive in the wrong hands.")
        self.explosives = Item("C4-explosives", "A neat package of EXPLOSIVES!")
        self.minaret_blueprint = Item("minaret blueprint", "Seems like a blueprint for some religious building. \n" \
                                      "I wonder where it is intended for. Disastrous things could \n" \
                                      "happen if the True Finns got their hands on this.")
        self.lotion_bottle = Item("full lotion bottle", "Not very useful in your current situation. \nIt may come in handy once you have made yourself home, so you store it in your pocket.")
        self.bomb = Item("bomb", "A homemade bomb. It's deadly.")
        self.cam = Item("video camera", "While searching through the room for food, you happen to find a video camera that has recorded the events from last night. \nTo your horror you see a video of the True Finn party members raving in the Assembly Hall. \nYou realize that the True Finns must have staged a coup d'etat and are now in control of the parliament. \nYou must escape, for the future of Finland!")
        self.map = Item("map of Karjala", "A map of a former Finnish province.")
        
        
        self.truefinn1 = Enemy("True Finn Party Member 1", "One of Timo Soini's loyal acolytes. He will go to any lengths to stop you.", "mark pouch")
        self.truefinn2 = Enemy("True Finn Party Member 2", "One of Timo Soini's loyal acolytes. He will go to any lengths to stop you.", "map of Karjala")
        self.teuvo = Enemy("Teuvo Hakkarainen", "Timo Soini's deadliest lieutenant. He will let you escape only over his dead body.", "minaret blueprint")
        self.timo = Enemy("Timo Soini", "Sitting on his throne is the Big Boss of the True Finns. Your knees shudder with fear. How can you get past something so monstruous?!", "bomb")
        
        
        self.office3 = Area("Prime Minister's office", "You wake up in the current Prime Minister's office after a wild presidential debate \nthat went on late into the night. A deafening roar echoes through the room \nand you realize that the roar originated from your stomach. Maybe the lunch room \nto the south still has some munchies left for you to ease your hunger with.\n\nWith the command 'help' you can get a list of all possible commands.")
        self.west3 = Area("Side Chamber", "A side chamber for the lunch room is before you. Leftovers from some kind of a party litter the room.")
        self.lunchroom3 = Area("Lunchroom", "You enter the common lunch room. Scattered remnants of food can be seen all over the place \nbut your favorite doughnuts are nowhere to be seen. An eerie silence creeps through the unusually empty room. \nIMPORTANT: You should make a more thorough search in the room with the command 'search' and examine any items you find!")
        self.east3 = Area("3rd Floor Corridor", "You enter a corridor with doors leading to offices, the utility closet and towards the staircase.")
        self.southeast3 = Area("3rd Floor Lobby", "You enter a small 3rd floor lobby.")
        self.deto3 = Area("Janitor's Closet", "You step inside the utility closet. Covering the walls are shelves filled with the janitor's tools.")
        self.west2 = Area("West Wing Office", u"You enter an office on the west wing of the House of Parliament. On the floor you can see traces of blood which seem to form up a sentence made of shaky letters: 'Kyllä kansa tietää'.")
        self.middle2 = Area("2nd Floor Main Lobby", "You enter the main lobby of the 2nd floor.")
        self.east2 = Area("2nd Floor East Lobby", "You enter a small 2nd floor lobby.")
        self.soini1 = Area("Entrance Hall", "You finally find the entrance hall. You can almost smell freedom, were it not the tingling feeling of someone watching you. You see that something is blocking the door out.")
        self.middle1 = Area("Main Lobby", "You enter the main lobby of the 1st floor. There are holes in the form of \nfootprints on the floor, leading towards west. Something huge must have passed by here recently.")
        self.east1 = Area("Cloakroom", "To the east from the main lobby you find yourself in the cloakroom.")
        self.south1 = Area("Men's Bathroom", "A standard men's bathroom. Vomit all over the place. Just disgusting..")
        self.teuvo1 = Area("Shady Corridor", "A shadowy corridor smelling of alcohol looms before you. \nThe wall is filled with pictures of immigrants. Somebody has been throwing darts at the pictures.")
        self.southeast1 = Area("self.southeast1", "You find a crammed meeting room filled with chairs. \nSome kind of a meeting must have been staged here. \nA map of Finland hangs on the wall with strategic arrows painted all over it.")
        self.end1 = Area("", "")
        self.office3.add_exit("south", self.lunchroom3)
        self.west3.add_exit("east", self.lunchroom3)
        self.east3.add_exit("west", self.lunchroom3)
        self.east3.add_exit("east", self.southeast3)
        self.east3.add_exit("south", self.deto3)
        self.southeast3.add_exit("north", self.east3)
        self.southeast3.add_exit("west", self.deto3)
        self.southeast3.add_exit("downstairs", self.east2)
        self.deto3.add_exit("north", self.east3)
        self.deto3.add_exit("east", self.southeast3)
        self.west2.add_exit("east", self.middle2)
        self.middle2.add_exit("upstairs", self.lunchroom3)
        self.middle2.add_exit("west", self.west2)
        self.middle2.add_exit("east", self.east2)
        self.middle2.add_exit("downstairs", self.middle1)
        self.east2.add_exit("upstairs", self.southeast3)
        self.east2.add_exit("west", self.middle2)
        self.soini1.add_exit("east", self.middle1)
        self.middle1.add_exit("upstairs", self.middle2)
        self.middle1.add_exit("west", self.soini1)
        self.middle1.add_exit("east", self.east1)
        self.middle1.add_exit("south", self.south1)
        self.east1.add_exit("west", self.middle1)
        self.east1.add_exit("east", self.southeast1)
        self.east1.add_exit("south", self.teuvo1)
        self.south1.add_exit("north", self.middle1)
        self.south1.add_exit("east", self.teuvo1)
        self.teuvo1.add_exit("north", self.east1)
        self.teuvo1.add_exit("west", self.south1)
        self.teuvo1.add_exit("east", self.southeast1)
        self.southeast1.add_exit("north", self.east1)
        self.southeast1.add_exit("west", self.teuvo1)
        
       
        self.west3.add_item(self.map)
        self.east2.add_item(self.minaret_blueprint)
        self.southeast1.add_item(self.lotion_bottle)
        self.east3.add_item(self.mark_pouch)
        self.lunchroom3.add_item(self.cam)
        
        self.destination = self.end1
        self.enemy_locations = enemy_locations
        
        
    def has_quit(self):
        '''
        Determines if the player has indicated a desire to quit
        game.
          
        @return: a boolean value indicating if the player wants to quit the game
        '''
        return self.has_quitted
    
     
     
    def get_location(self):
        '''
        Returns the current location of the player.
          
        @return: player location (type: Area)
        '''
        return self.location
    
     
   
    def go(self, direction):
        '''
        Attempts to move the player in the given direction.
        This is successful if there is an exit from the player's
        current location to the given direction.
          
        @param direction: a direction name (may be nonexistent direction)
        @return: a description of the results of the action
        '''
        destination = self.location.get_neighbor(direction)
        if destination != None:
            self.location = destination
            return 'You go ' + direction + '.'
        else:
            return "You can't go " + direction + '.'
      
    def get(self, item_name):
        '''Tries to pick up the given item. This is successful if the item is located in the player's current location.
        Parameters: item_name - an item name (may be nonexistent item)
        Returns: a description of the results of the action '''
        #
        area = self.get_location()
        if area.contains(item_name):
            self.carried_items[item_name] = area.remove_item(item_name)
            return 'You pick up the ' + item_name + '.'
        else:
            return 'There is no ' + item_name + ' here to pick up. \nRemember that also the item choice is CAPITAL sensitive.'
   
   
    def has(self, item_name):
        '''Determines if the player is carrying the given item.
        Parameters: item_name - the name of an item in the game
        Returns: a boolean value indicating if the player is in possession of the given item '''
        return item_name in self.carried_items
   
    def drop(self, item_name):
        '''Tries to drop the given item. This is successful if the item is currently in the player's possession.
        Parameters: item_name - an item name (may be nonexistent item)
        Returns: a description of the results of the action '''
        if self.has(item_name):
            item = self.carried_items.pop(item_name)
            self.get_location().add_item(item)
            return 'You drop the ' + item_name + '.'
        else:
            return "You don't even have that, so pretty stupid to try to drop it, huh??"
          
    def examine(self, item_name):
        '''Causes the player to examine the given item. This is successful if the item is
        currently in the player's possession.
        Parameters: item_name - an item name (may be nonexistent item)
        Returns: a description of the results of the action '''
        #if item_name in self.carried_items
        if self.has(item_name):
            return 'You look closely at the ' + item_name + '.\n' + self.carried_items[item_name].get_description()
        else:
            return 'If you want to examine something, you need to pick it up first.'
          
   
    def make_inventory(self):
        '''Causes the player to list what they are carrying.
        Returns: a listing of the player's possessions or a statement
        indicating that the player is carrying nothing (type: string) '''
        if len(self.carried_items) > 0:
            return 'You are carrying:\n' +  "\n".join(self.carried_items)   
        else:
            return 'You are empty-handed.'
   
     
    def rest(self):
        '''
        Causes the player to rest for a short while (this has no
        real effect in game terms).
          
        @return: a description of the action
        '''
     
        return 'You take a quick break and drink a cup of coffee.'
    
     
     
    def quit(self):
        '''
        Signals that the player wants to quit the game.
        '''
        self.has_quitted = True
    
        
    
    def search(self):
        '''
        Searches an area for items and returns a message if the search produced results.
        '''
        item_amount = self.get_location().display_items()
        description = ''
        for item in item_amount:
            description +=  item + '\n'
        if len(description) > 0:
            return 'Item(s) you find here:\n' + description
        else:
            index = random.randint(1,3)
            if index == 1:
                return 'You search but find nothing.'
            if index == 2:
                return 'Your search leaves you empty-handed.'
            if index == 3:
                return "You search in every corner, but you find nothing."
            
    def inspect(self):
        '''
        Displays a description of the enemy, including it's weakness.
        '''
        location = self.get_location()
        if location.enemy_in_area():
            return location.display_enemies().values()[0].get_description() + "\nThe enemy's weakness is: " + location.display_enemies().values()[0].get_weakness() + '.'
        else:
            return "No enemies in sight."
    
    def use(self, item):
        '''
        Uses an item. Use only works on enemies, more specifically if the used item is the enemy's weakness. 
        Otherwise it does nothing.
        '''
        
        if item == '':
            return 'Please give an item to use.'
        elif item in self.carried_items:
            self.used_items[item] = self.get_location()
            return 'You use the ' + item + '.'
        else:
            index = random.randint(1,2)
            if index == 1:
                return "You don't even have any freakin' " + item + '.'
            if index == 2:
                return "If you don't have an item, you can't possibly use it either.."
    
    def facing_enemy(self):
        '''
        Checks if the player is in the same location as 
        the enemy and if the enemy is alive.
        '''
        location = self.get_location()
        if location in self.enemy_locations:
            if location.enemy_in_area():
                return True
        else:
            return False  
        
    def check_used_items(self):
        '''
        Returns a boolean value of whether the player has used an item.
        '''
        if len(self.used_items.keys()) > 0:
            return True
        else:
            return False
        
        
    def kill_enemy(self):
        '''
        Returns a boolean value indicating if the player has used the item on the enemy
        that is the enemy's weakness. The player must be in the 
        same location as the enemy when he used the item.
        '''
        location = self.get_location()
        enemy = location.display_enemies().values()
        weakness = enemy[0].get_weakness()
        if self.facing_enemy():
            if weakness in self.used_items.keys(): #Checks if the player has used the item that is the enemy's weakness.
                if self.used_items[weakness] == location:  #Checks if the player has used the item in the enemy's location (the player's current location).
                    return True
        else:
            return False    
        
    def killed_enemy(self):
        '''
        When the player has killed the enemy in a location,
        this method adds the location's items and adds exits to the location.
        It also removes the enemies from the location.
        '''
        location = self.get_location()
        enemy = location.display_enemies().values()
        if location.enemy_in_area():
            weakness = enemy[0].get_weakness()
            if self.kill_enemy() == True:
                if weakness == 'mark pouch':
                    location.add_item(self.key)
                    location.remove_enemy(self.truefinn1.get_name())
                    print "You shower the Party Member with old marks and pennies. The Party Member cries hysterically in nostalgic memories and runs off. \nWhile running away, he drops a key!"
                if weakness == 'map of Karjala':
                    location.add_item(self.detonator)
                    location.remove_enemy(self.truefinn2.get_name())
                    print "You throw the map of Karjala at the feet of the Party Member. \nThe Party Member becomes enraged and storms off shouting: 'Karjala takas prkl! \nHe drops a detonator."
                if weakness == 'minaret blueprint':
                    location.add_item(self.explosives)
                    location.remove_enemy(self.teuvo.get_name())
                    print "With a shocked expression on his face when you show him the minaret blueprint, Teuvo Hakkarainen leaves the room to show the blueprint to his boss. \nFrom his backpocket drop some C4-explosives."
                if weakness == 'bomb':
                    location.remove_enemy(self.timo.get_name())
                    location.add_exit("west", self.end1)
                    print "You plant the bomb under Timo Soini's throne and run away. A few seconds later you hear an explosion and return to see that Timo has disintegrated. \nYou are now free to escape!"
        
        
    def used_items(self):
        '''
        Returns the catalogue containing the items used.
        '''
        return self.used_items
        
    
    def choose_character(self):
        '''
        This method lets the player choose a character to play with.
        Returns the character of the player's choice.
        '''
        characters = '\n'
        for character in self.character_list:
            characters += character + '\n'
        print characters
        self.chosen_character = raw_input('Your choice: ').decode(sys.stdin.encoding)
        if self.chosen_character in self.character_list:
            return self.chosen_character
        else:
            print "\nYou can't choose that character. Please make another choice.\nPlease note: The choice is CAPITAL sensitive."
            return self.choose_character()
        
     
    
    def combine(self):
        '''
        Combines the detonator and the C4-explosives into a bomb.
        Returns a string indicating the results.
        '''
        if "detonator" and "C4-explosives" in self.carried_items:
            #self.to_inventory(self.bomb)
            del self.carried_items["detonator"]
            del self.carried_items["C4-explosives"]
            self.carried_items[self.bomb.get_name()] = self.bomb
            return "You managed to create a bomb out of the explosives and the detonator."
        else:
            return "Nothing interesting happens."
   
    
    def help(self):
        '''
        Returns a help text with a list of the possible commands
        and a short explanation of what they do.
        '''
        return '''
        Every turn you are asked to give a command.
        Here is a list of all the possible commands and what they do:
        
        help:
        This help menu will appear.
        
        go + 'direction':
        You choose to go in the given direction. The possible directions are given.
        
        search:
        You search the current room and get a list of what you find.
        
        inspect:
        You look more closely at the enemy in the room.
        If there is no enemy, this command does nothing.
        
        get + 'item':
        You pick up the item.
        
        examine + 'item':
        You examine the item.
        
        use + 'object':
        You try to use the object.
        
        drop + 'item':
        You drop the item.
        
        inventory:
        You get a list of the items you are currently carrying.
        
        combine:
        You combine two items together to create a new item.
        
        rest:
        You take a quick rest.
        
        quit:
        You quit the game.
        
        All item names are CAPITAL sensitive.
        '''
       
    