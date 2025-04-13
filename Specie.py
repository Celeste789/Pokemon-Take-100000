# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:41:45 2025

@author: Celeste
"""


class Specie:
    def __init__(self, name, specie_type1, learnset, hp, stats, total_stats, BYE, starter, specie_type2=None):
        self.specie_name = name
        self.specie_type1 = specie_type1
        self.specie_type2 = specie_type2
        self.specie_learnset = learnset
        self.specie_hp = hp
        self.specie_stats = stats
        self.total_stats = total_stats
        self.base_yield_exp = BYE
        self.starter = starter
