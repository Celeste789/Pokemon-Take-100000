# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:23:28 2025

@author: Celeste
"""

import tkinter as tk

    #as far as i understand, you make a class for each frame and the update :shrug:
class MainPopupBattle:
    
    def __init__(self):
        
        screen = WelcomeFrame() 
        
        screen.title("Welcome to the Pokemon Battle")
        screen.geometry("400x400")
    
        
        self.label.pack()
        self.button.pack()
        self.screeen.pack()
        
        
    # def change(self):
    #     self.screen.pack_forget() # delete currrent frame
    #     self.screeen = tk.Tk()
    #     self.screen.pack() # make new frame
    
    
    


class WelcomeFrame:
    def __init__(self):
        frame1 = tk.Frame()
        
        self.frame1 = frame1
        self.label = tk.Label(frame1, text="Welcome to the Pokemon Battle")
        self.button = tk.Button(frame1, command=None, text="Begin", fg='Black')
    
    
#     def __init__(self, screen):
        
#         screen.title("Battle")
#         self.label = tk.Label(screen, text="Welcome to the Pokemon Battle")
#         self.button = tk.Button(screen, command=self.change(screen), text="Begin", fg='Black')
        
#         self.label.pack()
#         self.button.pack()
        
#     def change(self, screen):
#         screen.quit()
#         new_screen = tk.Tk()
#         new_screen.mainloop()


# def main():
#     screen = tk.Tk()
#     PopupBattle(screen)
#     screen.mainloop()
        
# main()        
        




# screen = tk.Tk()
# screen.geometry("400x400")
# screen.title('Begin Battle')
# button = tk.Button(screen, text='Beggin', width=25, command=self.change())
# button.pack()
# screen.mainloop()


# def change(self):
#     self.label.pack_forget()

def main():
    screen = tk.Tk()
    MainPopupBattle()
    screen.mainloop()
    
main()

