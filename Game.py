# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:04:13 2025

@author: Celeste
"""

from Specie import Specie
from Pokemon import Pokemon
from Type import Type
from Move import Move
from Trainer import Trainer
from Battle import *


class Game:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2        
        
        self.selected_pokemon1 = None
        self.selected_move1 = None
        
        self.selected_pokemon2 = None
        self.selected_move2 = None
        

game = Game(trainer1, trainer2)