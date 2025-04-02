from VariableStatistics import *

pokemon_list = [
    cyndi_dict,
    toto_dict,
    chiko_dict,
    ratta1_dict,
    ratta2_dict,
    hoot1_dict,
    hoot2_dict,
    geo1_dict,
    geo2_dict
]

with open("teams.json", 'w') as f:
    json.dump(pokemon_list, f, indent=3)











