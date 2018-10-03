import dice as d
import random as r
import tkinter as tk
import colorama
from termcolor import colored, cprint
from gm import *
from generative import *
from une import UNE
from magic import Magic
from prophecy import Prophecy
from genesysUI import GenesysUI
from tkinter import ttk
from os import system
import sys

colorama.init()

def error():
    e = sys.exc_info()
    return e

def help():
    print(colored('DICE ROLLING', 'yellow'))
    print('Type {0}. Typing {1} will roll 3 20-sided dice.'.format(colored('"<number of dice>d<number of sides>"', 'cyan'), colored('"3d20"', 'cyan')))
    print('')
    print('There are extra options such as selecting the highest and the lowest dice.')
    print('Typing {} will roll 4 20-sided dice and select the 3 highest.'.format(colored('"4d20h3"', 'cyan')))
    print('{} will roll a 100-sided dice and select the one highest dice.'.format(colored('"2d100h1"', 'cyan')))
    print('')
    print('Typing {} will roll 4 20-sided dice and select the 3 lowest.'.format(colored('"4d20v3"', 'cyan')))
    print('{} will roll a 100-sided dice and select the one lowest dice.'.format(colored('"2d100v1"', 'cyan')))
    print('')
    print(colored('GM EMULATION', 'yellow'))
    print('Type {}.'.format(colored('"fate <numbers 1-9>"', 'cyan')))
    print('The number means the likelihood an event will happen.')
    print('You may add a {} or {} sign after the number, to indicate whether the situation is in favor of the subject or not.'.format(colored('"+"', 'cyan'), colored('""', 'cyan'),))
    print('')
    print(colored('GM EMULATION: DETAILS', 'yellow'))
    print('Type {} to generate a detail.'.format(colored('"detail"', 'cyan')))
    print('Details answer a non-Yes/No question such as "What does the room look like?"')
    print('Details can be used in conjunction with Actions and Descriptions if you are finding it hard to interpret something.')
    print('')
    print(colored('GM EMULATION: ACTIONS', 'yellow'))
    print('Type {} to generate an action.'.format(colored('"action"', 'cyan')))
    print('It can be used as a supplement to details, or to provide inspiration concerning actions.')
    print('')
    print(colored('GM EMULATION: DESCRIPTION', 'yellow'))
    print('Type {} to generate a description.'.format(colored('"description" or "desc"', 'cyan')))
    print('It can be used as a supplement to details, or to provide inspiration concerning descriptions.')
    print('')
    print(colored('GM EMULATION: EVENTS', 'yellow'))
    print('Type {} to receive a random event.'.format(colored('"event"', 'cyan')))
    print('Descriptions will be provided depending on the event.')
    print('Threads will be mentioned in an event, a thread is a particular quest or plot hook.')
    print('')
    print(colored('GM EMULATION: STRENGTH COMPARISON', 'yellow'))
    print('Type {} to generate the strength for an NPC, monsters etc.'.format(colored('"strength" or "str"', 'cyan')))
    print('{} may be added as modifiers.'.format(colored('"important/weak/strong/prime"', 'cyan')))
    print('Ex: "strength important weak"')
    print('')
    print(colored('NPC GENERATION', 'yellow'))
    print('Type {} to generate an NPC.'.format(colored('"npc"', 'cyan')))
    print('')
    print(colored('NPC MOOD', 'yellow'))
    print('Type {}, where the numbers represent your reputation or relationship.'.format(colored('"npc mood <1-7>"', 'cyan')))
    print('It is also possible to type {}.'.format(colored('<hated/hostile/distrustful/neutral/peaceful/friendly/loved>', 'cyan')))
    print('')
    print(colored('NPC CONVERSATION', 'yellow'))
    print('Type {} to generate the focus of the conversation.'.format(colored('"npc convo"', 'cyan')))
    print('It is also possible to type {}.'.format(colored('<scheming/insane/friendly/hostile/inquisitive/knowing/mysterious/prejudiced>', 'cyan')))
    print('{} is an alternative where the numbers correspond to the demeanors mentioned above.'.format(colored('<1-8>', 'cyan')))
    print('')
    print(colored('PUNISHMENT', 'yellow'))
    print('Type {} to generate a punishment.'.format(colored('"punish"', 'cyan')))
    print('This command is for when a punishment cannot be decided.')
    print('')
    print(colored('PLOT TWIST', 'yellow'))
    print('Type {} to generate a plot twist.'.format(colored('"twist"', 'cyan')))
    print('Generates a plot twist, applicable to almost any quest or adventure.')
    print('')
    print(colored('GOAL GENERATION', 'yellow'))
    print('Type {} to generate a plot twist.'.format(colored('"goal"', 'cyan')))
    print('Generates a goal. May be reinterpreted into a quest or adventure, or into an objective/thread.')
    print('')
    print(colored('PROPHECY SYSTEM', 'yellow'))
    print('Type {} to receive a prophecy.'.format(colored('"prophecy"', 'cyan')))
    print('You must use your imagination to interpret it in any way you wish.')
    print('NOTE: In truth, this is a quest generator in broken English, I am improving the AI for this.')
    print('')
    print(colored('DUNGEON GENERATION', 'yellow'))
    print('Type {} to generate a dungeon.'.format(colored('"twist"', 'cyan')))
    print('Generates a description of a dungeon.')
    print('')
    print(colored('SETTLEMENT GENERATION', 'yellow'))
    print('Type {} to generate a settlement. (village/town/city)'.format(colored('"twist"', 'cyan')))
    print('Generates a settlement.')
    print('')

def commands():
    print(colored('COMMAND LIST', 'yellow'))
    print(''' <number> d <number> (OPTIONAL: h <number> / v <number>)

    ''')

