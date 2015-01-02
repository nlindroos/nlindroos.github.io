'''
Created on Aug 30, 2011

@author: santtu
'''

from Tkinter import *
from adventure import Adventure

class Adventure_GUI(object):
    '''
    This class contains a GUI for the Adventure text game project. 
    The GUI reads its input from a text field and displays
    data about the game in uneditable text areas.
    
    @see: src.adventure.ui.adventure_text_UI
    '''

    def __init__(self):
        '''
        Creates a new adventure game frame and starts a new
        adventure from the beginning. Immediately makes the
        frame visible.
        '''
        self.window = Tk()
    
        self.adventure = Adventure()        # fixed value: a session only has one adventure and ends when that one finishes
        self.player = self.adventure.get_player()              # fixed value
    
        self.location_info = Text(self.window, height=7, width=100)
        self.location_info.configure(state=DISABLED)
        Label(self.window, text="Location:", width=10).grid(row=0, column=0)
        self.location_info.grid(row=0, column=1)
    
        self.input = Entry(self.window, width=100)
        Label(self.window, text="Command:", width=10).grid(row=1, column=0)
        self.input.grid(row=1, column=1)
        self.input.bind('<Return>', self.text_entered)
    
        self.turn_output = Text(self.window, height=7, width=100)
        self.turn_output.configure(state=DISABLED)
        Label(self.window, text="Events:", width=10).grid(row=2, column=0)
        self.turn_output.grid(row=2, column=1)
    
        self.turn_counter = Label(self.window)
        self.turn_counter.grid(row=3, column=0, rowspan=2, columnspan=1)
    
        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Quit", command=self.window.quit)
        menubar.add_cascade(label="Program", menu=filemenu)
        self.window.config(menu=menubar)
    
        self.window.title(self.adventure.get_name())
        self.window.configure(background='lightgray')
        self.update_info(self.adventure.get_welcome())
    
        self.window.mainloop()


    def text_entered(self, event):
        '''
        Event handler method: reacts (assuming the game is not over) to 
        the user giving a new command in the command input field.
        Clears the input field and proceeds to execute the given command.
        
        @param event: the field that that received the input
        '''
        if event.widget == self.input and  not self.adventure.is_over():
            command = event.widget.get()
            if len(command) > 0:
                event.widget.delete(0, END)
                self.play_turn(command)
      
    
  



    def play_turn(self, command):
        '''
        Lets the player play a turn by executing the
        given command. If the player wants to quit,
        exits the application. Otherwise, updates
        the GUI with the game's new status after the
        player's turn.
        
        @param command: a command to execute, e.g. "go north", "quit"
        '''
        turn_report = self.adventure.play_turn(command)
        if self.player.has_quit():
            self.window.quit()
        
        self.update_info(turn_report)
  


    def update_info(self, turn_report): 
        '''
        Updates the GUI with the current game status data.
        
        @param turn_report: a report of the player's latest turn
        '''
        if not self.adventure.is_over():
            self.turn_output.configure(state=NORMAL)
            self.turn_output.delete(1.0, END)
            self.turn_output.insert(END, turn_report)
            self.turn_output.configure(state=DISABLED)
        else:
            self.turn_output.configure(state=NORMAL)
            self.turn_output.delete(1.0, END)
            self.turn_output.insert(END, turn_report + "\n\n" + self.adventure.get_goodbye())
            self.turn_output.configure(state=DISABLED)
        
        self.location_info.configure(state=NORMAL)
        self.location_info.delete(1.0, END) 
        self.location_info.insert(END, self.player.get_location().get_full_description())
        self.location_info.configure(state=DISABLED)
        
        self.turn_counter.configure(text="Turns played: " + str(self.adventure.get_turn_count()))



if __name__ == '__main__':
    '''
    Creates a user interface frame onscreen.
    '''
    Adventure_GUI()
  




