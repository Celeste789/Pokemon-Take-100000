# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:40:07 2025

@author: Celeste
"""

class Pokemon:
    
    def __init__(self, name, specie, moves, stats):
        self.pokemon_name = name
        self.pokemon_specie = specie
        self.pokemon_moves = moves
        self.pokemon_stats = stats

    def pokemon_HP_setter(self, new_HP):
        self.pokemon_stats["HP"] = new_HP

        
    
        