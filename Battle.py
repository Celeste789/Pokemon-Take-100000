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
    "Water": 1 / 2,
    "Fire": 1 / 2,
    "Grass": 1 / 2,
    "Normal": 1
}

type_effectiveness_water = {
    "Water": 1 / 2,
    "Fire": 2,
    "Grass": 1 / 2,
    "Normal": 1
}

type_effectiveness_grass = {
    "Water": 2,
    "Fire": 1 / 2,
    "Grass": 1 / 2,
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

ember = Move("Ember", 10, fire, "Special")
water_gun = Move("Water Gun", 11, water, "Physical")
razor_leaf = Move("Razor Leaf", 12, grass, "Special")
tackle = Move("Tackle", 10, normal, "Physical")

cyndi_stats = {
    "HP": 50,
    "Attack": 20,
    "Special Attack": 30,
    "Defense": 30,
    "Special Defense": 20,
    "Speed": 15
}

chiko_stats = {
    "HP": 45,
    "Attack": 30,
    "Special Attack": 20,
    "Defense": 10,
    "Special Defense": 20,
    "Speed": 15
}

toto_stats = {
    "HP": 40,
    "Attack": 35,
    "Special Attack": 20,
    "Defense": 25,
    "Special Defense": 15,
    "Speed": 20
}

ratta_stats = {
    "HP": 35,
    "Attack": 30,
    "Special Attack": 25,
    "Defense": 20,
    "Special Defense": 20,
    "Speed": 20
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

cyndaquil = Specie("Cyndaquil", fire, [ember, tackle], [])
cyndi = Pokemon("Cyndi", cyndaquil, cyndi_moves, cyndi_stats)

chikorita = Specie("Chikorita", grass, [razor_leaf, tackle], [])
chiko = Pokemon("Chiko", chikorita, chiko_moves, chiko_stats)

totodile = Specie("Totodile", water, [water_gun, tackle], [])
toto = Pokemon("Toto", totodile, toto_moves, toto_stats)

rattata = Specie("Rattata", normal, [tackle], [])
ratta1 = Pokemon("Ratta1", rattata, ratta_moves, ratta_stats)
ratta2 = Pokemon("Ratta2", rattata, ratta_moves, ratta_stats)

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


