
import random

import Character
import Events

def main():
    # main loop checker
    check = True

    # create player character
    p_name = input("Enter your name: ")
    player = Character.Character(p_name, 20)
    player_team = [player]

    # opening message
    print("\nWelcome, {}. You have {} health.".format(player.name, player.c_health))

    event_counter = 0

    while (check):
        # check if enough events have occurred
        if event_counter == 10:
            check = False
            break
        # check if players are still alive
        all_dead = True
        for p in player_team:
            if p.dead != True:
                all_dead = False
        if all_dead:
            print("\nYour adventure is over.\n")
            check = False
            break
        # continue adventure
        else:
            print("\nYou are walking along a road.\n")
            # ask for player input
            command = input("What would you like to do? Type 'Help' for commands. ")
            command = command.lower()
            # display possible commands
            if (command == "help") or (command == "h"):
                print("\nYou may enter in any of these commands: move, quit")
                print("You may use the first letter of each command instead.")
            # trigger event
            elif (command == "move") or (command == "m"):
                print("\nYou move along the road.")
                #Events.event_picker(player_team)
                Events.event_picker(player_team)
                event_counter += 1
            # quit game
            elif(command == "quit") or (command == "q"):
                check = False
                break
            else:
                print("\nInvalid command! Please retry.")
    return


if __name__ == '__main__':
    main()
