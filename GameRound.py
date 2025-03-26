# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:04:13 2025

@author: Celeste
"""
import json
import random
from VariableStatistics import *
from HistoryEvent import HistoryEvent
from History import History
import VariableStatistics

history = History()


class GameRound:
    def __init__(self):
        self.trainer1_game = VariableStatistics.trainer1
        self.trainer2_game = VariableStatistics.trainer2

        self.selected_pokemon1 = None
        self.selected_move1 = None

        self.selected_pokemon2 = None
        self.selected_move2 = None

        self.pokemon_loser = None
        self.pokemon_winner = None

        self.round_number = 0
        self.new_round_critical_bool = False
        self.history_event = None

        self.list_pokemon_participants_team1 = []
        self.list_pokemon_participants_team2 = []

        self.list_pokemon_leveled_up = []

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
        self.pokemon_loser.pokemon_fainted_setter(True)

    def pokemon_winner_setter(self, pokemon):
        self.pokemon_winner = pokemon

    def pokemon_history_event_setter(self, round_number, pokemon1, pokemon2, damage1, damage2, critical1, critical2):
        self.history_event = HistoryEvent(
            round_number, pokemon1, pokemon2, damage1, damage2, critical1, critical2
        )

    def battle(self):
        # 1
        done = True
        # 2
        self.round_number += 1
        # 3
        pokemon1 = self.selected_pokemon1
        pokemon2 = self.selected_pokemon2
        # 4
        if pokemon1 not in self.list_pokemon_participants_team1:
            self.list_pokemon_participants_team1.append(pokemon1)
        if pokemon2 not in self.list_pokemon_participants_team2:
            self.list_pokemon_participants_team2.append(pokemon2)
        # 5
        move1 = self.selected_move1
        move2 = self.selected_move2
        # 6
        if pokemon2.pokemon_specie.specie_stats["Speed"] > pokemon1.pokemon_specie.specie_stats["Speed"]:
            pokemon_aux = pokemon1
            pokemon1 = pokemon2
            pokemon2 = pokemon_aux
            # 6.5
            move_aux = move1
            move1 = move2
            move2 = move_aux
        # 7
        new_hp1 = pokemon1.pokemon_HP_getter()
        new_hp2 = pokemon2.pokemon_HP_getter()
        # 8
        damage1 = 0
        critical2 = False
        # 9
        damage2, critical1 = self.damage_calculator(attacker=pokemon1, defender=pokemon2, move=move1)
        # 10
        new_hp2 -= damage2
        # 11
        pokemon2.pokemon_HP_setter(new_HP=new_hp2)
        # 12
        if new_hp2 <= 0:
            self.pokemon_loser_setter(pokemon2)
            self.pokemon_winner_setter(pokemon1)
            self.pokemon_loser.pokemon_fainted_setter(True)
        # 13
        else:
            damage1, critical2 = self.damage_calculator(attacker=pokemon2, defender=pokemon1, move=move2)
            new_hp1 -= damage1
            pokemon1.pokemon_HP_setter(new_HP=new_hp1)
            if new_hp1 <= 0:
                self.pokemon_loser_setter(pokemon1)
                self.pokemon_winner_setter(pokemon2)
                self.pokemon_loser.pokemon_fainted_setter(True)
            # 14
            else:
                done = False
        # 15
        if done:
            # 16
            if self.pokemon_loser in self.trainer1_game.trainer_team.values():
                exp_for_each = self.exp_formula(self.pokemon_loser) / len(self.list_pokemon_participants_team2)
                for pokemon in self.list_pokemon_participants_team2:
                    self.add_exp(exp_for_each, pokemon)
                    self.list_pokemon_leveled_up.append(pokemon)
            # 17
            elif self.pokemon_loser in self.trainer2_game.trainer_team.values():
                exp_for_each = self.exp_formula(self.pokemon_loser) / len(self.list_pokemon_participants_team1)
                for pokemon in self.list_pokemon_participants_team1:
                    self.add_exp(exp_for_each, pokemon)
                    self.list_pokemon_leveled_up.append(pokemon)
        self.save_team_to_json(team1, 'save_team_1.json')
        self.save_team_to_json(team2, 'save_team_2.json')
        # 18
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

        return done

    def damage_calculator(self, attacker, defender, move):
        # 1
        power_move = move.move_power
        move_type = move.move_type
        move_category = move.move_category
        # 2
        type2 = defender.pokemon_specie.specie_type
        # 3
        type_effectiveness = type2.type_effectiveness[move_type.type_name]
        # 4
        defense_2 = defender.pokemon_stats["Defense"]
        attack_1 = attacker.pokemon_stats["Attack"]
        # 5
        critical = 1
        critical_bool = False
        # 6
        if move_category == "Special":
            defense_2 = defender.pokemon_stats["Special Defense"]
            attack_1 = attacker.pokemon_stats["Special Attack"]
        # 7
        attacker_lvl = attacker.pokemon_lvl
        # 8
        random_number = random.random()
        if random_number <= 0.05:
            critical_bool = True
            critical = 2
        # 9
        random_number2 = random.uniform(0.9, 1.2)
        partial_damage1 = (2 * attacker_lvl * critical / 5) + 2
        partial_damage2 = partial_damage1 * power_move * attack_1 / defense_2 + 2
        total_damage = partial_damage2 / 20 * type_effectiveness * random_number2
        # 10
        return int(total_damage), critical_bool

    def pokemon_left_trainer(self, trainer):
        # 1
        pokemon_left = False
        for name in trainer.trainer_team.keys():
            if not trainer.trainer_team[name].pokemon_fainted:
                pokemon_left = True
        return pokemon_left

    def exp_formula(self, pokemon_fainted):
        b = pokemon_fainted.pokemon_specie.base_yield_exp
        l = pokemon_fainted.pokemon_lvl
        random_number = random.uniform(0.9, 1.2)
        return int(b * l * random_number / 7)

    def save_team_to_json(self, team, file):
        team_list = []
        for pokemon in team.values():
            pokemon_dict = pokemon_to_dict(pokemon)
            team_list.append(pokemon_dict)
        with open(file, 'w') as f:
            json.dump(team_list, f, indent=3)

    def add_exp(self, exp, pokemon):
        # 1
        lvl_up = False
        # 2
        plus = int(pokemon.pokemon_exp_getter() + exp)
        # 3
        pokemon.pokemon_exp_setter(plus)
        # 4
        if pokemon.pokemon_exp_getter() >= (pokemon.pokemon_lvl + 1) ** 3:
            true_exp = int(pokemon.pokemon_exp_getter() - (pokemon.pokemon_lvl + 1) ** 3)
            pokemon.pokemon_exp_setter(true_exp)
            pokemon.pokemon_lvl += 1
            lvl_up = True
        # 5
        return lvl_up
