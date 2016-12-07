"""
1. Have a dictionary for each type with key as attacking type and value as effectiveness (int/float)
2. Lower both so they're all the same, they match my code
3. Check if both are actual types and return error message if they're not
4. Use attack input as key and defense input as dictionary
5. Return string depending on what multiplier is (if 2 return "It's super effective!")
"""

#Step 1
normal = {
	"normal" : 1.0,
	"fighting" : 2.0,
	"flying" : 1.0,
	"poison" : 1.0,
	"ground" : 1.0,
	"rock" : 1.0,
	"bug" : 1.0,
	"ghost" : 0.0,
	"fire" : 1.0,
	"water" : 1.0,
	"grass" : 1.0,
	"electric" : 1.0,
	"psychic" : 1.0,
	"ice" : 1.0,
	"dragon" : 1.0,
}

fighting = {
	"normal" : 1.0,
	"fighting" : 1.0,
	"flying" : 2.0,
	"poison" : 1.0,
	"ground" : 1.0,
	"rock" : 0.5,
	"bug" : 0.5,
	"ghost" : 1.0,
	"fire" : 1.0,
	"water" : 1.0,
	"grass" : 1.0,
	"electric" : 1.0,
	"psychic" : 2.0,
	"ice" : 1.0,
	"dragon" : 1.0,
}

flying = {
	"normal" : 1.0,
	"fighting" : 0.5,
	"flying" : 1.0,
	"poison" : 1.0,
	"ground" : 0.0,
	"rock" : 2.0,
	"bug" : 0.5,
	"ghost" : 1.0,
	"fire" : 1.0,
	"water" : 1.0,
	"grass" : 0.5,
	"electric" : 2.0,
	"psychic" : 1.0,
	"ice" : 2.0,
	"dragon" : 1.0,
}

poison = {
	"normal" : 1.0,
	"fighting" : 0.5,
	"flying" : 1.0,
	"poison" : 0.5,
	"ground" : 2.0,
	"rock" : 1.0,
	"bug" : 2.0,
	"ghost" : 1.0,
	"fire" : 1.0,
	"water" : 1.0,
	"grass" : 0.5,
	"electric" : 1.0,
	"psychic" : 2.0,
	"ice" : 1.0,
	"dragon" : 1.0,
}

ground = {
	"normal" : 1.0,
	"fighting" : 1.0,
	"flying" : 1.0,
	"poison" : 0.5,
	"ground" : 1.0,
	"rock" : 0.5,
	"bug" : 1.0,
	"ghost" : 1.0,
	"fire" : 1.0,
	"water" : 2.0,
	"grass" : 2.0,
	"electric" : 0.0,
	"psychic" : 1.0,
	"ice" : 2.0,
	"dragon" : 1.0,
}

rock = {
	"normal" : 0.5,
	"fighting" : 2.0,
	"flying" : 0.5,
	"poison" : 0.5,
	"ground" : 2.0,
	"rock" : 1.0,
	"bug" : 1.0,
	"ghost" : 1.0,
	"fire" : 0.5,
	"water" : 2.0,
	"grass" : 2.0,
	"electric" : 1.0,
	"psychic" : 1.0,
	"ice" : 1.0,
	"dragon" : 1.0,
}

bug = {
	"normal" : 1.0,
	"fighting" : 0.5,
	"flying" : 2.0,
	"poison" : 2.0,
	"ground" : 0.5,
	"rock" : 2.0,
	"bug" : 1.0,
	"ghost" : 1.0,
	"fire" : 2.0,
	"water" : 1.0,
	"grass" : 0.5,
	"electric" : 1.0,
	"psychic" : 1.0,
	"ice" : 1.0,
	"dragon" : 1.0,
}

ghost = {
	"normal" : 0.0,
	"fighting" : 0.0,
	"flying" : 1.0,
	"poison" : 0.5,
	"ground" : 1.0,
	"rock" : 1.0,
	"bug" : 0.5,
	"ghost" : 2.0,
	"fire" : 1.0,
	"water" : 1.0,
	"grass" : 1.0,
	"electric" : 1.0,
	"psychic" : 1.0,
	"ice" : 1.0,
	"dragon" : 1.0,
}

fire = {
	"normal" : 1.0,
	"fighting" : 1.0,
	"flying" : 1.0,
	"poison" : 1.0,
	"ground" : 2.0,
	"rock" : 2.0,
	"bug" : 0.5,
	"ghost" : 1.0,
	"fire" : 0.5,
	"water" : 2.0,
	"grass" : 0.5,
	"electric" : 1.0,
	"psychic" : 1.0,
	"ice" : 1.0,
	"dragon" : 1.0,
}

