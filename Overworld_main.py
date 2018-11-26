
import random
import math
import time

import Item
import Character
import Events

def still_alive(player_team):
    """
    Checks if player team is still alive.
    Args:
        player_team: list of player objects
    Returns:
        True if players are still alive
        False if players are all dead
    """
    all_dead = True
    for p in player_team:
        if p.dead != True:
            all_dead = False
            return True

    if all_dead:
        print("\nYour adventure is over.\n")
        return False

def main():
    """
    Main game loop of the Practice RPG
    """

    # loop to select whether to continue from old save
    while (True):
        cmd = input("Please select an option: 1: New Game, 2: Continue Game, 3: Quit. ")

        if cmd == "1":
            # create player character
            p_name = input("Enter your name: ")
            player = Character.Ally(p_name, 20, 1, 0, 1, 0, 10)
            player_team = [player]

            # opening message
            print("\nWelcome, {}. You have {} health.".format(player.name, player.c_health))

            event_counter = 0
            break

        if cmd == "2":
            # open file
            # print("\nWelcome back!")
            """
            Need player object list, event_counter, 
            """
            print("Sorry! Save files aren't here yet!")
            # FIXME: add break when you put in save files

        if cmd == "3":
            print("\nQuitting...")
            return
        else:
            print("\nInvalid command! Try again.")

    # set loop checker back to normal
    check = True
    # set/reset rest limit
    rest_count = 3
    rest_test = True

    print("\nYou are walking along a road.")

    # main game loop
    while (check):
            
        # check if players are still alive
        check = still_alive(player_team)
        if check == False:
            break

        # check if players aren't all knocked out, if one is, heal
        all_ko = True
        for p in player_team:
            if p.knockout != True:
                all_ko = False
            else:
                print() # formatting
                p.healing(1)
                print("\n{} has awakened!".format(p.name))

        # if all players are knocked out, have them lose 15% of their average gold each
        lost_gold = 0
        if all_ko:
            for p in player_team:
                lost_gold += math.floor(0.15 * p.gold)
            for p in player_team:
                p.gold -= math.floor(lost_gold / len(player_team))
            print("\nYour adventurers wake up, but have lost {} gold.".format(lost_gold))
            
        # check if enough events have occurred to reset the rest counter
        if ((event_counter % 10) == 0) and (rest_test != True):
            print("\nYou're tired and able to rest again.")
            rest_count = 3
            rest_test = True # prevents repeat information

        # continue adventure
        else:
            # ask for player input
            command = input("\nWhat would you like to do? Type 'Help' for commands. ")
            command = command.lower()
                       
            # display possible commands
            if (command == "help") or (command == "h"):
                print("\nYou may enter in any of these commands: move, rest, status, items, or quit")
                print("You may use the first letter of each command instead.")
       
            # secret testing function
            elif (command == "ult"):
                for p in player_team:
                    p.c_health = 99999
                    p.strength = 99999
                    #p.defense = 99999
                    # FIXME: add speed modifier 
                print("\nult enabled")

            # display player team status
            elif (command == "status") or (command == "s"):
                for p in player_team:
                    p.information()
                print() # formatting

            elif (command == "items") or (command == "i"):
                if len(player_team[0].backpack) != 0:
                    Item.manage(player_team[0])
                else:
                    print("\nYou have no items!")

            # trigger event
            elif (command == "move") or (command == "m"):
                print("\nYou move along the road.")

                # check if enough events have occurred
                if event_counter == 30:
                    Events.boss_event(player_team) # Final event
                    print("\nYou've had quite an adventure!\n")
                    check = False
                    break

                # testing area
                #Events.armor_event(player_team)

                # new player road
                if event_counter == 0:
                    time.sleep(1.5)
                    Events.easy_slime_event(player_team)
                    event_counter += 1
                elif event_counter == 1:
                    Events.best_god_event(player_team)
                    event_counter += 1

                # normal encounters
                else:
                    Events.event_picker(player_team)
                    event_counter += 1
                    rest_test = False

            # resting event
            elif (command == "rest") or (command == "r"):
                if rest_count <= 0:
                    print("\nYou're not tired!")
                else:
                    rest_count -= 1
                    print("\nYou take a rest. You have {} rests remaining.".format(rest_count))
                    for p in player_team:
                        p.healing(math.ceil((random.randint(10, 60)/100) * p.health))
                    event_counter += 1
                       
            # quit game
            elif(command == "quit") or (command == "q"):
                # FIXME: add save option before quitting
                print("\nQuitting...")
                break
            else:
                print("\nInvalid command! Please retry.")
            time.sleep(1.5)
    return

if __name__ == '__main__':
    main()
