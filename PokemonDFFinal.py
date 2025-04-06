#%%
import pandas as pd
from Move import Move
from Specie import Specie
#%%
feda_learnset_df = pd.read_csv('data frames/feda_learnsets.csv')
pokemon_df_aux = pd.read_csv('data frames/pokemon.csv')
pokemon_df_aux[['Primary Type', 'Secondary Type']] = pokemon_df_aux['Type'].str.split(' ', expand=True)
pokemon_df_aux.drop(columns=['Type'], inplace=True)

stater_species = ["Chikorita", "Cyndaquil", "Totodile", "Bulbasaur", "Charmander", "Squirtle"]
pokemon_df_aux["Starter"] = pokemon_df_aux["Name"].isin(stater_species)

pokemon_df_aux.drop_duplicates(subset=['Name'], inplace=True)
pokemon_df_aux.drop(columns=['Evolution'], inplace=True)
pokemon_df_aux.drop(columns=['Unnamed: 0'], inplace=True)

pokemon_to_remove = set(feda_learnset_df["Pokemon Name"])
pokemon_df_aux_cleaned = pokemon_df_aux[pokemon_df_aux["Name"].isin(pokemon_to_remove)]

pokemon_df_aux_cleaned
#%%
feda_learnset_df.head(3)
#%%
list_of_dict_move = []
for index, move in feda_learnset_df.iterrows():
    dict_move = {"Move": move["Move"], "Power": move["Pwr."], "Type": move["Type"], "Category": move["Cat."]}
    list_of_dict_move.append(dict_move)
for move in list_of_dict_move:
    print(move)
#%%
def dictionary_to_move(move_dictionary):
    move = Move(name=move_dictionary["Move"],
                power=move_dictionary["Power"],
                category=move_dictionary["Category"],
                move_type=move_dictionary["Type"])
    return move
list_of_moves = []
for move_dict in list_of_dict_move:
    move = dictionary_to_move(move_dict)
    list_of_moves.append(move)
for move in list_of_moves:
    print(move.move_name, move.move_power)
#%%
list_of_dict_specie = []
for index, specie in pokemon_df_aux_cleaned.iterrows():
    stats_dict = {"Attack": specie["Attack"], "Defense": specie["Defense"], "Speed": specie["Speed"], "Special Defense": specie["Sp.Def"], "Special Attack": specie["Sp.Atk"]}
    dict_specie = {"Specie Name":specie["Name"], "Specie Type1": specie["Primary Type"], "Specie Type2": specie["Secondary Type"], "Specie Learnset": {}, "Specie BYE": specie["base_experience"], "Starter": specie["Starter"], "Specie HP": specie["HP"], "Specie Stats": stats_dict}
    list_of_dict_specie.append(dict_specie)
print(len(list_of_dict_specie))
for specie in list_of_dict_specie:
    print(specie)
#%%
def dictionary_to_specie(specie_dictionary):
    specie = Specie(name=specie_dictionary["Specie Name"], specie_type1=specie_dictionary["Specie Type1"], specie_type2=specie_dictionary["Specie Type2"], learnset=specie_dictionary["Specie Learnset"], BYE=specie_dictionary["Specie BYE"], hp=specie_dictionary["Specie HP"], stats=specie_dictionary["Specie Stats"], starter=specie_dictionary["Starter"])
    return specie

list_of_species = []
for specie_dict in list_of_dict_specie:
    specie = dictionary_to_specie(specie_dict)
    list_of_species.append(specie)
for specie in list_of_species:
    print(specie.specie_name)
#%%
feda_learnset_df[feda_learnset_df["Pokemon Name"] == "Cyndaquil"]
#%%
cyndaquil_dict_of_moves = {}
for index, move in feda_learnset_df.iterrows():
    list_of_moves_cyndaquil = []
    cyndaquil_moves_df = feda_learnset_df[feda_learnset_df["Pokemon Name"] == "Cyndaquil"]
    for _, move in cyndaquil_moves_df.iterrows():
        move_cyndaquil = Move(name=move["Move"],
                            power=move["Pwr."],
                            category=move["Cat."],
                            move_type=move["Type"])
        list_of_moves_cyndaquil.append(move_cyndaquil)
for move in list_of_moves_cyndaquil:
    print(move.move_name)
#%%
dict_of_dicts_pokemon_moves = {}
for _, row in pokemon_df_aux_cleaned.iterrows():
    pokemon_move_dict = {}
    list_of_moves_not_dicts = []
    specie_name = row["Name"]
    moves_df = feda_learnset_df[feda_learnset_df["Pokemon Name"] == specie_name]
    for _, dict_move in moves_df.iterrows():
        move = Move(name=dict_move["Move"],
                    power=dict_move["Pwr."],
                    category=dict_move["Cat."],
                    move_type=dict_move["Type"])
        list_of_moves_not_dicts.append(move)
    pokemon_move_dict[specie_name] = list_of_moves_not_dicts
    dict_of_dicts_pokemon_moves[specie_name] = pokemon_move_dict
#%%
for key, values in dict_of_dicts_pokemon_moves.items():
    print(key, values)
#%%
for specie in list_of_species:
    for specie_name, move_pok_dict in dict_of_dicts_pokemon_moves.items():
        if specie.specie_name == specie_name:
            specie.specie_learnset = move_pok_dict[specie_name]
for specie in list_of_species:
    for move in specie.specie_learnset:
        name = move.move_name
        print(specie.specie_name, name)
#%%
type_effectiveness_df = pd.read_csv('data frames/chart.csv')
type_effectiveness_df
#%%
type_effectiveness_df[type_effectiveness_df["Attacking"] == "Fire"]["Water"]
#%%
for type in type_effectiveness_df.columns:
    print(type)
#%%
crossed_effectiveness_dict_of_dicts = {}
for _, row in type_effectiveness_df.iterrows():
    attacker_type = row["Attacking"]  # this is your key — a string
    effectiveness_dict = {}
    for defender_type in type_effectiveness_df.columns[1:]:  # skip 'Attacking'
        effectiveness = row[defender_type]
        effectiveness_dict[defender_type] = effectiveness
    crossed_effectiveness_dict_of_dicts[attacker_type] = effectiveness_dict

for attacker, defenders in crossed_effectiveness_dict_of_dicts.items():
    print(f"{attacker}:")
    for defender, value in defenders.items():
        print(f"  vs {defender}: {value}")
#%%
dict_of_dicts_type_final = {}
for attacker, defenders in crossed_effectiveness_dict_of_dicts.items():
    for defender, multiplier in defenders.items():
        if defender not in dict_of_dicts_type_final:
            dict_of_dicts_type_final[defender] = {}
        dict_of_dicts_type_final[defender][attacker] = multiplier

for key, value in dict_of_dicts_type_final.items():
    print(f"{key}")
    for key_aux, value_aux in value.items():
        print(
            f"  {key_aux}: {value_aux}")
#%%
