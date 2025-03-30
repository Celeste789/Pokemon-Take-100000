import json

import VariableStatistics
from VariableStatistics import *

pokemon_dicts = [
    cyndi_dict,
    toto_dict,
    chiko_dict,
    ratta1_dict,
    ratta2_dict
]

with open('teams.json', 'w') as f:
    json.dump(pokemon_dicts, f, indent=3)









