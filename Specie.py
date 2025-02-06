# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:41:45 2025

@author: Celeste
"""


class Specie:
    def __init__(self, name, specie_type, learnset, hp, stats, BYE):
        self.specie_name = name
        self.specie_type = specie_type
        self.specie_learnset = learnset
        self.specie_hp = hp
        self.specie_stats = stats
        self.base_yield_exp = BYE
