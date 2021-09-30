#!/bin/python3

# example of user-input loop


# program example: 

# Dungeon Crawler
# Welcome to DUNGEON CRAWLER
# created by [insert your name]


#You are outside the dungeon.
# What do you want to do?
# 1) Kick Door Down
# 2) Fight Monsters
# 3) Run Away
# 4) End Game

# Your choice: 3 [enter]
# [screen should clear]

# your father must have been right, you aren't cut out for adventure.

# You are outside the dungeon.
# What do you want to do?
# 1) Kick Door Down
# 2) Fight Monsters
# 3) Run Away
# 4) End Game
# Your choice: 1 [enter]
# [screen should clear]

# You kick in the door, A monster is here.

# You are in dungeon room 1. A monster blocks your path.
# What do you want to do?
# 1) Kick Door Down
# 2) Fight Monsters
# 3) Run Away
# 4) End Game
# Your choice: 1 [enter]
# [screen clear]

# You cant move forward until you kill the monster.

# You are in dungeon room 1. A monster blocks your path.
# What do you want to do?
# 1) Kick Door Down
# 2) Fight Monsters
# 3) Run Away
# 4) End Game
# Your choice: 2 [enter]
# [screen clear]

# you kill the monster!
# You are in dungeon room 1. A monster is dead at your feet.
# What do you want to do?
# 1) Kick Door Down
# 2) Fight Monsters
# 3) Run Away
# 4) End Game

# Your choice: 2 [enter]
# [screen clear]

# The monster is already dead. You wrestle with your inner demons.
# You are in dungeon room 1. A monster is dead at your feet.
# What do you want to do?
# 1) Kick Door Down
# 2) Fight Monsters
# 3) Run Away
# 4) End Game

# Your choice: 1 [enter]
# [screen clear]

# You are in dungeon room 2. A monster blocks your path.
# What do you want to do?
# 1) Kick Door Down
# 2) Fight Monsters
# 3) Run Away
# 4) End Game

# Your choice: 3 [enter]
# [screen clear]

# You fled the monster like a coward and returned to camp for the night. You return the next day and are outside the dungeon.

# What do you want to do?
# 1) Kick Door Down
# 2) Fight Monsters
# 3) Run Away
# 4) End Game

# Your choice: 4 [enter]
# [screen clear]

# Okay good bye!
# [program loop ends]

def main():
    print()
    print('Welcome to DUNGEON CRAWLER')
    print('created by: Voidsec')
    print()
    # set dungeon_outside loop to true
    dungeon_outside = True
    while dungeon_outside:
        print()    
        print('\nYou are outside the dungeon, what do you want to do?')
        disp_choices()
        usr_choice = int(input('Make your choice: '))
        if usr_choice == 1:
            dungeon_outside = False
            enter_dungeon(usr_choice)
        elif usr_choice == 2:
            print('\nThere are no monsters in the area.')
        elif usr_choice == 3:
            print('\nYou father must have been right, you are not cut out for adventure.')
        else:
            print('\nOkay good bye!')
            exit()

def disp_choices():
    print()
    print('What do you want to do?')
    print()
    print('1) Kick Door Down')
    print('2) Fight Monsters')
    print('3) Run Away')
    print('4) End Game')

# def gen_dungeon():
#     # status
#     active = True
#     # enter loop
#    while active:
#        enter_dungeon()

# #def gen_monster():
#     active = True
#     #
#     while active:
#         print('You are in dungeon room 1. A monster blocks your path.')
#         disp_choices()
#         usr_choice = int(input('Make your choice: '))
#         if usr_choice == 1:
#             print('You cant move forward until you kill the monster.')
#         elif usr_choice == 2:
#             print('You kill the monster!')
#             print('You are in dungeon room 1. A monster is dead at your feet.')
#             disp_choices()
#             if usr_choice == 2:
#                 print('The monster is already dead. You wrestle with your inner demons.')

def enter_dungeon(usr_choice):
    #gen_dungeon()
    # set game to true
    game_active = True
    while game_active:
        if usr_choice == 1:
            dungeon1 = True
            print()
            print('You kick in the door, A monster is here.')
            print()
            while dungeon1:
                print('You are in dungeon room 1. A monster blocks your path.')
                disp_choices()
                usr_choice = int(input('Make your choice: '))
                if usr_choice == 1:
                    print('You cant move forward until you kill the monster.')
                elif usr_choice == 2:
                    print('You kill the monster!')
                    print('You are in dungeon room 1. A monster is dead at your feet.')
                    disp_choices()
                    if usr_choice == 2:
                        print('The monster is already dead. You wrestle with your inner demons.')
                    



#execute main
main()