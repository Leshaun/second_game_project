from random import randint
from math import floor
from Templates import CharacterTemplate
from Templates import CharacterMove

player_character = CharacterTemplate("", 20, None, None, None, None)
player_character.name = input("Welcome to the arena! What is your name?\n")

move_types = ["Fire", "Electric", "Ice"]

move_damage = 0
move_used = 0
challenger_counter = 0
challenger_limit = 10

moves = [
    # Basic moves
    CharacterMove("Punch", 2, 3, None, 0),
    CharacterMove("Kick", 1, 5, None, 0),
    CharacterMove("Headbutt", 3, 4, None, 1),
    # Type moves 1
    CharacterMove("Fireball", 2, 3, move_types[0], 0),
    CharacterMove("Thunderbolt", 2, 3, move_types[1], 0),
    CharacterMove("Icicle", 2, 3, move_types[2], 0),
    # Type moves 2
    CharacterMove("Wildfire", 1, 8, move_types[0], 1),
    CharacterMove("Thunderstorm", 1, 8, move_types[1], 1),
    CharacterMove("Blizzard", 1, 8, move_types[2], 1),
    # The modhammer
    CharacterMove("MODHAMMER", 20, 20, None, 0)
]

challenger_names = [
    "Burt",
    "Harald",
    "Mr Muscle",
    "Vlad the Impaler",
    "Grom the Gruesome",
    "Steve",
    "Dudebro",
    "Yvonne the Accountant",
    "Shaka kaSenzangakhona, First King of the Zulus",
    "Robert aka \"Fierce Tyrantlord of the Underworld\"",
    "Ligma",
    "Sugma",
    "...Pegma?",
    "Ingvar Kamprad",
    "Lars Ohly",
    "Guff, of recent renown",
    "Burt 2",
    "Used Car Salesman",
    "Freddy",
    "Your Old Pal Dave",
    "Elon Musk, the Wealthiest African American in History",
    "The Pierogi Salesman",
    "Nana",
    "Pawpaw",
    "your boss",
    "Huge Jackedman"
]

print(player_character.name
      + ", huh? CLASSIC choice!\n"
        "Select a basic move:\n(a) "
      + moves[0].name + "\n(b) "
      + moves[1].name + "\n(c) "
      + moves[2].name)

while True:
    player_move1 = input()
    if player_move1 == "a":
        player_character.move1 = moves[0]
        break
    elif player_move1 == "b":
        player_character.move1 = moves[1]
        break
    elif player_move1 == "c":
        player_character.move1 = moves[2]
        break
    elif player_move1 == "modhammer":
        player_character.move1 = moves[9]
        break
    else:
        print("Please select a basic move:\n(a) "
              + moves[0].name + "\n(b) "
              + moves[1].name + "\n(c) "
              + moves[2].name)

print(player_character.move1.name
      + " it is.\n"
        "Select a type move:\n(a) "
      + moves[3].name + "\n(b) "
      + moves[4].name + "\n(c) "
      + moves[5].name)

while True:
    player_move2 = input()
    if player_move2 == "a":
        player_character.move2 = moves[3]
        break
    elif player_move2 == "b":
        player_character.move2 = moves[4]
        break
    elif player_move2 == "c":
        player_character.move2 = moves[5]
        break
    else:
        print("Please select a basic move:\n(a) "
              + moves[3].name + "\n(b) "
              + moves[4].name + "\n(c) "
              + moves[5].name)

print(player_character.move2.name
      + " it is.\n"
        "Select a second type move:\n(a) "
      + moves[6].name + "\n(b) "
      + moves[7].name + "\n(c) "
      + moves[8].name)

while True:
    player_move3 = input()
    if player_move3 == "a":
        player_character.move3 = moves[6]
        break
    elif player_move3 == "b":
        player_character.move3 = moves[7]
        break
    elif player_move3 == "c":
        player_character.move3 = moves[8]
        break
    else:
        print("Please select a basic move:\n(a) "
              + moves[6].name + "\n(b) "
              + moves[7].name + "\n(c) "
              + moves[8].name)

print(player_character.move3.name
      + " it is.\nNow entering the arena.")


def new_challenger():
    global challenger
    challenger = CharacterTemplate(challenger_names[randint(0, len(challenger_names)-1)], randint(10, 20),
                                   moves[randint(0, 2)],moves[randint(3, 5)], moves[randint(6, 8)],
                                   move_types[randint(0, 2)])
    print("Your next challenger is " + challenger.name + "!")
    if challenger.hitpoints < 14:
        print(challenger.name + " appears rather weak.")
    elif challenger.hitpoints < 18:
        print(challenger.name + " appears of moderate strength.")
    else:
        print(challenger.name + " appears rather strong.")
    while player_character.hitpoints > 0 and challenger.hitpoints > 0:

        combat_function()


def combat_function():
    move_turn = 0
    while (move_turn % 2) == 0:
        move_turn += 1

        player_turn()

    else:
        if challenger.hitpoints > 0:
            move_turn += 1

            challenger_turn()

    print("You've defeated " + challenger.name + "!\n")


