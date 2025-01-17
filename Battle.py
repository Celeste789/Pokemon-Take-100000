# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:36:59 2025

@author: Celeste
"""


from Specie import *
from Pokemon import *
from Type import *
from Move import *


type_effectiveness_fire = {
    "Water": 1/2,
    "Fire": 1/2,
    "Grass": 1/2
    }

type_effectiveness_water = {
    "Water": 1/2,
    "Fire": 2,
    "Grass": 1/2
    }

type_effectiveness_grass = {
    "Water": 2,
    "Fire": 1/2,
    "Grass":1/2
    }



fire = Type("Fire", type_effectiveness_fire)
water = Type("Water", type_effectiveness_water)
grass = Type("Grass", type_effectiveness_grass)



ember = Move("Ember", 40, fire)
water_gun = Move("Water Gun", 35, water)
razor_leaf = Move("Razor Leaf", 30, grass)


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

squirt_stats = {
    "HP": 40,
    "Attack": 35,
    "Special Attack": 20,
    "Defense": 25,
    "Special Defense": 15,
    "Speed": 20
    }

cyndaquil = Specie("Cyndaquil", fire, [ember], [])
cyndi = Pokemon("Cyndi", cyndaquil,[ember],cyndi_stats)

chikorita = Specie("Chikorita", grass, [razor_leaf], [])
chiko = Pokemon("Chiko", chikorita, [razor_leaf], chiko_stats)


squirtle = Specie("Squirtle", water, [water_gun], [])
squirt = Pokemon("Squirt", squirtle, [water_gun], squirt_stats)



def battle(pokemon1, pokemon2):
    
    specie1 = pokemon1.pokemon_specie
    moves1 = pokemon1.pokemon_moves
    stats1 = pokemon1.pokemon_stats
    
    specie2 = pokemon2.pokemon_specie
    moves2 = pokemon2.pokemon_moves
    stats2 = pokemon2.pokemon_stats
    
    while stats1["HP"] > 0 and stats2["HP"] > 0:
        










