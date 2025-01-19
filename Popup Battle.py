# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 21:02:51 2025

@author: Celeste
"""

import tkinter as tk

from Specie import Specie
from Pokemon import Pokemon
from Type import Type
from Move import Move
from Trainer import Trainer
from Battle import *

screen = tk.Tk()
screen.geometry("400x400")
screen.title("Pokemon Battle")

class MainScreen:
    def __init__(self, master):
        self.master = master
        self.frame = WelcomeScreen(self)  
        self.frame.pack()
        
        self.selected_pokemon = None
        self.selected_move = None
        
    def change(self, frame):
        self.frame.pack_forget()  # Remove the current frame
        self.frame = frame(self)  # Create the new frame
        self.frame.pack()

class WelcomeScreen(tk.Frame):
    def __init__(self, controller):  # controller is the MainScreen instance
        super().__init__(controller.master)
        lbl_title = tk.Label(self, text="Welcome to the pokemon battle")
        lbl_title.pack()
        
        
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
        
        lbl_trainer1 = tk.Label(self, text="This are trainer1's pokemons: ")
        lbl_trainer1.pack()
        
        v = tk.StringVar()
        trainer_team = trainer1.trainer_team

        for name, pokemon in trainer_team.items():
            btn_pokemon = tk.Button(self, text=name, command=lambda p=pokemon: self.select_pokemon(controller, p))
            btn_pokemon.pack()
                  

        # Add a button to go back to the WelcomeScreen
        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(WelcomeScreen))
        btn_back.pack()
        
        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()
        
    def select_pokemon(self, controller, pokemon):
        controller.selected_pokemon = pokemon
        controller.change(PickAMoveScreen(selected_pokemon=pokemon, controller=controller)) 

        
class PickAMoveScreen(tk.Frame):
    def __init__(self, controller, selected_pokemon):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl = tk.Label(self, text=f"Now, pick a move for {selected_pokemon.pokemon_name}!")
        lbl.pack()
        
        v = tk.StringVar()
        dict_moves = {}
        
        for move in selected_pokemon.pokemon_moves:
            tuple_name_move = (move.move_name, move)
            dict_moves.update(tuple_name_move)
            
        for name, move in dict_moves,items():
            btn_move = tk.Button(self, text=name, command=lambda m=move: self.select_move(controller, m))
            btn_move.pack()
                    
            # btn_pokemon = tk.Button(self, text=name, command=lambda p=pokemon: self.select_pokemon(controller, p))
            # btn_pokemon.pack()

        # Add a button to go back to the WelcomeScreen 
        btn = tk.Button(self, text="Back", command=lambda: controller.change(PickAPokemonScreen))
        btn.pack()
        
        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()
    
    def select_move(self, controller, move):
        controller.selected_move = move
        controller.change(DamageScreen)
    
        

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