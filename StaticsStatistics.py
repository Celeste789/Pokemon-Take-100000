from Type import Type
import PokemonDFFinal as pdf

type_effectiveness_dict_of_dicts = pdf.dict_of_dicts_type_final
list_of_types = [type for type in type_effectiveness_dict_of_dicts.keys()]
dict_of_type_effectiveness = {}

for type_name in list_of_types:
    for name, type_it in type_effectiveness_dict_of_dicts.items():
        if name == type_name:
            dict_of_type_effectiveness[type_name] = type_it

print(dict_of_type_effectiveness['Fire'])

dict_of_type_class = {}
for type_name in list_of_types:
    type = Type(type_name, dict_of_type_effectiveness[type_name])
    dict_of_type_class[type_name] = type

print(dict_of_type_class['Fire'].type_name, dict_of_type_class['Fire'].type_effectiveness)

dict_of_dicts_species_class = pdf.dict_of_dicts_species_class




