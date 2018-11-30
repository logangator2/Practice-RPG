
import random
import math
import time

import Overworld_main
import Item
import Character

def battle(player_team, enemy_list):
    """
    Runs main battle simulation for any encounter. 
    Effects:
        Stats for characters change depending on outcome of battle.
    Returns:
        True: if players succeeded
        False: if players were knocked out
    """
    check = 1
    n_enemies = len(enemy_list)
    og_enemies = []

    for e in enemy_list:
        og_enemies.append(e)

    if n_enemies == 1:
        print("Oh no! An enemy has appeared!")
    else:
        print("Oh no! Enemies have appeared!")

    # main battle while loop
    while check != 0:
        # check if all enemies have been defeated
        if len(enemy_list) == 0:
            print("You win! All enemies have been defeated.")
            value = 0

            # calc experience
            for e in og_enemies:
                value += e.calc_experience(player_team)
            value = math.ceil(value / len(player_team))

            # deal experience
            for p in player_team:
                p.gain_xp(value)
            return True

        # display teams
        print("\nEnemies:")
        for e in enemy_list:   
            e.information()
        print("\nAllies:")
        for p in player_team:
            print("Name: {}, Health: {}/{}".format(p.name, p.c_health, p.health))
        print()
            
        # request user input
        if player_team[0].level == 1:
            print("There are different commands that you can use in battle.")
        for p in player_team:
            p_in = input("What would you like {} to do? ".format(p.name))
            check = battle_command_checker(p_in.lower(), p, enemy_list)

        # FIXME: All code in this function below this comment needs to be changed when there len(player_team) > 1
        tmp_player = player_team[0]

        # have enemies attack if player entered in valid input
        if check == 3:
            for e in enemy_list:
                e.normal_attack(tmp_player) # ADD: add random moves for diff enemies
                time.sleep(1.5)
                if tmp_player.knockout:
                    print("{} blacked out!".format(tmp_player)) # FIXME: change to 'your team' later on - could check w/ if statement
                    return False
                if tmp_player.dead:
                    print("{} died!".format(tmp_player))
                    return False
    return False

def battle_command_checker(command, player, enemy_list):
    """
    Checks that player input is valid and executes command if so.
    Args:
        command: input from player
        player: character that user chose to execute command with
        enemy_list: list of enemies
    Effects:
        If player input is valid, executes command
    Returns:
        0 = Quit: If the player chose to quit, it quits the program
        1 = Help: If the player chose to display help, quit, or entered an invalid command, the game continues
        2 = All Clear: If all enemies have been defeated, sends 'all enemies defeated' signal to main
        3 = Valid Command: If player's action was completely valid and not help or quit
    """
    if len(enemy_list) == 0:
        return 2

    elif (command == "help") or (command == "h"):
        print("You may enter in any of these commands: fight, items, defend, status, or run")
        print("You may use the first letter of each command instead.")
        return 1

    elif (command == "defend") or (command == "d"):
        print()
        player.defend()
        print()
        return 3

    # secret testing function
    elif (command == "ult"):
        player.c_health = 99999
        player.strength = 99999
        print("\nult enabled")
        return 1

    # display player status
    elif (command == "status") or (command == "s"):
        player.information()
        return 1

    elif (command == "items") or (command == "i"):
        if len(player.backpack) != 0:
            for item in player.backpack:
                print(item.name)
            selection = input("Which item would you like to use? ")
            counter = 0
            for item in player.backpack:
                if selection.lower() == item.name.lower():
                    item.use(player)
                    player.backpack.remove(item)
                    break
                elif (selection.lower() != item.name.lower()) and (player.backpack[counter] == player.backpack[-1]):
                    print("Invalid selection! Please try again.")
                    return 1
                counter += 1
            return 3
        else:
            print("You have no items! Please try again.")
            return 1

    elif (command == "fight") or (command == "f"):
        target = input("Which enemy would you like to attack? ")

        # check for valid target
        for e in enemy_list:
            if e.name.lower() == target.lower():
                player.normal_attack(e)
                print()
                time.sleep(1.5)
                if e.dead:
                    enemy_list.remove(e)
                return 3

        # making sure enemy_num is an integer before testing logic
        try:
            enemy_num = int(target)
        except:
            print("Invalid target! Try again.")
            return 1
        
        if (enemy_num > 0) and (enemy_num <= len(enemy_list)):
            player.normal_attack(enemy_list[enemy_num - 1])
            print()
            time.sleep(1.5)
            if enemy_list[enemy_num - 1].dead:
                enemy_list.remove(enemy_list[enemy_num - 1])
            return 3

        print("Invalid target! Try again.")
        return 1

    elif (command == "run") or (command == "r"):
        print("You run!")
        return 0

    else:
        print("Invalid command! Please retry.")
        return 1

def slime_generator():
    """
    Generates a random number of slime enemies
    Returns:
        enemy_list: a list of enemy slimes
    """
    enemy_list = []
    n_slimes = random.randint(1, 4)

    for n in range(n_slimes):
        slime = Character.Enemy("Slime {}".format(n + 1), 5, "weak")
        enemy_list.append(slime)
    return enemy_list        

