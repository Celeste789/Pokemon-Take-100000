# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 21:02:51 2025

@author: Celeste
"""

import tkinter as tk

from GameRound import *
from History import History

screen = tk.Tk()
screen.geometry("400x400")
screen.title("Pokemon Battle")

game_round = GameRound()


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.frame = WelcomeScreen(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()  # Remove the current frame
        self.frame = frame(self)  # Create the new frame
        self.frame.pack()

    def change_screen2(self):
        if game_round.battle():
            self.change(EndScreen)
        else:
            self.change(DamageScreen)


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

        btn_continue = tk.Button(self, text="Continue", command=lambda: controller.change_screen2())
        btn_continue.grid(row=4, column=0, columnspan=5, pady=10)

        btn_back = tk.Button(self, text="Back", command=lambda: controller.change(PickAnAction))
        btn_back.grid(row=5, column=0, columnspan=5, pady=10)

        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.grid(row=6, column=0, columnspan=5, pady=10)


class DamageScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        lbl_hp1 = tk.Label(self,
                           text=f"{game_round.selected_pokemon1.pokemon_name}'s HP is {game_round.selected_pokemon1.pokemon_hp}"
                           )
        lbl_hp1.pack()

        history_event = history.history_getter()[0]

        damage1 = history_event.new_round_damage1
        lbl_damage1 = tk.Label(self, text=f"The damage for {game_round.selected_pokemon1.pokemon_name} is {damage1}")
        lbl_damage1.pack()

        lbl_hp2 = tk.Label(self,
                           text=f"{game_round.selected_pokemon2.pokemon_name}'s HP is {game_round.selected_pokemon2.pokemon_hp}")
        lbl_hp2.pack()
        btn_change_pokemon = tk.Button(self, text="Change Pokemon",
                                       command=lambda: controller.change(PickAPokemonScreen))

        damage2 = history_event.new_round_damage2
        lbl_damage2 = tk.Label(self, text=f"The damage for {game_round.selected_pokemon2.pokemon_name} is {damage2}")
        lbl_damage2.pack()

        if history_event.new_round_critical1:
            lbl_critic1 = tk.Label(self, text=f"{game_round.selected_pokemon1.pokemon_name} landed a critical hit")
            lbl_critic1.pack()
        if history_event.new_round_critical2:
            lbl_critic2 = tk.Label(self, text=f"{game_round.selected_pokemon2.pokemon_name} landed a critical hit")
            lbl_critic2.pack()

        btn_change_pokemon.pack()

        btn_pick_move = tk.Button(self, text="Pick A Move",
                                  command=lambda: controller.change(PickAMoveScreen))
        btn_pick_move.pack()


class EndScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.master)
        controller.master.geometry("600x400")

        history_event = history.history_getter()[0]

        damage1 = history_event.new_round_damage1
        lbl_damage1 = tk.Label(self, text=f"The damage for {game_round.selected_pokemon1.pokemon_name} is {damage1}")
        lbl_damage1.pack()

        damage2 = history_event.new_round_damage2
        lbl_damage2 = tk.Label(self, text=f"The damage for {game_round.selected_pokemon2.pokemon_name} is {damage2}")
        lbl_damage2.pack()

        if history_event.new_round_critical1:
            lbl_critic1 = tk.Label(self, text=f"{game_round.selected_pokemon1.pokemon_name} landed a critical hit")
            lbl_critic1.pack()
        if history_event.new_round_critical2:
            lbl_critic2 = tk.Label(self, text=f"{game_round.selected_pokemon2.pokemon_name} landed a critical hit")
            lbl_critic2.pack()

        if (game_round.pokemon_loser or game_round.pokemon_winner) is None:
            lbl_no_winner = tk.Label(self, text=f"Nobody won")
            lbl_no_winner.pack()
        else:
            lbl_fainted = tk.Label(self, text=f"{game_round.pokemon_loser.pokemon_name} fainted")
            lbl_fainted.pack()
            lbl_winner = tk.Label(self, text=f"{game_round.pokemon_winner.pokemon_name} won")
            lbl_winner.pack()
            if game_round.pokemon_loser in game_round.trainer1_game.trainer_team.values():
                for pokemon in game_round.list_pokemon_participants_team2:
                    exp_for_each = game_round.exp_formula(game_round.pokemon_loser) / len(game_round.trainer2_game.trainer_team)
                    pokemon_lvl_up = game_round.add_exp(exp_for_each, pokemon)

                    lbl_exp = tk.Label(self,
                                       text=f"{pokemon.pokemon_name} gained {exp_for_each} points of exp \n"
                                            f"{pokemon.pokemon_name} experience is now {pokemon.pokemon_exp_getter()}")
                    lbl_exp.pack()
                    if pokemon_lvl_up:
                        lbl_lvl_up = tk.Label(self,
                                              text=f"{pokemon.pokemon_name} leveled up \n"
                                                   f"{pokemon.pokemon_name} level is now {pokemon.pokemon_lvl_getter()}")
                        lbl_lvl_up.pack()
            elif game_round.pokemon_loser in game_round.trainer2_game.trainer_team.values():
                for pokemon in game_round.list_pokemon_participants_team1:
                    exp_for_each = (game_round.exp_formula(game_round.pokemon_loser) /
                                    len(game_round.trainer2_game.trainer_team))
                    pokemon_lvl_up = game_round.add_exp(exp_for_each, pokemon)

                    lbl_exp = tk.Label(self,
                                       text=f"{pokemon.pokemon_name} gained {exp_for_each} points of exp \n"
                                            f"{pokemon.pokemon_name} experience is now {pokemon.pokemon_exp_getter()}")
                    lbl_exp.pack()

                    if pokemon_lvl_up:
                        lbl_lvl_up = tk.Label(self,
                                              text=f"{pokemon.pokemon_name} leveled up \n"
                                                   f"{pokemon.pokemon_name} level is now {pokemon.pokemon_lvl_getter()}")
                        lbl_lvl_up.pack()
        if not game_round.pokemon_left_trainer(game_round.trainer1_game):
            lbl_loser1 = tk.Label(self, text=f"{game_round.trainer1_game.trainer_name} lost")
            lbl_loser1.pack()
        elif not game_round.pokemon_left_trainer(game_round.trainer2_game):
            lbl_loser2 = tk.Label(self, text=f"{game_round.trainer2_game.trainer_name} lost")
            lbl_loser2.pack()
        else:
            btn_pick_another_pokemon = tk.Button(self, text="Pick another Pokemon",
                                                 command=lambda: controller.change(PickAPokemonScreen))
            btn_pick_another_pokemon.pack()

        btn_quit = tk.Button(self, text="Quit", command=screen.destroy)
        btn_quit.pack()


def main():
    MainScreen(screen)
    screen.mainloop()


main()
