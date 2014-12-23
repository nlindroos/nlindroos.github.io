'''
Created on 2.3.2013

@author: Nicke
'''
import sys
from PyQt4 import QtGui, QtCore
from player import Player
from labyrinth import Labyrinth



class Window(QtGui.QMainWindow, QtGui.QWidget):
    
    def __init__(self, x_size, y_size):
        self.ended = 0
        self.changed = 1
        self.x_size = x_size*15+250
        self.y_size = y_size*15+75
        self.qp = QtGui.QPainter()
        self.lab = Labyrinth([x_size, y_size])
        
        if self.lab.matrix[self.lab.x_size/2][self.lab.y_size/2]:
            x = self.lab.x_size/2+1
            y = self.lab.y_size/2
            self.player = Player([x, y])
            self.lab.matrix[self.lab.x_size/2+1][self.lab.y_size/2] = 8
        else:
            x = self.lab.x_size/2
            y = self.lab.y_size/2
            self.player = Player([x, y])
            self.lab.matrix[self.lab.x_size/2][self.lab.y_size/2] = 8
        
        super(Window, self).__init__()
        self.initUI()

        
    def initUI(self):
        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        btn1 = QtGui.QPushButton('New Game', self)
        btn1.setShortcut('Ctrl+N')
        btn1.setToolTip('Generates a new maze.')
        btn1.resize(btn1.sizeHint())
        btn1.move(self.x_size-150, 50)
        btn1.clicked.connect(self.button1Clicked)
        
        btn2 = QtGui.QPushButton('Up', self)
        btn2.setShortcut('Up')
        btn2.setToolTip('<b>Up</b>')
        btn2.resize(btn2.sizeHint())
        btn2.move(self.x_size-150, 115)
        btn2.clicked.connect(self.button2Clicked)
        
        btn3 = QtGui.QPushButton('Down', self)
        btn3.setShortcut('Down')
        btn3.setToolTip('<b>Down</b>')
        btn3.resize(btn3.sizeHint())
        btn3.move(self.x_size-150, 175)
        btn3.clicked.connect(self.button3Clicked)
        
        btn4 = QtGui.QPushButton('Right', self)
        btn4.setShortcut('Right')
        btn4.setToolTip('<b>Right</b>')
        btn4.resize(btn4.sizeHint())
        btn4.move(self.x_size-100, 145)
        btn4.clicked.connect(self.button4Clicked)
        
        btn5 = QtGui.QPushButton('Left', self)
        btn5.setShortcut('Left')
        btn5.setToolTip('<b>Left</b>')
        btn5.resize(btn5.sizeHint())
        btn5.move(self.x_size-200, 145)
        btn5.clicked.connect(self.button5Clicked)
        
        btn6 = QtGui.QPushButton('Resign', self)
        btn6.setShortcut('Ctrl+R')
        btn6.setToolTip('Ends the game and shows the solution.')
        btn6.resize(btn6.sizeHint())
        btn6.move(self.x_size-150, 250)
        btn6.clicked.connect(self.button6Clicked)
        
        btn7 = QtGui.QPushButton('Load', self)
        btn7.setShortcut('Ctrl+L')
        btn7.setToolTip('<b>Loads</b> the game from a file.')
        btn7.resize(btn7.sizeHint())
        btn7.move(self.x_size-200, 325)
        btn7.clicked.connect(self.button7Clicked)
        
        btn8 = QtGui.QPushButton('Save', self)
        btn8.setShortcut('Ctrl+S')
        btn8.setToolTip('<b>Saves</b> the game to a file.')
        btn8.resize(btn8.sizeHint())
        btn8.move(self.x_size-100, 325)
        btn8.clicked.connect(self.button8Clicked)
        
        btn9 = QtGui.QPushButton('Help', self)
        btn9.setShortcut('H')
        btn9.setToolTip('Shows the instructions for the game.')
        btn9.resize(btn9.sizeHint())
        btn9.move(self.x_size-150, 400)
        btn9.clicked.connect(self.button9Clicked)
        
        self.resize(self.x_size, self.y_size)
        #self.center()   # Centers the window on the screen
        #self.setGeometry(200, 200, self.x_size, self.y_size)
        self.setWindowTitle('Labyrinth')
        
        self.show()
        
        
    def paintEvent(self, e):
        '''
        Draws a new maze in the window.
        '''
        if self.ended==0:
            self.qp.begin(self)
            j = 0
            height = 15
            while j<self.lab.y_size:
                width = 15
                height+=15
                for k in self.lab.matrix:
                    if k[j]==1:
                        self.draw_rectangle(width, height, 1)
                    elif k[j]==2:
                        self.draw_rectangle(width, height, 2)
                    elif k[j]==3:
                        self.draw_rectangle(width, height, 3)
                    elif k[j]==4:
                        self.draw_rectangle(width, height, 4)
                    elif k[j]==5:
                        self.draw_rectangle(width, height, 5)
                    elif k[j]==7:
                        self.draw_rectangle(width, height, 7)
                    elif k[j]==8:
                        self.draw_rectangle(width, height, 8)
                    else:
                        self.draw_rectangle(width, height, 10)
                    
                    width+=15
                j+=1
            self.qp.end()
        else:
            self.qp.begin(self)
            j = 0
            height = 15
            while j<((self.y_size-75)/15):
                width = 15
                height+=15
                for k in self.new_lab:
                    if k[j]==1:
                        self.draw_rectangle(width, height, 1)
                    elif k[j]==2:
                        self.draw_rectangle(width, height, 2)
                    elif k[j]==3:
                        self.draw_rectangle(width, height, 3)
                    elif k[j]==4:
                        self.draw_rectangle(width, height, 4)
                    elif k[j]==5:
                        self.draw_rectangle(width, height, 5)
                    elif k[j]==7:
                        self.draw_rectangle(width, height, 7)
                    elif k[j]==8:
                        self.draw_rectangle(width, height, 8)
                    elif k[j]==9:
                        self.draw_rectangle(width, height, 9)
                    else:
                        self.draw_rectangle(width, height, 10)
                    
                    width+=15
                j+=1
            self.qp.end()
            
      
    def draw_rectangle(self, x, y, param):
        if param==1:
            self.qp.setBrush(QtGui.QColor(QtCore.Qt.black))
            self.qp.drawRect(x, y, 15, 15)
        elif param==2 or param==3:
            self.qp.setBrush(QtGui.QColor(QtCore.Qt.yellow))
            self.qp.drawRect(x, y, 15, 15)
        elif param==4 or param==5:
            self.qp.setBrush(QtGui.QColor(QtCore.Qt.cyan))
            self.qp.drawRect(x, y, 15, 15)
        elif param==7:
            self.qp.setBrush(QtGui.QColor(QtCore.Qt.green))
            self.qp.drawRect(x, y, 15, 15)
        elif param==8:
            self.qp.setBrush(QtGui.QColor(QtCore.Qt.blue))
            self.qp.drawRect(x, y, 15, 15)
        elif param==9:
            self.qp.setBrush(QtGui.QColor(QtCore.Qt.green))
            self.qp.drawRect(x, y, 15, 15)
        else:
            self.qp.setBrush(QtGui.QColor(0, 0, 0, 0))
            self.qp.drawRect(x, y, 15, 15)
        
        
        
    def button1Clicked(self):
        '''
        Calls a new generation of a maze.
        '''
        
        x_value, ok = QtGui.QInputDialog.getText(self, 'New game', 
            "Enter the width of the new maze:")
        
        if ok:
            y_value, ok = QtGui.QInputDialog.getText(self, 'New game', 
            "Enter the height of the new maze:")
            try:
                x_size = int(x_value)
                y_size = int(y_value)
                self.statusBar().showMessage("")
                self.lab = Labyrinth([x_size, y_size])
                if self.lab.matrix[self.lab.x_size/2][self.lab.y_size/2]:
                    x = self.lab.x_size/2+1
                    y = self.lab.y_size/2
                    self.player = Player([x, y])
                    self.lab.matrix[self.lab.x_size/2+1][self.lab.y_size/2] = 8
                else:
                    x = self.lab.x_size/2
                    y = self.lab.y_size/2
                    self.player = Player([x, y])
                    self.lab.matrix[self.lab.x_size/2][self.lab.y_size/2] = 8
                self.x_size = self.lab.x_size*15+250
                self.y_size = self.lab.y_size*15+75
                self.ended = 0
                self.resize((x_size*15+250), (y_size*15+75))
                self.update()
            except ValueError:
                self.statusBar().showMessage("One of the values was incorrect.")
        
        
    def button2Clicked(self):
        '''
        Moves up.
        '''
        if not self.player.at_exit() and not self.ended:
            self.changed = 1
            self.player.move(0, self.lab.matrix)
            self.update()
            if self.player.at_exit():
                self.statusBar().showMessage("Game ended.")
        else:
            self.statusBar().showMessage("Game ended.")
        
        
    def button3Clicked(self):
        '''
        Moves down.
        '''
        if not self.player.at_exit() and not self.ended:
            self.changed = 1
            self.player.move(2, self.lab.matrix)
            self.update()
        else:
            self.statusBar().showMessage("Game ended.")
        
        
    def button4Clicked(self):
        '''
        Moves right.
        '''
        if not self.player.at_exit() and not self.ended:
            self.changed = 1
            self.player.move(1, self.lab.matrix)
            self.update()
        else:
            self.statusBar().showMessage("Game ended.")
        
        
    def button5Clicked(self):
        '''
        Moves left.
        '''
        if not self.player.at_exit() and not self.ended:
            self.changed = 1
            self.player.move(3, self.lab.matrix)
            self.update()
        else:
            self.statusBar().showMessage("Game ended.")


    def button6Clicked(self):
        '''
        Ends the game.
        '''
        if not self.ended:
            self.ended = 1
            self.new_lab = self.lab.solve(self.player.get_position())
            self.update()
            self.statusBar().showMessage("Game ended.")
        
        
    def button7Clicked(self):
        '''
        Loads a new game.
        '''
        file_name, ok = QtGui.QInputDialog.getText(self, 'Load maze', 
            "Enter the name of the file to be read without the filename extension (.txt):\ne.g. game1")
        if ok:
            if self.lab.from_file(file_name):
                self.statusBar().showMessage("Load successful.")
                if self.lab.matrix[self.lab.x_size/2][self.lab.y_size/2]:
                    x = self.lab.x_size/2+1
                    y = self.lab.y_size/2
                    self.player = Player([x, y])
                    self.lab.matrix[self.lab.x_size/2+1][self.lab.y_size/2] = 8
                else:
                    x = self.lab.x_size/2
                    y = self.lab.y_size/2
                    self.player = Player([x, y])
                    self.lab.matrix[self.lab.x_size/2][self.lab.y_size/2] = 8
                #self.resize((self.lab.x_size*15+250), (self.lab.y_size*15+75))
                self.x_size = self.lab.x_size*15+250
                self.y_size = self.lab.y_size*15+75
                self.ended = 0
                self.update()
                
            else:
                self.statusBar().showMessage("Load failed.")
        
        
    def button8Clicked(self):
        '''
        Saves the maze.
        '''
        if not self.ended:
            file_name, ok = QtGui.QInputDialog.getText(self, 'Save', 
                "Enter the name of the file to save to without the filename extension (.txt):\ne.g. game1")
            if ok:
                self.changed = 0
                self.lab.to_file(file_name)
                self.statusBar().showMessage("Saved the maze to file " + file_name + ".txt")
        else:   # Game ended
            self.statusBar().showMessage("Unable to save. The game has ended.")
    
    
    def button9Clicked(self):
        '''
        Shows the help window with instructions.
        '''
        QtGui.QMessageBox.question(self, 'Message',
                "Your objective is to steer the blue square (player) to the\ngreen square (end). \
Empty squares are passages and\nfilled squares are walls.\nYellow squares are north-southbridges and \
cyan\nsquares are north-south bridges. The resign button\nshows a path to the end from the current square.", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)


    def center(self):
        '''
        Function for centering the window on the screen.
        '''
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def closeEvent(self, event):
        '''
        Changes the default close event.
        '''
        if self.changed:
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure to quit without saving?", QtGui.QMessageBox.Yes | 
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    
            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore() 
    
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    window = Window(30, 35)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 
    
