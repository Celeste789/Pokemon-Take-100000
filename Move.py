# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:52:20 2025

@author: Celeste
"""

class Move:
    def __init__(self, name, power, move_type, category, pp, accuracy, lvl):
        self.move_name = name
        self.move_power = power
        self.move_type = move_type
        self.move_category = category
        self.move_pp = pp
        self.move_accuracy = accuracy
        self.move_lvl = lvl
