
import random

import Character
import Enemy
import Events

def main():
    # main loop checker
    check = True

    # create player character
    p_name = input("Enter your name: ")
    player = Character.Character(p_name, 20)

    # opening message
    print("\nWelcome, {}. You have {} health.".format(player.name, player.c_health))

    event_counter = 0

    while (check):
        if event_counter == 10:
            check = False
            break
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
                # FIXME: Make more than one event - maybe an event picker
                Events.slime_event(player)
                event_counter += 1
            # quit game
            elif(command == "quit") or (command == "q"):
                check = False
                break


if __name__ == '__main__':
    main()