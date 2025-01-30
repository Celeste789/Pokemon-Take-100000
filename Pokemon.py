# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:40:07 2025

@author: Celeste
"""

from random import uniform


class Pokemon:
    def __init__(self, name, specie, moves):
        self.pokemon_name = name
        self.pokemon_specie = specie
        self.pokemon_moves = moves
        self.pokemon_stats = self.stats
        self.pokemon_lvl = 5
        self.pokemon_exp = 0

    def pokemon_HP_setter(self, new_HP):
        self.pokemon_stats["HP"] = new_HP

    def pokemon_lvl_setter(self, new_lvl):
        self.pokemon_lvl = new_lvl

    def pokemon_exp_setter(self, new_exp):
        self.pokemon_exp = new_exp

    def pokemon_hp_calculator(self):
        hp = (0.02 * self.pokemon_specie.specie_stats["HP"] * self.pokemon_lvl + self.pokemon_lvl + 10) * uniform(1.1,
                                                                                                                  19)
        return hp

    def pokemon_stats_calculator(self, stat):
        new_stat = (0.02 * 2 * self.pokemon_specie.specie_stats[stat] * self.pokemon_lvl + 5) * uniform(1.1, 1.9)
        return new_stat

    stats = {
        "HP": pokemon_hp_calculator()
    }
    for stat_name, stat_value in stats.items():
        stats[stat_name] = pokemon_stats_calculator(stat_name)
