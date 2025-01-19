# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:36:59 2025

@author: Celeste
"""


import Specie
import Pokemon
import Type
import Move
import Trainer

type_effectiveness_fire = {
    "Water": 1/2,
    "Fire": 1/2,
    "Grass": 1/2,
    "Normal": 1
    }

type_effectiveness_water = {
    "Water": 1/2,
    "Fire": 2,
    "Grass": 1/2,
    "Normal": 1
    }

type_effectiveness_grass = {
    "Water": 2,
    "Fire": 1/2,
    "Grass":1/2,
    "Normal":1
    }


type_effectiveness_normal = {
    "Water": 1,
    "Fire": 1,
    "Grass":1,
    "Normal":1
    }



fire = Type("Fire", type_effectiveness_fire)
water = Type("Water", type_effectiveness_water)
grass = Type("Grass", type_effectiveness_grass)
normal = Type("Normal", type_effectiveness_normal)



ember = Move("Ember", 40, fire, "Special")
water_gun = Move("Water Gun", 35, water, "Physical")
razor_leaf = Move("Razor Leaf", 30, grass, "Special")
tackle = Move("Tackle", 30, normal, "Physical")


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

ratta_stats = {
    "HP": 35,
    "Attack": 30,
    "Special Attack": 25,
    "Defense": 20,
    "Special Defense": 20,
    "Speed": 20
    }

cyndaquil = Specie("Cyndaquil", fire, [ember, tacke], [])
cyndi = Pokemon("Cyndi", cyndaquil,[ember, tackle],cyndi_stats)

chikorita = Specie("Chikorita", grass, [razor_leaf, tackle], [])
chiko = Pokemon("Chiko", chikorita, [razor_leaf], chiko_stats)


squirtle = Specie("Squirtle", water, [water_gun, tackle], [])
squirt = Pokemon("Squirt", squirtle, [water_gun, tackle], squirt_stats)

rattata = Specie("Rattata", normal, [tackle], [])
ratta1 = Pokemon("Ratta1", rattata, [tackle], ratta_stats)
ratta2 = Pokemon("Ratta2", rattata, [tackle], ratta_stats)


team1 = {
    "Squirt": squirt,
    "Ratta1": ratta1
    }

team2 = {
    "Chiko": chiko,
    "Ratta2": ratta2
        
    }

trainer1 = Trainer("Trainer_1", team1, [])
trainer2 = Trainer("Trainer_2", team2, [])


# def battle(pokemon1, pokemon2):
    
#     specie1 = pokemon1.pokemon_specie
#     moves1 = pokemon1.pokemon_moves
#     stats1 = pokemon1.pokemon_stats
    
#     specie2 = pokemon2.pokemon_specie
#     moves2 = pokemon2.pokemon_moves
#     stats2 = pokemon2.pokemon_stats
    
#     while stats1["HP"] > 0 and stats2["HP"] > 0:
        