system("title "+"Fiere RPG Companion v0.12 by Mikhail Joseph T. Agudo")

print('---------------------------------------')
print(colored('WELCOME TO FIERE', 'yellow'))
print('Fiere is an RPG Companion.')
print('')
print('Type {} to see a guide on the usage of commands.'.format(colored('"help"', 'cyan')))
print('Many of the functions require imagination and/or interpretation on your part.')
print('')
print(colored('SPECIAL THANKS TO:', 'yellow'))

print('''Mythic GM Emulator by Tom Pigeon
The Universal NPC Emulator by Zach Best
Ironsworn by Shawn Tomkin
NLTK Sentences: https://www.hallada.net/2017/07/11/generating-random-poems-with-python.html
Vincent Jarvina for bringing up prophecies
''')

game_master = Mythic()
une = UNE()
prophecy = Prophecy()
dungeon_gen = Dungeon()
settle_gen = Settlement()
oracle = Oracle()
magic_sys = Magic()

quit = 0
while quit == 0:
    print('-----------------------')
    player_input = input('{}: '.format(colored('Input', 'magenta')))
    print('-----------------------')
    try:
        temp = player_input
        temp += '111'
        player_input = player_input.split()
        if(player_input[0] == 'fate'):
            placeholder = 1
    except:
        player_input = 'asdawdasd'
    if(player_input[0] == "fate"):
        if(len(player_input) == 2):
            try:
                result = game_master.calculate(int(player_input[1]))
                print(result)
            except:
                print(error())
        elif(len(player_input) > 2):
            try:
                result = game_master.calculate(int(player_input[1]), player_input[2])
                print(result)
            except:
                print(error())
        else:
            print('Please type "fate <numbers 1-9">.')
            print('Ex: "fate 2" or "fate 9"')
            print(error())
    elif(player_input[0] == "detail"):
        if(len(player_input) > 1):
            try:
                result_1, result_2 = game_master.detail(player_input[1])
                print(result_1 + ' ' + result_2)
            except:
                print(error())
        else:
            try:
                result_1, result_2 = game_master.detail()
                print(result_1 + ' ' + result_2)
            except:
                print(error())
    elif(player_input[0] == "action"):
        try:
            print(game_master.action_gen())
        except:
            print(error())
    elif(player_input[0] == "description" or player_input[0] == "desc"):
        try:
            print(game_master.description_gen())
        except:
            print(error())
    elif(player_input[0] == "strength" or player_input[0] == "str"):
        if(len(player_input) == 2):
            try:
                print(game_master.strength_determine(player_input[1]))
            except:
                print(error())
        elif(len(player_input) > 2):
            try:
                print(game_master.strength_determine(player_input[1], player_input[2]))
            except:
                print(error())
        else:
            try:
                print(game_master.strength_determine())
            except:
                print(error())
    elif(player_input[0] == "prophecy"):
        if(len(player_input) > 1):
            if(player_input[1] == 'bigrams'):
                print(prophecy.test())
        else:
            try:
                print(prophecy.generate())
            except:
                print(error())
    elif(player_input[0] == "npc"):
        if(len(player_input) > 1):
            try:
                if(player_input[1] == "mood"):
                    if(len(player_input) > 2):
                        print('The NPC\'s mood is ' + une.mood(player_input[2]) + '.')
                    else:
                        print('The NPC\'s mood is ' + une.mood('') + '.')
                elif(player_input[1] == "convo"):
                    if(len(player_input) > 2):
                        print(une.convo(player_input[2]))
                    else:
                        print(une.convo(''))
            except:
                print(error())
                print('Either a bug occured or the input was wrong.')
                print('')
                print('For "npc mood", use <hated/hostile/distrustful/neutral/peaceful/friendly/loved> to describe your reputation or relationship.')
                print('It is also possible to type "npc mood <1-7>" or simply "npc mood" for a random disposition')
        else:
            print(une.generate())
    elif(player_input[0] == "genesys"):
        try:
            root = tk.Tk()
            root.title('Genesys Dice Roller')
            GenesysUI(root).pack(side="top", fill="both", expand=True)
            root.mainloop()
        except:
            print(error())
    elif(player_input[0] == "event"):
        try:
            event, event_desc, meaning = game_master.generate()
            print(colored("Event: ", 'yellow') + event)
            print(colored("Event Meaning: ", 'green') + meaning)
            print(event_desc)
        except:
            print(error())
    elif(player_input[0] == "dungeon"):
        try:
            location, purpose = dungeon_gen.generate()
            print(colored('Location: ', 'green') + location)
            print(colored('Purpose: ', 'yellow') + purpose)
        except:
            print(error())
    elif(player_input[0] == "settlement"):
        try:
            print(settle_gen.generate())
        except:
            print(error())
    elif(player_input[0] == "punish"):
        try:
            print(oracle.price())
        except:
            print(error())
    elif(player_input[0] == "twist"):
        try:
            print(oracle.plot_twist())
        except:
            print(error())
    elif(player_input[0] == "goal"):
        try:
            print(oracle.get_goal())
        except:
            print(error())
    elif(player_input[0] == "magic"):
        try:
            if(len(player_input) > 1):
                result = ''
                for i in range(len(player_input)):
                    if (i != 0):
                        result += magic_sys.translate(player_input[i]) + ' '
                print(result)
        except:
            print(error())
    elif(player_input[0] == "help"):
        help()
    elif(player_input[0] == "commands"):
        commands()
    else:
        try:
            rolls = d.roll(player_input[0])
            total = 0
            for result in rolls:
                total += result
                print(result)
            print(colored('Total:', 'yellow'),total)
        except:
            print("Either an error occured or the input was wrong.")
