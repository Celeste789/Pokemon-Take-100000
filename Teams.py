import json
from VariableStatistics import *

pokemon_dicts = [chiko_dict, chiko_dict, todo_dict, ratta1_dict, ratta2_dict]

with open('teams.json', 'w') as f:
    json.dump(pokemon_dicts, f, indent=3)