def event_picker(player_team):
    """
    Randomly picks an event 
    Args:
        player_team: list of player Character objects
    Effects:
        calls one of the specified events events
    """
    time.sleep(1.5) # For UI
    # NOTE: May want to just return a randomized selection of possible events so events aren't repeated

    rn = random.randint(1, 8)

    if rn == 1:
        slime_event(player_team)
    elif rn == 2:
        baby_event(player_team)
    elif rn == 3:
        god_event(player_team)
    elif rn == 4:
        print("\n{} has fallen in a hole.".format(player_team[0]))
        player_team[0].damage(5)
    elif rn == 5:
        print("\nYou have a pleasant stroll along the road. The road is quiet.")
    elif rn == 6:
        g = random.randint(1, 100)
        player_team[0].gold += g
        print("\nYou found {} gold on the road!".format(g))
    elif rn == 7:
        goblin_event(player_team)
    elif rn == 8:
        armor_event(player_team)
    
    # Ideas
        # gain an ally
        # arrive in a town
        # bandits
        # two groups are fighting and you have to choose between the two
        # troll asks you a riddle and if you don't know the answer you fight

def chest(player_team):
    """
    Generates a chest.
    """
    c = random.randint(1, 2)
    #c = 1 # FIXME: delete when armor and weapons implemented
    if c == 0:
        print("Not here yet.")
    # armor
    elif c == 1: # FIXME: names are weird
        a_types = ["Chain", "Plate"]
        a_names = ["helmet", "torso", "leggings", "boots"]

        t = random.choice(a_types)
        p = random.choice(a_names)

        item = Item.Armor("{} {}".format(t, p.capitalize()), "A sturdy piece of armor.", t, p, player_team)
    # potion    
    elif c == 2:
        potions = ["Minor", "Normal", "Major"]
        t = random.choice(potions)
        item = Item.Healing_Potion("{} Healing Potion".format(t), "Heals a character.", t)

    g = random.randint(100, 200)
    print("You found {} gold!".format(g))
    player_team[0].gold += g
    print("You found {}!".format(item.name))
    player_team[0].backpack.append(item)
    return

def boss_event(player_team):
    """
    Runs the boss event. Spawns boss.
    """
    enemy_list = [Character.Enemy("Dragon", 65, "boss")] # FIXME: make modular and add more bosses
    if battle(player_team, enemy_list):
        player_team[0].gold += 1000
        print("\nYou've saved the surrounding area! You've earned {} gold.".format(1000))
    else:
        if not Overworld_main.still_alive(player_team):
            print("\nThe dragon has burnt you and the surrounding area to ashes.")
        else:
            print("\nYou narrowly escape the dragon's flames, but the surrounding area has been burned to the ground.")
    return

def armor_event(player_team):
    """
    Runs the armor event. Generates a piece of low-level armor.
    """
    print("You see a piece of armor lying on the ground. You pick it up.")
    r = random.randint(0, 3)
    if r == 0:
        item = Item.Armor("Leather Helmet", "A leather helmet to prevent light injuries.", "Leather", "helmet", player_team)
    elif r == 1:
        item = Item.Armor("Leather Chest Piece", "Leather armor to prevent light injuries.", "Leather", "torso", player_team)
    elif r == 2:
        item = Item.Armor("Leather Pants", "Essentially leggings.", "Leather", "leggings", player_team)
    elif r == 3:
        item = Item.Armor("Leather Boots", "Stylish leather boots. Just do it.", "Leather", "boots", player_team)

    player_team[0].backpack.append(item)
    return

def goblin_event(player_team):
    """
    Runs the goblin event.
    """
    enemy_list = []
    while (True):
        answer = (input("\nYou hear voices in the forest to your left. Would you like to investigate? Y/N ")).lower()
        if (answer == "yes") or (answer == "y"):
            print("\nGoblins are arguing over a chest, but stop and draw their weapons when they see you.")
            for n in range((random.randint(2,4))):
                goblin = Character.Enemy("Goblin {}".format(n + 1), 10, "annoying")
                enemy_list.append(goblin)
            if battle(player_team, enemy_list):
                print("\nYou found a chest!")
                chest(player_team)
            break
        elif (answer == "no") or (answer == "n"):
            print("\nIt's probably nothing. You're fine, right?")
            break
        else:
            print("\nInvalid command! Try again.")
    return

def baby_event(player_team):
    """
    Runs the baby animal event
    Args:
        player_team: list of player Character objs
    """
    enemy_list = []
    check = True
    while (check):
        answer = (input("\nYou see a hurt baby animal on the road. Will you try and help it? Y/N ")).lower()
        if (answer == "yes") or (answer == "y"):
            print("\nThe animal was crying for its mother! The beast appears to defend its young.")
            enemy_list.append(Character.Enemy("Momma Bear", 20, "average"))
            battle(player_team, enemy_list)
            check = False
            break
        elif (answer == "no") or (answer == "n"):
            print("\nYou leave the animal to die. You're a terrible person.")
            check = False
            break
        else:
            print("\nInvalid command! Try again.")
    return

def god_event(player_team):
    """
    Runs forgiving god's event, also used to heal up new players.
    Effects:
        Heals up 15% of health of each p in player_team
    """
    print("\nYou have wandered into a forgiving god's terrain.")
    for p in player_team:
        value = math.ceil(0.15 * p.health)
        p.healing(value)

def best_god_event(player_team):
    """
    Runs forgiving god's event, also used to heal up new players.
    Effects:
        Heals up 15% of healthof each p in player_team
    """
    print("\nYou have wandered into a forgiving god's terrain.")
    for p in player_team:
        p.healing(p.health)

def slime_event(player_team):
    """
    Runs slime event
    Args:
        player_team: list of player Character objects
    """

    enemy_list = slime_generator() # generate slime enemies
    battle(player_team, enemy_list)
    return

def easy_slime_event(player_team):
    """
    Runs easy slime event for new players
    Args:
        player_team: list of player Character objects
    """

    # inconsistent slime health done on purpose for easy slime event
    enemy_list = [Character.Enemy("Slime 1", 10, "weak"), Character.Enemy("Slime 2", 10, "weak")]
    battle(player_team, enemy_list)
    return
