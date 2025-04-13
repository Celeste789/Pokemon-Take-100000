# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:36:59 2025

@author: Celeste
"""
import json
import StaticsStatistics

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

hoothoot_moves = {
    "Peck": peck
}

geodude_moves = {
    "Roll Out": roll_out
}

cyndi = Pokemon("Cyndi", cyndaquil, cyndi_moves)
chiko = Pokemon("Chiko", chikorita, chiko_moves)
toto = Pokemon("Toto", totodile, toto_moves)
ratta1 = Pokemon("Ratta1", rattata, ratta_moves)
ratta2 = Pokemon("Ratta2", rattata, ratta_moves)
hoot1 = Pokemon("Hoot1", hoothoot, hoothoot_moves)
hoot2 = Pokemon("Hoot2", hoothoot, hoothoot_moves)
geo1 = Pokemon("Geo1", geodude, geodude_moves)
geo2 = Pokemon("Geo2", geodude, geodude_moves)

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


def dict_to_pokemon(pokemon_dic: dict) -> Pokemon:
    pokemon_name = pokemon_dic["Name"]
    pokemon_specie = StaticsStatistics.dict_of_dicts_species_class[pokemon_dic["Specie"]]
    # pokemon_moves_aux = pokemon_dic["Moves"]
    # pokemon_moves = {}
    # for move_name in pokemon_moves_aux:
    #     pokemon_moves[move_name] = Move(name=move_name,
    #                                     )
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


def team_to_dict(team: specie_it) -> specie_it:
    final_dict = {}
    for name, pokemon in team:
        final_dict[name] = pokemon_to_dict(pokemon)
    return final_dict


def dict_to_team(team_dict: specie_it) -> specie_it:
    final_team = {}
    for name, pokemon_dict in team_dict:
        final_team[name] = dict_to_pokemon(pokemon_dict)
    return final_team


def trainer_to_dict(trainer: Trainer) -> specie_it:
    final_dict = {}
    trainer_name = trainer.trainer_name
    trainer_team = team_to_dict(trainer.trainer_team)
    trainer_potions = trainer.trainer_potions
    final_dict["Name"] = trainer_name
    final_dict["Team"] = trainer_team
    final_dict["Potions"] = trainer_potions


def trainer_dict_to_trainer(trainer_dict: specie_it) -> Trainer:
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
geo1_dict = pokemon_to_dict(geo1)
geo2_dict = pokemon_to_dict(geo2)
hoot1_dict = pokemon_to_dict(hoot1)
hoot2_dict = pokemon_to_dict(hoot2)

with open('teams.json', 'r') as f:
    pokemon_dicts_read = json.load(f)

list_of_pokemon = []

for dictionary in pokemon_dicts_read:
    pokemon = dict_to_pokemon(dictionary)
    list_of_pokemon.append(pokemon)

dict_of_pokemons = {}
for pokemon in list_of_pokemon:
    dict_of_pokemons[pokemon.pokemon_name] = pokemon

cyndi = dict_of_pokemons["Cyndi"]
chiko = dict_of_pokemons["Chiko"]
toto = dict_of_pokemons["Toto"]
ratta1 = dict_of_pokemons["Ratta1"]
ratta2 = dict_of_pokemons["Ratta2"]
hoot1 = dict_of_pokemons["Hoot1"]
hoot2 = dict_of_pokemons["Hoot2"]
geo1 = dict_of_pokemons["Geo1"]
geo2 = dict_of_pokemons["Geo2"]

if __name__ == "__main__":
    pass
