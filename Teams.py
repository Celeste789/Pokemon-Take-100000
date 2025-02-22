import json
from VariableStatistics import *

pokemon_dicts = {
    "Cyndi": cyndi_dict,
    "Chiko": chiko_dict,
    "Toto": toto_dict,
    "Ratta1": ratta1_dict,
    "Ratta2": ratta2_dict
}

with open('teams.json', 'w') as f:
    json.dump(pokemon_dicts, f, indent=3)





