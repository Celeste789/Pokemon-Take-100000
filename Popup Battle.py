# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 21:02:51 2025

@author: Celeste
"""

import tkinter as tk

from GameRound import *

screen = tk.Tk()
screen.geometry("400x400")
screen.title("Pokemon Battle")

game_round = GameRound(trainer1, trainer2)
trainer1_frame_class = game_round.trainer1_game
trainer2_frame_class = game_round.trainer2_game


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

        lbl_acknowledgment = tk.Label(self, text="Thanks to Carpincho Feliz")
        lbl_acknowledgment.pack()


class PickAPokemonScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl_title = tk.Label(self, text="Time to pick your pokemons", font=("Arial", 14))
        lbl_title.grid(row=0, column=0, columnspan=5, pady=10)

        left_frame = tk.Frame(self)
        right_frame = tk.Frame(self)
        left_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        right_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

        lbl_trainer1 = tk.Label(left_frame, text="Trainer 1's Pokémon:")
        lbl_trainer1.grid()

        trainer_team1 = game_round.trainer1_game.trainer_team
        pokemon1_var = tk.StringVar(None, " ")

        for name, pokemon in trainer_team1.items():
            btn_pokemon1 = tk.Radiobutton(
                master=left_frame,
                text=name,
                variable=pokemon1_var,
                value=name,
                command=lambda: game_round.selected_pokemon1_setter(pokemon1_var.get())
            )
            if not pokemon.pokemon_status:
                btn_pokemon1.configure(state=tk.DISABLED)
            btn_pokemon1.grid()

        lbl_trainer2 = tk.Label(right_frame, text="Trainer 2's Pokémon:")
        lbl_trainer2.grid()

        trainer_team2 = game_round.trainer2_game.trainer_team
        pokemon2_var = tk.StringVar(None, " ")

        for name, pokemon in trainer_team2.items():
            btn_pokemon2 = tk.Radiobutton(
                master=right_frame,
                text=name,
                variable=pokemon2_var,
                value=name,
                command=lambda: game_round.selected_pokemon2_setter(pokemon2_var.get())
            )
            if not pokemon.pokemon_status:
                btn_pokemon2.configure(state=tk.DISABLED)
            btn_pokemon2.grid()

        btn_continue = tk.Button(self, text="Continue", command=lambda: controller.change(PickAnAction))
        btn_continue.grid(row=4, column=0, columnspan=5, pady=10)

        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(WelcomeScreen))
        btn_back.grid(row=5, column=0, columnspan=5, pady=10)

        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.grid(row=6, column=0, columnspan=5, pady=10)


class PickAnAction(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        btn_stats = tk.Button(self, text=f"Show stats",
                              command=lambda: controller.change(ShowStats))
        btn_stats.pack()

        btn_move = tk.Button(self, text=f"Pick a move",
                             command=lambda: controller.change(PickAMoveScreen))
        btn_move.pack()

        # btn_potion = tk.Button(self, text="Quit", command=screen.destroy)
        # btn_potion.grid(row=6, column=0, columnspan=5, pady=10)

        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(PickAPokemonScreen))
        btn_back.pack()

        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()


class ShowStats(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl_hp1 = tk.Label(self,
                           text=f"{game_round.selected_pokemon1.pokemon_name}'s HP is {game_round.selected_pokemon1.pokemon_hp}")
        lbl_hp1.pack()

        lbl_hp2 = tk.Label(self,
                           text=f"{game_round.selected_pokemon2.pokemon_name}'s HP is {game_round.selected_pokemon2.pokemon_hp}")
        lbl_hp2.pack()

        lbl_title1 = tk.Label(self, text=f"{game_round.selected_pokemon1.pokemon_name} stats are")
        lbl_title1.pack()

        for stat_name, stat_value in game_round.selected_pokemon1.pokemon_stats.items():
            lbl_stat = tk.Label(self, text=f"{stat_name}: {stat_value}")
            lbl_stat.pack()

        lbl_title2 = tk.Label(self, text=f"{game_round.selected_pokemon2.pokemon_name} stats are")
        lbl_title2.pack()

        for stat_name, stat_value in game_round.selected_pokemon2.pokemon_stats.items():
            lbl_stat = tk.Label(self, text=f"{stat_name}: {stat_value}")
            lbl_stat.pack()

        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(PickAnAction))
        btn_back.pack()

        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()


class PickAMoveScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl_title = tk.Label(self, text="Time to pick your moves", font=("Arial", 14))
        lbl_title.grid(row=0, column=0, columnspan=5, pady=10)

        left_frame = tk.Frame(self)
        right_frame = tk.Frame(self)
        left_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        right_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

        lbl_pokemon1 = tk.Label(left_frame, text=f"{game_round.selected_pokemon1.pokemon_name}'s moves")
        lbl_pokemon1.grid(sticky="w", pady=5)

        move1_var = tk.StringVar(None, " ")

        for name, move in game_round.selected_pokemon1.pokemon_moves.items():
            btn_move1 = tk.Radiobutton(
                master=left_frame,
                text=name,
                variable=move1_var,
                value=name,
                command=lambda: game_round.selected_move1_setter(move1_var.get())
            )
            btn_move1.grid(sticky="W")

        lbl_pokemon2 = tk.Label(left_frame, text=f"{game_round.selected_pokemon2.pokemon_name}'s moves")
        lbl_pokemon2.grid(sticky="w", pady=5)

        move2_var = tk.StringVar(None, " ")

        for name, move in game_round.selected_pokemon2.pokemon_moves.items():
            btn_move2 = tk.Radiobutton(
                master=left_frame,
                text=name,
                variable=move2_var,
                value=name,
                command=lambda: game_round.selected_move2_setter(move2_var.get())
            )
            btn_move2.grid(sticky="W")

        btn_continue = tk.Button(self, text="Continue", command=lambda: controller.change(DamageScreen))
        btn_continue.grid(row=4, column=0, columnspan=5, pady=10)

        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(PickAnAction))
        btn_back.grid(row=5, column=0, columnspan=5, pady=10)

        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.grid(row=6, column=0, columnspan=5, pady=10)


class DamageScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        if not game_round.battle():

            lbl_damage1 = tk.Label(self,
                                   text=f"{game_round.selected_pokemon1.pokemon_name}'s HP is {game_round.selected_pokemon1.pokemon_hp}")
            lbl_damage1.pack()

            lbl_damage2 = tk.Label(self,
                                   text=f"{game_round.selected_pokemon2.pokemon_name}'s HP is {game_round.selected_pokemon2.pokemon_hp}")
            lbl_damage2.pack()

            btn_change_pokemon = tk.Button(self, text="Change Pokemon",
                                           command=lambda: controller.change(PickAPokemonScreen))
            btn_change_pokemon.pack()

            btn_pick_move = tk.Button(self, text="Pick A Move",
                                      command=lambda: controller.change(PickAMoveScreen))
            btn_pick_move.pack()

        else:

            controller.change(EndScreen)

        # btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        # btn_quit.pack()


class EndScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        if (game_round.pokemon_loser or game_round.pokemon_winner) is None:
            lbl_no_winner = tk.Label(self, text=f"Nobody won")
            lbl_no_winner.pack()
        else:
            lbl_fainted = tk.Label(self, text=f"{game_round.pokemon_loser.pokemon_name} fainted")
            lbl_fainted.pack()
            lbl_winner = tk.Label(self, text=f"{game_round.pokemon_winner.pokemon_name} won")
            lbl_winner.pack()

        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()

        btn_back = tk.Button(self, text="Back", command=controller.change(PickAPokemonScreen))
        btn_back.pack()


def main():
    MainScreen(screen)
    screen.mainloop()


main()
