# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:36:59 2025

@author: Celeste
"""


from StaticsStats import *
from Pokemon import Pokemon
from Trainer import Trainer

cyndaquil_stats = {
    "Attack": 52,
    "Special Attack": 60,
    "Defense": 49,
    "Special Defense": 50,
    "Speed": 65
}

cyndaquil_hp = 39
chikorita_hp = 45
totodile_hp = 50
rattata_hp = 30

cyndi_moves = {
    "Ember": ember,
    "Tackle": tackle
}

chiko_moves = {
    "Razor Leaf": razor_leaf,
    "Tackle": tackle
}

toto_moves = {
    "Water Gun": water_gun,
    "Tackle": tackle
}

ratta_moves = {
    "Tackle": tackle
}

cyndi = Pokemon("Cyndi", cyndaquil, cyndi_moves)
chiko = Pokemon("Chiko", chikorita, chiko_moves)


toto = Pokemon("Toto", totodile, toto_moves)

ratta1 = Pokemon("Ratta1", rattata, ratta_moves)
ratta2 = Pokemon("Ratta2", rattata, ratta_moves)

team1 = {
    "Toto": toto,
    "Ratta1": ratta1
}

team2 = {
    "Chiko": chiko,
    "Ratta2": ratta2
}

trainer1 = Trainer("Trainer_1", team1, [])
trainer2 = Trainer("Trainer_2", team2, [])
