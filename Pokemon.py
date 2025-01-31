# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:40:07 2025

@author: Celeste
"""

from random import uniform

from Specie import Specie


class Pokemon:
    def __init__(self, name, specie, moves):
        self.pokemon_name = name
        self.pokemon_specie = specie
        self.pokemon_moves = moves
        self.pokemon_hp = None
        self.pokemon_stats = {}
        self.pokemon_lvl = 5
        self.pokemon_exp = 0
        self.pokemon_status = True

        self.pokemon_hp = self.pokemon_hp_calculator()

        for stat_name, stat_value in self.pokemon_specie.specie_stats.items():
            self.pokemon_stats[stat_name] = self.pokemon_stats_calculator(stat_name)

    def pokemon_HP_setter(self, new_HP):
        self.pokemon_hp = new_HP

    def pokemon_HP_getter(self):
        return self.pokemon_hp

    def pokemon_lvl_setter(self, new_lvl):
        self.pokemon_lvl = new_lvl

    def pokemon_exp_setter(self, new_exp):
        self.pokemon_exp = new_exp

    def pokemon_hp_calculator(self):
        hp = (0.02 * self.pokemon_specie.specie_hp * self.pokemon_lvl + self.pokemon_lvl + 10) * uniform(0.9, 1.2)
        return int(hp)

    def pokemon_stats_calculator(self, stat):
        new_stat = (0.02 * 2 * self.pokemon_specie.specie_stats[stat] * self.pokemon_lvl + 5) * uniform(0.9, 1.2)
        return int(new_stat)

    def pokemon_status_setter(self, new_status):
        self.pokemon_status = new_status
