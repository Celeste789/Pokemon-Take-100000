from Type import Type
from Move import Move
from Specie import Specie

type_effectiveness_fire = {
    "Water": 2,
    "Fire": 1 / 2,
    "Grass": 1 / 2,
    "Normal": 1
}

type_effectiveness_water = {
    "Water": 1 / 2,
    "Fire": 1 / 2,
    "Grass": 2,
    "Normal": 1
}

type_effectiveness_grass = {
    "Water": 1 / 2,
    "Fire": 2,
    "Grass": 1 / 2,
    "Normal": 1
}

type_effectiveness_normal = {
    "Water": 1,
    "Fire": 1,
    "Grass": 1,
    "Normal": 1
}

fire = Type("Fire", type_effectiveness_fire)
water = Type("Water", type_effectiveness_water)
grass = Type("Grass", type_effectiveness_grass)
normal = Type("Normal", type_effectiveness_normal)

ember = Move("Ember", 45, fire, "Special")
water_gun = Move("Water Gun", 40, water, "Special")
razor_leaf = Move("Razor Leaf", 45, grass, "Physical")
tackle = Move("Tackle", 40, normal, "Physical")

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

cyndaquil_hp = 39
chikorita_hp = 45
totodile_hp = 50
rattata_hp = 30

cyndaquil = Specie("Cyndaquil", fire, [ember, tackle], cyndaquil_hp, cyndaquil_stats, 65)
chikorita = Specie("Chikorita", grass, [razor_leaf, tackle], hp=chikorita_hp, stats=chikorita_stats, BYE=64)
totodile = Specie("Totodile", water, [water_gun, tackle], hp=totodile_hp, stats=totodile_stats, BYE=66)
rattata = Specie("Rattata", normal, [tackle], hp=rattata_hp, stats=rattata_stats, BYE=57)