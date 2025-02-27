# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:40:07 2025

@author: Celeste
"""

from random import uniform


class Pokemon:
    def __init__(self, name, specie, moves, stats=None, status=True, hp=None, lvl=1, exp=0, fainted=False):
        self.pokemon_name = name
        self.pokemon_specie = specie
        self.pokemon_moves = moves
        self.pokemon_lvl = lvl
        self.pokemon_exp = exp
        self.pokemon_status = status
        if not hp:
            self.pokemon_hp = self.pokemon_hp_calculator()
        else:
            self.pokemon_hp = hp
        if not stats:
            self.pokemon_stats = {}
            for stat_name, stat_value in self.pokemon_specie.specie_stats.items():
                self.pokemon_stats[stat_name] = self.pokemon_stats_calculator(stat_name)
        else:
            self.pokemon_stats = stats
        self.pokemon_fainted = fainted

    def pokemon_HP_setter(self, new_HP):
        self.pokemon_hp = new_HP

    def pokemon_HP_getter(self):
        return self.pokemon_hp

    def pokemon_lvl_setter(self, new_lvl):
        self.pokemon_lvl = new_lvl

    def pokemon_lvl_getter(self):
        return self.pokemon_lvl

    def pokemon_exp_setter(self, new_exp):
        self.pokemon_exp = int(new_exp)

    def pokemon_fainted_getter(self):
        return self.pokemon_fainted

    def pokemon_fainted_setter(self, boolean):
        self.pokemon_fainted = boolean

    def pokemon_hp_calculator(self):
        hp = (0.02 * self.pokemon_specie.specie_hp * self.pokemon_lvl + self.pokemon_lvl + 10) * uniform(0.9, 1.2)
        return int(hp)

    def pokemon_stats_calculator(self, stat):
        new_stat = (0.02 * 2 * self.pokemon_specie.specie_stats[stat] * self.pokemon_lvl + 5) * uniform(0.9, 1.2)
        return int(new_stat)

    def pokemon_status_setter(self, new_status):
        self.pokemon_status = new_status

    def pokemon_exp_getter(self):
        return self.pokemon_exp
