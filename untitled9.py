# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 21:02:51 2025

@author: Celeste
"""

import tkinter as tk

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
        lbl = tk.Label(self, text="Welcome to the pokemon battle")
        lbl.pack()
        
        # Use the controller to switch frames
        btn = tk.Button(self, text="Begin", command=lambda: controller.change(PickAPokemonScreen))
        btn.pack()

class PickAPokemonScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl = tk.Label(self, text="Now, pick your pokemon!")
        lbl.pack()

        # Add a button to go back to the WelcomeScreen
        btn = tk.Button(self, text="Back", command=lambda: controller.change(WelcomeScreen))
        btn.pack()

def main():
    app = MainScreen(screen)
    screen.mainloop()

main()