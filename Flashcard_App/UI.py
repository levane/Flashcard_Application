#!/usr/bin/python
from tkinter import *

'''
    Window is 600 by 600 and cannot be resized
'''

class Window(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
        self.parent.title("Flashcard Application")
        self.pack(fill=BOTH, expand=1)
        quitButton_x = 550
        quitButton_y = 560
        Window.quitButton(self, quitButton_x, quitButton_y)
        
    def quitButton(self, x_coordinate, y_coordinate):
        quitBut = Button(self, text="Quit",
                         command=self.quit)
        quitBut.place(x=x_coordinate,y=y_coordinate)

'''      
class Button():
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    def quitButton(self):
        quitBut = Button(self, text="Quit",
                         command=close_window())
        quitBut.place(x=self.x_coordinate,y=self.y_coordinate) 
    def close_window(self):
        self.destroy()
class CommandsWin():
    '''

def main():
  
    root = Tk()
    root.geometry("600x600+150+50")
    app = Window(root)
    root.resizable(0,0)
    root.mainloop()  

if __name__ == '__main__':
    main()