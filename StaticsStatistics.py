from Type import Type
from Move import Move
from Specie import Specie
import PokemonDFFinal as pdf

type_effectiveness_dict_of_dicts = pdf.dict_of_dicts_type_final

type_effectiveness_fire = type_effectiveness_dict_of_dicts['Fire']
type_effectiveness_water = type_effectiveness_dict_of_dicts['Water']
type_effectiveness_grass = type_effectiveness_dict_of_dicts['Grass']
type_effectiveness_flying = type_effectiveness_dict_of_dicts['Flying']
type_effectiveness_electric = type_effectiveness_dict_of_dicts['Electric']
type_effectiveness_poison = type_effectiveness_dict_of_dicts['Poison']
type_effectiveness_ice = type_effectiveness_dict_of_dicts['Ice']
type_effectiveness_fighting = type_effectiveness_dict_of_dicts['Fighting']
type_effectiveness_psychic = type_effectiveness_dict_of_dicts['Psychic']
type_effectiveness_ground = type_effectiveness_dict_of_dicts['Ground']
type_effectiveness_rock = type_effectiveness_dict_of_dicts['Rock']
type_effectiveness_bug = type_effectiveness_dict_of_dicts['Bug']
type_effectiveness_ghost = type_effectiveness_dict_of_dicts['Ghost']
type_effectiveness_dragon = type_effectiveness_dict_of_dicts['Dragon']
type_effectiveness_steel = type_effectiveness_dict_of_dicts['Steel']
type_effectiveness_normal = type_effectiveness_dict_of_dicts['Normal']


fire = Type("Fire", type_effectiveness_fire)
water = Type("Water", type_effectiveness_water)
grass = Type("Grass", type_effectiveness_grass)
normal = Type("Normal", type_effectiveness_normal)
rock = Type("Rock", type_effectiveness_rock)
flying = Type("Flying", type_effectiveness_flying)
electric = Type("Electric", type_effectiveness_electric)
bug = Type("Bug", type_effectiveness_bug)
steel = Type("Steel", type_effectiveness_steel)
ghost = Type("Ghost", type_effectiveness_ghost)
dragon = Type("Dragon", type_effectiveness_dragon)
psychic = Type("Psychic", type_effectiveness_psychic)
ground = Type("Ground", type_effectiveness_ground)
poison = Type("Poison", type_effectiveness_poison)
ice = Type("Ice", type_effectiveness_ice)
fighting = Type("Fighting", type_effectiveness_fighting)



ember = Move("Ember", 45, fire, "Special")
water_gun = Move("Water Gun", 40, water, "Special")
razor_leaf = Move("Razor Leaf", 45, grass, "Physical")
tackle = Move("Tackle", 40, normal, "Physical")
roll_out = Move("Roll Out", 35, rock, "Physical")
peck = Move("Peck", 35, flying,"Physical")

cyndaquil_stats = {
    "Attack": 52,
    "Special Attack": 60,
    "Defense": 49,
    "Special Defense": 50,
    "Speed": 65
}

chikorita_stats = {
    "Attack": 49,
    "Special Attack": 49,
    "Defense": 65,
    "Special Defense": 65,
    "Speed": 45
}

totodile_stats = {
    "Attack": 65,
    "Special Attack": 44,
    "Defense": 64,
    "Special Defense": 48,
    "Speed": 45
}

rattata_stats = {
    "Attack": 56,
    "Special Attack": 25,
    "Defense": 35,
    "Special Defense": 35,
    "Speed": 72
}

hoothoot_stats = {
    "Attack": 30,
    "Special Attack": 36,
    "Defense": 30,
    "Special Defense": 56,
    "Speed": 50
}

geodude_stats = {
    "Attack": 80,
    "Special Attack": 30,
    "Defense": 100,
    "Special Defense": 30,
    "Speed": 20
}

cyndaquil_hp = 39
chikorita_hp = 45
totodile_hp = 50
rattata_hp = 30
hoothoot_hp = 60
geodude_hp = 40

cyndaquil = Specie("Cyndaquil", fire, [ember, tackle], cyndaquil_hp, cyndaquil_stats, 65, starter=True)
chikorita = Specie("Chikorita", grass, [razor_leaf, tackle], hp=chikorita_hp, stats=chikorita_stats, BYE=64, starter=True)
totodile = Specie("Totodile", water, [water_gun, tackle], hp=totodile_hp, stats=totodile_stats, BYE=66, starter=True)
rattata = Specie("Rattata", normal, [tackle], hp=rattata_hp, stats=rattata_stats, BYE=57, starter=False)
geodude = Specie("Geodude", rock, [roll_out], geodude_hp, geodude_stats, 73, False)
hoothoot = Specie("HootHoot", flying, [peck], hoothoot_hp, hoothoot_stats, 58, False)


species_dict = {
    "Cyndaquil": cyndaquil,
    "Chikorita": chikorita,
    "Totodile": totodile,
    "Rattata": rattata,
    "HootHoot": hoothoot,
    "Geodude": geodude
}

moves_dict = {
    "Tackle": tackle,
    "Ember": ember,
    "Water Gun": water_gun,
    "Razor Leaf": razor_leaf,
    "Peck": peck,
    "Roll Out": roll_out
}