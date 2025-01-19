# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 21:02:51 2025

@author: Celeste
"""

import tkinter as tk

import Specie
from Pokemon import *
from Type import *
from Move import *
from Trainer import *
from Battle import *

screen = tk.Tk()
screen.geometry("400x400")
screen.title("Pokemon Battle")

class MainScreen:
    def __init__(self, master):
        self.master = master
        self.frame = WelcomeScreen(self)  
        self.frame.pack()
        
    def change(self, frame):
        self.frame.pack_forget()  # Remove the current frame
        self.frame = frame(self)  # Create the new frame
        self.frame.pack()

class WelcomeScreen(tk.Frame):
    def __init__(self, controller):  # controller is the MainScreen instance
        super().__init__(controller.master)
        lbl_title = tk.Label(self, text="Welcome to the pokemon battle")
        lbl_title.pack()
        
        lbl_trainer1 = tk.Label(self, text=list(trainer.team.keys))
        
        # Use the controller to switch frames
        btn_begin = tk.Button(self, text="Begin", command=lambda: controller.change(PickAPokemonScreen))
        btn_begin.pack()
        
        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()
        
        

class PickAPokemonScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl = tk.Label(self, text="Now, pick your pokemon!")
        lbl.pack()

        # Add a button to go back to the WelcomeScreen
        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(WelcomeScreen))
        btn_back.pack()
        
        btn_continue = tk.Button(self, text="Continue", command=lambda: controller.change(PickAMoveScreen))
        btn_continue.pack()
        
        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()
        
class PickAMoveScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl = tk.Label(self, text="Now, pick your move!")
        lbl.pack()

        # Add a button to go back to the WelcomeScreen 
        btn = tk.Button(self, text="Back", command=lambda: controller.change(PickAPokemonScreen))
        btn.pack()
        
        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()
        

class DamageScreen(tk.Frame):
    pass

class FaintedScreen(tk.Frame):
    pass

class WinnerScreen(tk.Frame):
    pass



def main():
    app = MainScreen(screen)
    screen.mainloop()

main()