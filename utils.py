import random as r
import pandas as pd
from termcolor import colored, cprint

def rollsim(lower, upper):
    roll = 0
    for x in range(lower + upper):
        roll = r.randint(lower, upper)

    return roll

def colored_text(text, color):
    placeholder

def GM_Cell():
    placeholder

class Cell:
    def __init__(self, lower, upper, description):
        self.lower = lower
        self.upper = upper
        self.description = description

def Grammar():
    placeholder

def extract_lines(source):
    with open(source, 'r') as file:
        NAMES = file.readlines()
    for i in NAMES:
        i = i.rstrip('\r\n')
    return NAMES

class Alphabet:
    def __init__(self):
        self.alph = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
            '': 0,
        }
        '''
        for letter in alph:
            alph[letter] = {
                'a': None,
                'b': None,
                'c': None,
                'd': None,
                'e': None,
                'f': None,
                'g': None,
                'h': None,
                'i': None,
                'j': None,
                'k': None,
                'l': None,
                'm': None,
                'n': None,
                'o': None,
                'p': None,
                'q': None,
                'r': None,
                's': None,
                't': None,
                'u': None,
                'v': None,
                'w': None,
                'x': None,
                'y': None,
                'z': None,
                '': None,
            }'''

        #for x in alph:
        #    print(alph[x])

def process_name(source, markov_source):
    #markov_table = []
    markov_table = Alphabet()
    name_list = extract_lines(source)

    most_letters = 0
    total_count = 0

    for name in name_list:
        lined_name = list(name)

        for x in range(len(lined_name)):
            context_letter = lined_name[x]
            markov_table.alph[context_letter] += 1

        total_count += 1
