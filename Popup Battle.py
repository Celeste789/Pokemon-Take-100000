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
from Game import *

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
        
        self.lbl_trainer1 = tk.Label(self, text="These are trainer1's pokemons: ")
        self.lbl_trainer1.pack()
        
        trainer_team1 = game.trainer1.trainer_team
        pokemon1_var = tk.StringVar()
        
        for name, pokemon in trainer_team1.items():
            btn_pokemon1 = tk.Radiobutton( 
               #master=controller,
                text=name,
                variable = pokemon1_var,
                value = pokemon,
                command = self.select_pokemon(game.trainer1, pokemon)
            )
            btn_pokemon1.pack()

                    
        self.lbl_trainer2 = tk.Label(self, text="These are trainer2's pokemons: ")
        self.lbl_trainer2.pack()
        
                
        
        trainer_team2 = game.trainer2.trainer_team
        pokemon2_var = tk.StringVar()

        for name, pokemon in trainer_team2.items():
            btn_pokemon2 = tk.Radiobutton(
                #master=controller,
                text=name,
                variable = pokemon2_var,
                value = pokemon,
                command=self.select_pokemon(game.trainer2, pokemon)
            )
            btn_pokemon2.pack()
            
        #game.selected_pokemon1 = trainer_team1.get(pokemon2_var)
                  
        lbl_qandb = tk.Label(self, text="Back and Quit Buttons")
        lbl_qandb.pack()
        
        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(WelcomeScreen))
        btn_back.pack()
        
        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()

    def select_pokemon(self, trainer, pokemon):
        if trainer == game.trainer1:
            game.selected_pokemon1 = pokemon
        else:
            game.selected_pokemon2 = pokemon

class PickAMoveScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl = tk.Label(self, text=f"Now, pick a move for {selected_pokemon.pokemon_name}!")
        lbl.pack()
        
        dict_moves = {move.move_name: move for move in selected_pokemon.pokemon_moves}       
            
        for name, move in dict_moves.items():
            btn_move = tk.Button(
                self,
                text=name,
                command=lambda m=move, x=controller, p=selected_pokemon: self.select_move(x, m, p)
            ) 
            btn_move.pack()
            
        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(PickAPokemonScreen))
        btn_back.pack()
        
        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()
        
    def select_move(self, controller, move, pokemon):
        controller.selected_move = move
        controller.select_pokemon = pokemon
        controller.change(lambda x=controller: DamageScreen(x,pokemon,move))

class DamageScreen(tk.Frame):
    def __init__(self, controller, selected_pokemon, selected_move):
        super().__init__(controller.master)
        controller.master.geometry("600x400")
        
        

class FaintedScreen(tk.Frame):
    pass

class WinnerScreen(tk.Frame):
    pass



def main():
    app = MainScreen(screen)
    screen.mainloop()

main()