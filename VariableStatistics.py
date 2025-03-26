# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:36:59 2025

@author: Celeste
"""

from StaticsStatistics import *
from Pokemon import Pokemon
from Trainer import Trainer

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


def pokemon_to_dict(pokemon_object: Pokemon) -> dict:
    pokemon_name = pokemon_object.pokemon_name
    pokemon_specie = pokemon_object.pokemon_specie
    pokemon_moves = []
    for name in pokemon_object.pokemon_moves.keys():
        pokemon_moves.append(name)
    pokemon_stats = pokemon_object.pokemon_stats
    pokemon_lvl = pokemon_object.pokemon_lvl
    pokemon_exp = pokemon_object.pokemon_exp
    pokemon_hp = pokemon_object.pokemon_hp
    pokemon_fainted = pokemon_object.pokemon_fainted

    dic = {
        "Name": pokemon_name,
        "Specie": pokemon_specie.specie_name,
        "Moves": pokemon_moves,
        "Stats": pokemon_stats,
        "Lvl": pokemon_lvl,
        "Exp": pokemon_exp,
        "HP": pokemon_hp,
        "Fainted": pokemon_fainted
    }
    return dic


def dic_to_pokemon(pokemon_dic: dict) -> Pokemon:
    pokemon_name = pokemon_dic["Name"]
    pokemon_specie = species_dict[pokemon_dic["Specie"]]
    pokemon_moves_aux = pokemon_dic["Moves"]
    pokemon_moves = {}
    for move_name in pokemon_moves_aux:
        pokemon_moves[move_name] = moves_dict[move_name]
    pokemon_stats = pokemon_dic["Stats"]
    pokemon_lvl = pokemon_dic["Lvl"]
    pokemon_exp = pokemon_dic["Exp"]
    pokemon_hp = pokemon_dic["HP"]
    pokemon_fainted = pokemon_dic["Fainted"]
    return Pokemon(pokemon_name,
                   pokemon_specie,
                   pokemon_moves,
                   pokemon_stats,
                   pokemon_lvl,
                   pokemon_exp,
                   pokemon_hp,
                   pokemon_fainted)


def team_to_dict(team: dict) -> dict:
    final_dict = {}
    for name, pokemon in team:
        final_dict[name] = pokemon_to_dict(pokemon)
    return final_dict


def dict_to_team(team_dict: dict) -> dict:
    final_team = {}
    for name, pokemon_dict in team_dict:
        final_team[name] = dic_to_pokemon(pokemon_dict)
    return final_team


def trainer_to_dict(trainer: Trainer) -> dict:
    final_dict = {}
    trainer_name = trainer.trainer_name
    trainer_team = team_to_dict(trainer.trainer_team)
    trainer_potions = trainer.trainer_potions
    final_dict["Name"] = trainer_name
    final_dict["Team"] = trainer_team
    final_dict["Potions"] = trainer_potions


def trainer_dict_to_trainer(trainer_dict: dict) -> Trainer:
    trainer_name = trainer_dict["Name"]
    trainer_team = dict_to_team(trainer_dict["Team"])
    trainer_potions = trainer_dict["Potions"]
    trainer = Trainer(trainer_name, trainer_team, trainer_potions)
    return trainer


cyndi_dict = pokemon_to_dict(cyndi)
toto_dict = pokemon_to_dict(toto)
chiko_dict = pokemon_to_dict(chiko)
ratta1_dict = pokemon_to_dict(ratta1)
ratta2_dict = pokemon_to_dict(ratta2)

if __name__ == "__main__":
    pass
