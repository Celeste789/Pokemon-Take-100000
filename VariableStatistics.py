# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:36:59 2025

@author: Celeste
"""

from StaticsStatistics import *
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


def pokemon_to_dic(pokemon_object: Pokemon) -> dict:
    pokemon_name = pokemon_object.pokemon_name
    pokemon_specie = pokemon_object.pokemon_specie
    pokemon_moves = pokemon_object.pokemon_moves
    pokemon_stats = pokemon_object.pokemon_stats
    pokemon_lvl = pokemon_object.pokemon_lvl
    pokemon_exp = pokemon_object.pokemon_exp
    pokemon_status = pokemon_object.pokemon_status
    pokemon_hp = pokemon_object.pokemon_hp

    dic = {
        "Name": pokemon_name,
        "Specie": pokemon_specie,
        "Moves": pokemon_moves,
        "Stats": pokemon_stats,
        "Lvl": pokemon_lvl,
        "Exp": pokemon_exp,
        "Status": pokemon_status,
        "HP": pokemon_hp
    }
    return dic


def dic_to_pokemon(pokemon_dic: dict) -> Pokemon:
    pokemon_name = pokemon_dic["Name"]
    pokemon_specie = pokemon_dic["Specie"]
    pokemon_moves = pokemon_dic["Moves"]
    pokemon_stats = pokemon_dic["Stats"]
    pokemon_lvl = pokemon_dic["Lvl"]
    pokemon_exp = pokemon_dic["Exp"]
    pokemon_status = pokemon_dic["Status"]
    pokemon_hp = pokemon_dic["HP"]
    return Pokemon(pokemon_name,
                   pokemon_specie,
                   pokemon_moves,
                   pokemon_stats,
                   pokemon_lvl,
                   pokemon_exp,
                   pokemon_status,
                   pokemon_hp)
