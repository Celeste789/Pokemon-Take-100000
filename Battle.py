# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:36:59 2025

@author: Celeste
"""

from Specie import Specie
from Pokemon import Pokemon
from Type import Type
from Move import Move
from Trainer import Trainer

type_effectiveness_fire = {
    "Water": 2,
    "Fire": 1/2,
    "Grass": 1/2,
    "Normal": 1
}

type_effectiveness_water = {
    "Water": 1/2,
    "Fire": 1/2,
    "Grass": 2,
    "Normal": 1
}

type_effectiveness_grass = {
    "Water": 1/2,
    "Fire": 2,
    "Grass": 1/2,
    "Normal": 1
}

type_effectiveness_normal = {
    "Water": 1,
    "Fire": 1,
    "Grass": 1,
    "Normal": 1
}

fire = Type("Fire", type_effectiveness_fire)
water = Type("Water", type_effectiveness_water)
grass = Type("Grass", type_effectiveness_grass)
normal = Type("Normal", type_effectiveness_normal)

ember = Move("Ember", 45, fire, "Special")
water_gun = Move("Water Gun", 40, water, "Special")
razor_leaf = Move("Razor Leaf", 45, grass, "Physical")
tackle = Move("Tackle", 40, normal, "Physical")

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

chikorita_stats = {
    "Attack": 49,
    "Special Attack": 49,
    "Defense": 65,
    "Special Defense": 65,
    "Speed": 45
}

totodile_stats = {
    "Attack": 65,
    "Special Attack": 44,
    "Defense": 64,
    "Special Defense": 48,
    "Speed": 45
}

rattata_stats = {
    "Attack": 56,
    "Special Attack": 25,
    "Defense": 35,
    "Special Defense": 35,
    "Speed": 72
}

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

cyndaquil = Specie("Cyndaquil", fire, [ember, tackle], cyndaquil_hp, cyndaquil_stats, 65)
cyndi = Pokemon("Cyndi", cyndaquil, cyndi_moves)

chikorita = Specie("Chikorita", grass, [razor_leaf, tackle], hp=chikorita_hp, stats=chikorita_stats, BYE=64)
chiko = Pokemon("Chiko", chikorita, chiko_moves)

totodile = Specie("Totodile", water, [water_gun, tackle], hp=totodile_hp, stats=totodile_stats, BYE=66)
toto = Pokemon("Toto", totodile, toto_moves)

rattata = Specie("Rattata", normal, [tackle], hp=rattata_hp, stats=rattata_stats, BYE=57)
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


