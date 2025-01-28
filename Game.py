# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:04:13 2025

@author: Celeste
"""
from Specie import Specie
from Pokemon import Pokemon
from Type import Type
from Move import Move
from Trainer import Trainer
from Battle import *


class Game:
    def __init__(self, trainer1_game, trainer2_game):
        self.trainer1_game = trainer1_game
        self.trainer2_game = trainer2_game

        self.selected_pokemon1 = None
        self.selected_move1 = None

        self.selected_pokemon2 = None
        self.selected_move2 = None

        self.pokemon_loser = None
        self.pokemon_winner = None

    def selected_pokemon1_setter(self, pokemon_name):
        self.selected_pokemon1 = self.trainer1_game.trainer_team[pokemon_name]

    def selected_pokemon2_setter(self, pokemon_name):
        self.selected_pokemon2 = self.trainer2_game.trainer_team[pokemon_name]

    def selected_move1_setter(self, move_name):
        self.selected_move1 = self.selected_pokemon1.pokemon_moves[move_name]

    def selected_move2_setter(self, move_name):
        self.selected_move2 = self.selected_pokemon2.pokemon_moves[move_name]

    def pokemon_loser_setter(self, pokemon):
        self.pokemon_loser = pokemon

    def pokemon_winner_setter(self, pokemon):
        self.pokemon_winner = pokemon

    def battle(self):

        done = False

        pokemon1 = self.selected_pokemon1
        pokemon2 = self.selected_pokemon2

        move1 = self.selected_move1
        move2 = self.selected_move2

        power_move1 = move1.move_power
        power_move2 = move2.move_power

        new_hp1 = pokemon1.pokemon_stats["HP"]
        new_hp2 = pokemon2.pokemon_stats["HP"]

        new_hp1 -= power_move2
        new_hp2 -= power_move1

        Pokemon.pokemon_HP_setter(pokemon1, new_HP=new_hp1)
        Pokemon.pokemon_HP_setter(pokemon2, new_HP=new_hp2)

        if new_hp2 <= 0 < new_hp1:
            self.pokemon_loser_setter(pokemon2)
            self.pokemon_winner_setter(pokemon1)

        elif new_hp1 <= 0 < new_hp2:
            self.pokemon_loser_setter(pokemon1)
            self.pokemon_winner_setter(pokemon2)

        else:

            done = True

        return done

    # Pokemon.pokemon_HP_setter(self=self.selected_pokemon1, new_HP=pokemon1.pokemon_stats["HP"])
    # Pokemon.pokemon_HP_setter(self=self.selected_pokemon2, new_HP=pokemon2.pokemon_stats["HP"])
