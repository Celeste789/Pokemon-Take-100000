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

        lbl_title = tk.Label(self, text="Time to pick your pokemons", font=("Arial", 14))
        lbl_title.grid(row=0, column=0, columnspan=5, pady=10)
        
        left_frame = tk.Frame(self)
        right_frame = tk.Frame(self)
        left_frame.grid(row=1, column=0, padx=10, pady=10)
        right_frame.grid(row=1, column=2, padx=10, pady=10)
        
        self.lbl_trainer1 = tk.Label(master=left_frame, text="These are trainer1's pokemons: ")
        self.lbl_trainer1.grid(row=1, column=0, columnspan=1, padx=10, sticky="W")
        
        
        trainer_team1 = game.trainer1.trainer_team
        pokemon1_var = tk.StringVar(None, "Toto")
        
        for name, pokemon in trainer_team1.items():
            btn_pokemon1 = tk.Radiobutton( 
                master=left_frame,
                text=name,
                variable=pokemon1_var,
                value=pokemon,
                command=lambda: self.select_pokemon(game.trainer1, pokemon)
            )
            btn_pokemon1.grid(sticky="W")

                    
        self.lbl_trainer2 = tk.Label(master=right_frame, text="These are trainer2's pokemons: ")
        self.lbl_trainer2.grid(row=1, column=2, columnspan=1, padx=10, sticky="E")     
                
        trainer_team2 = game.trainer2.trainer_team
        pokemon2_var = tk.StringVar(None, "Chiko")

        for name, pokemon in trainer_team2.items():
            btn_pokemon2 = tk.Radiobutton( 
                master=right_frame,
                text=name,
                variable=pokemon2_var,
                value=pokemon,
                command=lambda: self.select_pokemon(game.trainer2, pokemon)
        )
            btn_pokemon2.grid(sticky="E")
            
        #game.selected_pokemon1 = trainer_team1.get(pokemon2_var)
                  
        lbl_qandb = tk.Label(self, text="Back and Quit Buttons")
        lbl_qandb.grid()
        
        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(WelcomeScreen))
        btn_back.grid()
        
        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.grid()

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