water = {
	"normal" : 1.0,
	"fighting" : 1.0,
	"flying" : 1.0,
	"poison" : 1.0,
	"ground" : 1.0,
	"rock" : 1.0,
	"bug" : 1.0,
	"ghost" : 1.0,
	"fire" : 0.5,
	"water" : 0.5,
	"grass" : 2.0,
	"electric" : 2.0,
	"psychic" : 1.0,
	"ice" : 0.5,
	"dragon" : 1.0,
}

grass = {
	"normal" : 1.0,
	"fighting" : 1.0,
	"flying" : 2.0,
	"poison" : 2.0,
	"ground" : 0.5,
	"rock" : 1.0,
	"bug" : 2.0,
	"ghost" : 1.0,
	"fire" : 2.0,
	"water" : 0.5,
	"grass" : 0.5,
	"electric" : 0.5,
	"psychic" : 1.0,
	"ice" : 2.0,
	"dragon" : 1.0,
}

electric = {
	"normal" : 1.0,
	"fighting" : 1.0,
	"flying" : 0.5,
	"poison" : 1.0,
	"ground" : 2.0,
	"rock" : 1.0,
	"bug" : 1.0,
	"ghost" : 1.0,
	"fire" : 1.0,
	"water" : 1.0,
	"grass" : 1.0,
	"electric" : 0.5,
	"psychic" : 1.0,
	"ice" : 1.0,
	"dragon" : 1.0,
}

psychic = {
	"normal" : 1.0,
	"fighting" : 0.5,
	"flying" : 1.0,
	"poison" : 1.0,
	"ground" : 1.0,
	"rock" : 1.0,
	"bug" : 2.0,
	"ghost" : 0.0,
	"fire" : 1.0,
	"water" : 1.0,
	"grass" : 1.0,
	"electric" : 1.0,
	"psychic" : 0.5,
	"ice" : 1.0,
	"dragon" : 1.0,
}

ice = {
	"normal" : 1.0,
	"fighting" : 2.0,
	"flying" : 1.0,
	"poison" : 1.0,
	"ground" : 1.0,
	"rock" : 2.0,
	"bug" : 1.0,
	"ghost" : 1.0,
	"fire" : 2.0,
	"water" : 1.0,
	"grass" : 1.0,
	"electric" : 1.0,
	"psychic" : 1.0,
	"ice" : 0.5,
	"dragon" : 1.0,
}

dragon = {
	"normal" : 1.0,
	"fighting" : 1.0,
	"flying" : 1.0,
	"poison" : 1.0,
	"ground" : 1.0,
	"rock" : 1.0,
	"bug" : 1.0,
	"ghost" : 1.0,
	"fire" : 0.5,
	"water" : 0.5,
	"grass" : 0.5,
	"electric" : 0.5,
	"psychic" : 1.0,
	"ice" : 2.0,
	"dragon" : 2.0,
}

print("Welcome to the Pokemon Type Matchups Checker!")
print("This checker is based off of Generation 1 type matchups (Pokémon Red/Green/Blue/Yellow).")
print("Enter the type of the attacking move and the type of the Pokémon being attacked!")

attacking = str(input("Attacking type: "))
defending = str(input("Defending type: "))

#Step 2
attacking = attacking.lower()
defending = defending.lower()

#Step 3
types = {"normal", "fighting", "flying", "poison", "ground", "rock", "bug", "ghost", "fire", "water", "grass", "electric", "psychic", "ice", "dragon"}
if attacking not in types:
	print("Your input for attacking is not a type.")
if defending not in types:
	print("Your input for defending is not a type.")

#Step 4
types_dict = {"normal": normal, "fighting": fighting, "flying": flying, "poison":poison, "ground":ground, "rock":rock, "bug":bug, "ghost":ghost, "fire":fire, "water":water, "grass":grass, "electric":electric, "psychic":psychic, "ice":ice, "dragon":dragon}

if types_dict[defending].get(attacking) == 2.0:
	print("It's super effective!")
elif types_dict[defending].get(attacking) == 1.0:
	print("Normal attack")
elif types_dict[defending].get(attacking) == 0.5:
	print("It's not very effective...")
elif types_dict[defending].get(attacking) == 0.0:
	print("It doesn't effect the Pokémon.")