def player_turn():
    move_used = input("You have " + str(player_character.hitpoints) + " hitpoints left."
                        "\nSelect your move:"
                        "\n(a) " + player_character.move1.name
                      + "\n(b) " + player_character.move2.name
                      + "\n(c) " + player_character.move3.name + "\n")
    if move_used == "a":
        move_used = player_character.move1
        move_damage = randint(move_used.min_dmg, move_used.max_dmg)
        if move_used.type == challenger.weakness:
            move_damage = move_damage * 2
            challenger.hitpoints = challenger.hitpoints - move_damage
            print("You use " + move_used.name + " for " + str(move_damage) + " damage!")
            if move_used.recoil:
                recoil_damage = floor(move_damage / 2)
                player_character.hitpoints = player_character.hitpoints - recoil_damage
                print("You took " + str(recoil_damage) + " recoil damage.")
        else:
            challenger.hitpoints = challenger.hitpoints - move_damage
            print("You use " + move_used.name + " for " + str(move_damage) + " damage!")
            if move_used.recoil:
                recoil_damage = floor(move_damage / 2)
                player_character.hitpoints = player_character.hitpoints - recoil_damage
                print("You took " + str(recoil_damage) + " recoil damage.")
    elif move_used == "b":
        move_used = player_character.move2
        move_damage = randint(move_used.min_dmg, move_used.max_dmg)
        if move_used.type == challenger.weakness:
            move_damage = move_damage * 2
            challenger.hitpoints = challenger.hitpoints - move_damage
            print("You use " + move_used.name + " for " + str(move_damage) + " damage!")
            if move_used.recoil:
                recoil_damage = floor(move_damage / 2)
                player_character.hitpoints = player_character.hitpoints - recoil_damage
                print("You took " + str(recoil_damage) + " recoil damage.")
        else:
            challenger.hitpoints = challenger.hitpoints - move_damage
            print("You use " + move_used.name + " for " + str(move_damage) + " damage!")
            if move_used.recoil:
                recoil_damage = floor(move_damage / 2)
                player_character.hitpoints = player_character.hitpoints - recoil_damage
                print("You took " + str(recoil_damage) + " recoil damage.")
    elif move_used == "c":
        move_used = player_character.move3
        move_damage = randint(move_used.min_dmg, move_used.max_dmg)
        if move_used.type == challenger.weakness:
            move_damage = move_damage * 2
            challenger.hitpoints = challenger.hitpoints - move_damage
            print("You use " + move_used.name + " for " + str(move_damage) + " damage!")
            if move_used.recoil:
                recoil_damage = floor(move_damage / 2)
                player_character.hitpoints = player_character.hitpoints - recoil_damage
                print("You took " + str(recoil_damage) + " recoil damage.")
        else:
            challenger.hitpoints = challenger.hitpoints - move_damage
            print("You use " + move_used.name + " for " + str(move_damage) + " damage!")
            if move_used.recoil:
                recoil_damage = floor(move_damage / 2)
                player_character.hitpoints = player_character.hitpoints - recoil_damage
                print("You took " + str(recoil_damage) + " recoil damage.")
    else:
        print("Invalid input. Your challenger gets a free turn!")
        #print("Select your move:"
        #      "\n(a) " + player_character.move1.name
        #      + "\n(b) " + player_character.move2.name
        #      + "\n(c) " + player_character.move3.name)
        #Make this go back and reselect


def challenger_turn():
    move_used = randint(1, 3)
    if move_used == 1:
        move_used = challenger.move1
        move_damage = randint(move_used.min_dmg, move_used.max_dmg)
        player_character.hitpoints = player_character.hitpoints - move_damage
        print(challenger.name + " used " + move_used.name + " for " + str(move_damage) + " damage!")
        if move_used.recoil:
            recoil_damage = floor(move_damage / 2)
            challenger.hitpoints = challenger.hitpoints - recoil_damage
            print(challenger.name + " took " + str(recoil_damage) + " recoil damage.")
    elif move_used == 2:
        move_used = challenger.move2
        move_damage = randint(move_used.min_dmg, move_used.max_dmg)
        player_character.hitpoints = player_character.hitpoints - move_damage
        print(challenger.name + " used " + move_used.name + " for " + str(move_damage) + " damage!")
        if move_used.recoil:
            recoil_damage = floor(move_damage / 2)
            challenger.hitpoints = challenger.hitpoints - recoil_damage
            print(challenger.name + " took " + str(recoil_damage) + " recoil damage.")
    else:
        move_used = challenger.move3
        move_damage = randint(move_used.min_dmg, move_used.max_dmg)
        player_character.hitpoints = player_character.hitpoints - move_damage
        print(challenger.name + " used " + move_used.name + " for " + str(move_damage) + " damage!")
        if move_used.recoil:
            recoil_damage = floor(move_damage / 2)
            challenger.hitpoints = challenger.hitpoints - recoil_damage
            print(challenger.name + " took " + str(recoil_damage) + " recoil damage.")


while challenger_counter < challenger_limit:
    if challenger_counter == 0:
        challenger_counter += 1
        print("You have now entered the arena where you will use your chosen moves to defeat various challengers.\n"
              "Defeat " + str(challenger_limit) + " of them and you will earn your freedom.\n"
              "Your " + str(challenger_counter) + "st challenger approaches.")

        new_challenger()

    elif challenger_counter == 1:
        player_character.hitpoints = 20
        challenger_counter += 1
        print("You have defeated your " + str(challenger_counter - 1) + "st challenger but there's no time to rest.\n"
              "Your " + str(challenger_counter) + "nd challenger approaches.")

        new_challenger()

    elif challenger_counter == 2:
        player_character.hitpoints = 20
        challenger_counter += 1
        print("You have defeated your " + str(challenger_counter - 1) + "nd challenger and look for your next foe.\n"
              "Your " + str(challenger_counter) + "rd challenger approaches.")

        new_challenger()
    else:
        while challenger_counter < challenger_limit:
            player_character.hitpoints = 20
            challenger_counter += 1
            print("You have defeated " + str(challenger_counter - 1) + "/" + str(challenger_limit) + " challengers.\n"
                  "Your " + str(challenger_counter) + "th challenger approaches.")

            new_challenger()
        print("You have defeated all the challengers in the arena and earned your freedom!")
