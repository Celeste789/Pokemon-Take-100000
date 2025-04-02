from Type import Type
from Move import Move
from Specie import Specie

type_effectiveness_fire = {
    "Water": 2,
    "Fire": 1 / 2,
    "Grass": 1 / 2,
    "Normal": 1,
    "Rock": 2,
    "Flying": 1
}

type_effectiveness_water = {
    "Water": 1 / 2,
    "Fire": 1 / 2,
    "Grass": 2,
    "Normal": 1,
    "Rock": 1,
    "Flying": 1
}

type_effectiveness_grass = {
    "Water": 1 / 2,
    "Fire": 2,
    "Grass": 1 / 2,
    "Normal": 1,
    "Rock": 1,
    "Flying": 2
}

type_effectiveness_normal = {
    "Water": 1,
    "Fire": 1,
    "Grass": 1,
    "Normal": 1,
    "Flying": 1,
    "Rock": 1
}

type_effectiveness_flying = {
    "Water": 1,
    "Fire": 1,
    "Grass": 1/2,
    "Rock": 2,
    "Flying": 1/2,
    "Normal": 1

}

type_effectiveness_rock = {
    "Water": 2,
    "Fire": 1,
    "Grass": 2,
    "Normal": 1/2,
    "Flying": 1/2,
}

fire = Type("Fire", type_effectiveness_fire)
water = Type("Water", type_effectiveness_water)
grass = Type("Grass", type_effectiveness_grass)
normal = Type("Normal", type_effectiveness_normal)
rock = Type("Rock", type_effectiveness_rock)
flying = Type("Flying", type_effectiveness_flying)

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