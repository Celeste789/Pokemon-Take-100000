# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:04:13 2025

@author: Celeste
"""
# from Specie import Specie
# from Pokemon import Pokemon
# from Type import Type
# from Move import Move
# from Trainer import Trainer
from Battle import *
from random import randint


class GameRound:
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
        done = True

        pokemon1 = self.selected_pokemon1
        pokemon2 = self.selected_pokemon2

        move1 = self.selected_move1
        move2 = self.selected_move2

        old_hp1 = pokemon1.pokemon_hp
        old_hp2 = pokemon2.pokemon_hp

        new_hp1 = pokemon1.pokemon_hp
        new_hp2 = pokemon2.pokemon_hp

        new_hp1 -= int(self.damage_calculator(pokemon2, pokemon1, move2))
        new_hp2 -= int(self.damage_calculator(pokemon1, pokemon2, move1))

        Pokemon.pokemon_HP_setter(pokemon1, new_HP=new_hp1)
        Pokemon.pokemon_HP_setter(pokemon2, new_HP=new_hp2)

        if new_hp2 <= 0:
            self.pokemon_loser_setter(pokemon2)
            self.pokemon_winner_setter(pokemon1)
        elif new_hp1 <= 0:
            self.pokemon_loser_setter(pokemon1)
            self.pokemon_winner_setter(pokemon2)
        else:
            done = False

        return done

    def damage_calculator(self, pokemon1, pokemon2, move):
        power_move = move.move_power

        move_type = move.move_type
        type2 = pokemon2.pokemon_specie.specie_type

        type_effectiveness = type2.type_effectiveness[move_type.type_name]

        move1_category = move.move_category

        defense_2 = pokemon2.pokemon_stats["Defense"]
        attack_1 = pokemon1.pokemon_stats["Attack"]

        critical = 1

        if move1_category == "Special":
            defense_2 = pokemon2.pokemon_stats["Special Defense"]
            attack_1 = pokemon1.pokemon_stats["Special Attack"]

        pokemon1_lvl = pokemon1.pokemon_lvl

        random_number = randint(1, 6)
        if random_number == 1:
            critical = 2

        partial_damage1 = (2 * pokemon1_lvl * critical / 5) + 2
        partial_damage2 = partial_damage1 * power_move * attack_1 / defense_2 + 2
        total_damage = partial_damage2 / 20 * type_effectiveness

        return int(total_damage)

        # pokemon1_exp = pokemon1.pokemon_exp
        # pokemon2_exp = pokemon2.pokemon_exp
