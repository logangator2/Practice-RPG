
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

    # opening messages
    print()
    print("Welcome, {}. You have {} health. Type 'Help' for commands.".format(player.name, player.c_health))
    print()

    event_counter = 0

    while (check):
        if event_counter == 10:
            check = False
        else:

            # begin event
            # FIXME: Make more than one event - maybe an event picker
            # FIXME: Allow player to quit before event is picked
            Events.slime_event(player)
            event_counter += 1


if __name__ == '__main__':
    main()