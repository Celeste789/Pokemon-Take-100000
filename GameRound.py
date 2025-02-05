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
import random
from Battle import *
from HistoryEvent import HistoryEvent
from History import History

history = History()


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

        self.round_number = 0
        self.new_round_critical_bool = False
        self.history_event = None

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
        self.pokemon_loser.pokemon_status_setter(False)

    def pokemon_winner_setter(self, pokemon):
        self.pokemon_winner = pokemon

    def pokemon_history_event_setter(self, round_number, pokemon1, pokemon2, damage1, damage2, critical1, critical2):
        self.history_event = HistoryEvent(
            round_number, pokemon1, pokemon2, damage1, damage2, critical1, critical2
        )

    def battle(self):
        done = True
        self.round_number += 1

        pokemon1 = self.selected_pokemon1
        pokemon2 = self.selected_pokemon2

        move1 = self.selected_move1
        move2 = self.selected_move2

        old_hp1 = pokemon1.pokemon_hp
        old_hp2 = pokemon2.pokemon_hp

        new_hp1 = pokemon1.pokemon_HP_getter()
        new_hp2 = pokemon2.pokemon_HP_getter()

        damage1, critical1 = self.damage_calculator(attacker=pokemon2, defender=pokemon1, move=move2)
        damage2, critical2 = self.damage_calculator(attacker=pokemon1, defender=pokemon2, move=move1)

        self.pokemon_history_event_setter(
            round_number=self.round_number,
            pokemon1=pokemon1,
            pokemon2=pokemon2,
            damage1=damage1,
            damage2=damage2,
            critical1=critical1,
            critical2=critical2
        )

        history.add(event=self.history_event)

        new_hp1 -= damage1
        new_hp2 -= damage2

        Pokemon.pokemon_HP_setter(pokemon1, new_HP=new_hp1)
        Pokemon.pokemon_HP_setter(pokemon2, new_HP=new_hp2)

        if new_hp2 <= 0:
            self.pokemon_loser_setter(pokemon2)
            self.pokemon_winner_setter(pokemon1)
            self.pokemon_loser.pokemon_fainted_setter(True)
        elif new_hp1 <= 0:
            self.pokemon_loser_setter(pokemon1)
            self.pokemon_winner_setter(pokemon2)
            self.pokemon_loser.pokemon_fainted_setter(True)
        else:
            done = False
            # self.selected_pokemon1.pokemon_HP_setter(old_hp1)
            # self.selected_pokemon2.pokemon_HP_setter(old_hp2)

        return done

    def damage_calculator(self, attacker, defender, move):
        power_move = move.move_power

        move_type = move.move_type
        move_category = move.move_category

        type2 = defender.pokemon_specie.specie_type
        type_effectiveness = type2.type_effectiveness[move_type.type_name]

        defense_2 = defender.pokemon_stats["Defense"]
        attack_1 = attacker.pokemon_stats["Attack"]

        critical = 1
        critical_bool = False

        if move_category == "Special":
            defense_2 = defender.pokemon_stats["Special Defense"]
            attack_1 = attacker.pokemon_stats["Special Attack"]

        attacker_lvl = attacker.pokemon_lvl

        random_number = random.random()
        if random_number <= 0.05:
            critical_bool = True
            critical = 2

        random_number2 = random.uniform(0.9, 1.2)
        partial_damage1 = (2 * attacker_lvl * critical / 5) + 2
        partial_damage2 = partial_damage1 * power_move * attack_1 / defense_2 + 2
        total_damage = partial_damage2 / 20 * type_effectiveness * random_number2

        return int(total_damage), critical_bool

        # pokemon1_exp = pokemon1.pokemon_exp
        # pokemon2_exp = pokemon2.pokemon_exp


    def pokemon_left_trainer(self, trainer):
        pokemon_left = False
        for name in trainer.trainer_team.keys():
            if not trainer.trainer_team[name].pokemon_fainted:
                pokemon_left = True
        return pokemon_left


