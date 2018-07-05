import random as r
import re
from gm import Cell
from termcolor import colored, cprint

with open('data/npcnames.ni', 'r') as file:
    NAMES = file.readlines()
for i in NAMES:
    i = i.rstrip('\r\n')

class UNECell():
    def __init__(self, lower, upper, description):
        self.lower = lower
        self.upper = upper
        self.description = description

class Mdict():
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return r.choice(l)

class MName():
    """
    A name from a Markov chain
    """
    def __init__(self, chainlen = 2):
        """
        Building the dictionary
        """
        if(chainlen > 10 or chainlen < 1):
            print ("Chain length must be between 1 and 10, inclusive")
            sys.exit(0)

        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen

        for l in NAMES:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")

    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()

class UNE():
    def __init__(self):
        self.npc_modifier = []
        self.npc_noun = []
        self.motivation_verb = []
        self.motivation_noun = []

        with open("data/une_npcmod.ni", 'r') as file:
            content = file.readlines()
        for i in content:
            self.npc_modifier.append(i.rstrip('\r\n'))

        with open("data/une_npcnoun.ni", 'r') as file:
            content = file.readlines()
        for i in content:
            self.npc_noun.append(i.rstrip('\r\n'))

        with open("data/une_motverb.ni", 'r') as file:
            content = file.readlines()
        for i in content:
            self.motivation_verb.append(i.rstrip('\r\n'))

        with open("data/une_motnoun.ni", 'r') as file:
            content = file.readlines()
        for i in content:
            self.motivation_noun.append(i.rstrip('\r\n'))

        self.relationship = {
            'hated': [Cell(1, None, 15), Cell(16, None, 30), Cell(31, None, 69), Cell(70, None, 84), Cell(85, None, 94), Cell(95, None, 99), Cell(100, None, 100)],
            'hostile': [Cell(1, None, 11), Cell(12, None, 24), Cell(25, None, 61), Cell(62, None, 81), Cell(82, None, 93), Cell(94, None, 98), Cell(99, None, 100)],
            'distrustful': [Cell(1, None, 7), Cell(8, None, 18), Cell(19, None, 46), Cell(47, None, 76), Cell(77, None, 90), Cell(91, None, 97), Cell(98, None, 100)],
            'neutral': [Cell(1, None, 5), Cell(6, None, 15), Cell(16, None, 30), Cell(31, None, 60), Cell(61, None, 85), Cell(86, None, 95), Cell(96, None, 100)],
            'peaceful': [Cell(1, None, 3), Cell(4, None, 11), Cell(12, None, 25), Cell(26, None, 55), Cell(56, None, 82), Cell(83, None, 93), Cell(94, None, 100)],
            'friendly': [Cell(1, None, 2), Cell(3, None, 8), Cell(9, None, 20), Cell(21, None, 40), Cell(41, None, 76), Cell(77, None, 89), Cell(90, None, 100)],
            'loved': [Cell(1, None, 1), Cell(2, None, 6), Cell(7, None, 16), Cell(17, None, 31), Cell(32, None, 70), Cell(71, None, 85), Cell(86, None, 100)],
        }

        self.bearing = {
            'scheming': [UNECell(1, 10, 'intent'), UNECell(11, 20, 'bargain'),
            UNECell(21, 30, 'means'), UNECell(31, 40, 'proposition'),
            UNECell(41, 50, 'plan'), UNECell(51, 60, 'compromise'),
            UNECell(61, 70, 'agenda'), UNECell(71, 80, 'arrangement'),
            UNECell(81, 90, 'negotiation'), UNECell(91, 100, 'plot')],
            'insane': [UNECell(1, 10, 'madness'), UNECell(11, 20, 'fear'),
            UNECell(21, 30, 'accident'), UNECell(31, 40, 'chaos'),
            UNECell(41, 50, 'idiocy'), UNECell(51, 60, 'illusion'),
            UNECell(61, 70, 'turmoil'), UNECell(71, 80, 'confusion'),
            UNECell(81, 90, 'facade'), UNECell(91, 100, 'bewilderment')],
            'friendly': [UNECell(1, 10, 'alliance'), UNECell(11, 20, 'comfort'),
            UNECell(21, 30, 'gratitude'), UNECell(31, 40, 'shelter'),
            UNECell(41, 50, 'happiness'), UNECell(51, 60, 'support'),
            UNECell(61, 70, 'promise'), UNECell(71, 80, 'delight'),
            UNECell(81, 90, 'aid'), UNECell(91, 100, 'celebration')],
            'hostile': [UNECell(1, 10, 'death'), UNECell(11, 20, 'capture'),
            UNECell(21, 30, 'judgement'), UNECell(31, 40, 'combat'),
            UNECell(41, 50, 'surrender'), UNECell(51, 60, 'rage'),
            UNECell(61, 70, 'resentment'), UNECell(71, 80, 'submission'),
            UNECell(81, 90, 'injury'), UNECell(91, 100, 'destruction')],
            'inquisitive': [UNECell(1, 10, 'questions'), UNECell(11, 20, 'investigation'),
            UNECell(21, 30, 'interest'), UNECell(31, 40, 'demand'),
            UNECell(41, 50, 'suspicion'), UNECell(51, 60, 'request'),
            UNECell(61, 70, 'curiosity'), UNECell(71, 80, 'skepticism'),
            UNECell(81, 90, 'command'), UNECell(91, 100, 'petition')],
            'knowing': [UNECell(1, 10, 'report'), UNECell(11, 20, 'effects'),
            UNECell(21, 30, 'examination'), UNECell(31, 40, 'records'),
            UNECell(41, 50, 'account'), UNECell(51, 60, 'news'),
            UNECell(61, 70, 'history'), UNECell(71, 80, 'telling'),
            UNECell(81, 90, 'discourse'), UNECell(91, 100, 'speech')],
            'mysterious': [UNECell(1, 10, 'rumor'), UNECell(11, 20, 'uncertainty'),
            UNECell(21, 30, 'secrets'), UNECell(31, 40, 'misdirection'),
            UNECell(41, 50, 'whispers'), UNECell(51, 60, 'lies'),
            UNECell(61, 70, 'shadows'), UNECell(71, 80, 'enigma'),
            UNECell(81, 90, 'obscurity'), UNECell(91, 100, 'conundrum')],
            'prejudiced': [UNECell(1, 10, 'reputation'), UNECell(11, 20, 'doubt'),
            UNECell(21, 30, 'bias'), UNECell(31, 40, 'dislike'),
            UNECell(41, 50, 'partiality'), UNECell(51, 60, 'belief'),
            UNECell(61, 70, 'view'), UNECell(71, 80, 'discrimination'),
            UNECell(81, 90, 'assessment'), UNECell(91, 100, 'difference')],
        }

        self.focus = [UNECell(1, 3, 'the current scene'), UNECell(4, 6, 'the last story'),
            UNECell(7, 9, 'equipment'), UNECell(10, 12, 'parents'), UNECell(13, 15, 'history'),
            UNECell(16, 18, 'retainers'), UNECell(19, 21, 'wealth'), UNECell(22, 24, 'relics'),
            UNECell(25, 27, 'the last action'), UNECell(28, 30, 'skills'), UNECell(31, 33, 'superiors'),
            UNECell(34, 36, 'fame'), UNECell(37, 39, 'the campaign'), UNECell(40, 42, 'future action'),
            UNECell(43, 45, 'friends'), UNECell(46, 48, 'allies'), UNECell(49, 51, 'the last scene'),
            UNECell(52, 54, 'contracts'), UNECell(55, 57, 'flaws'), UNECell(58, 60, 'the antagonist'),
            UNECell(61, 63, 'rewards'), UNECell(64, 66, 'experience'), UNECell(67, 69, 'knowledge'),
            UNECell(70, 72, 'the recent scene'), UNECell(73, 75, 'community'), UNECell(76, 78, 'treasure'),
            UNECell(79, 81, 'the character'), UNECell(82, 84, 'the current story'), UNECell(85, 87, 'family'),
            UNECell(88, 90, 'power'), UNECell(91, 93, 'weapons'), UNECell(94, 96, 'the previous scene'),
            UNECell(97, 100, 'the enemy ')
        ]

    def npcmod(self):
        result = self.npc_modifier[r.randint(0, len(self.npc_modifier) - 1)]
        return colored(result, 'green')

    def npcnoun(self):
        result = self.npc_noun[r.randint(0, len(self.npc_noun) - 1)]
        return colored(result, 'green')

    def motverb(self):
        result = self.motivation_verb[r.randint(0, len(self.motivation_verb) - 1)]
        unpack = list(result)
        if(unpack[len(unpack) - 1] == 'h'):
            result += 'es'
        elif(unpack[len(unpack) - 1] == 'y'):
            unpack[len(unpack) - 1] = 'ies'
            result = ''.join(unpack)
        elif(unpack[len(unpack) - 1] != 's'):
            result += 's'
        return colored(result, 'yellow')

    def motnoun(self):
        result = self.motivation_noun[r.randint(0, len(self.motivation_noun) - 1)]
        return colored(result, 'yellow')

    def generate(self):
        start = ""
        npc_mod = self.npcmod()
        temp = str(npc_mod)
        first = list(temp.lower())
        name = MName().New()
        if (first[5] == "a" or first[5] == "i" or first[5] == "u" or first[5] == "e" or first[5] == "o"):
            start = "An"
        else:
            start = "A"
        result = "{8} {0} {1} named {9}, {2} {3}, {4} {5} and {6} {7}.".format(
            npc_mod,
            self.npcnoun(),
            self.motverb(),
            self.motnoun(),
            self.motverb(),
            self.motnoun(),
            self.motverb(),
            self.motnoun(),
            start,
            colored(name, 'cyan')
        )
        return result

    def mood(self, input):
        mood = ''

        if(input == ''):
            temp = r.randint(1,7)
            if temp == 1:
                input = 'hated'
            elif temp == 2:
                input = 'hostile'
            elif temp == 3:
                input = 'distrustful'
            elif temp == 4:
                input = 'neutral'
            elif temp == 5:
                input = 'peaceful'
            elif temp == 6:
                input = 'friendly'
            elif temp == 7:
                input = 'loved'

        if input == '1':
            input = 'hated'
        elif input == '2':
            input = 'hostile'
        elif input == '3':
            input = 'distrustful'
        elif input == '4':
            input = 'neutral'
        elif input == '5':
            input = 'peaceful'
        elif input == '6':
            input = 'friendly'
        elif input == '7':
            input = 'loved'

        unpack = self.relationship[input]
        roll = r.randint(1, 100)
        for i in range(7):
            if(roll <= unpack[i].upper):
                if(i == 0):
                    mood = 'withdrawn'
                elif(i == 1):
                    mood = 'guarded'
                elif(i == 2):
                    mood = 'cautious'
                elif(i == 3):
                    mood = 'neutral'
                elif(i == 4):
                    mood = 'sociable'
                elif(i == 5):
                    mood = 'helpful'
                elif(i == 6):
                    mood = 'forthcoming'
                break

        return colored(mood, 'cyan')

    def convo(self, input):
        bearing = ''
        bearing_type = ''
        focus = ''

        if(input == ''):
            temp = r.randint(1,8)
            if temp == 1:
                input = 'scheming'
            elif temp == 2:
                input = 'insane'
            elif temp == 3:
                input = 'friendly'
            elif temp == 4:
                input = 'hostile'
            elif temp == 5:
                input = 'inquisitive'
            elif temp == 6:
                input = 'knowing'
            elif temp == 7:
                input = 'mysterious'
            elif temp == 8:
                input = 'prejudiced'

        if input == '1':
            input = 'scheming'
        elif input == '2':
            input = 'insane'
        elif input == '3':
            input = 'friendly'
        elif input == '4':
            input = 'hostile'
        elif input == '5':
            input = 'inquisitive'
        elif input == '6':
            input = 'knowing'
        elif input == '7':
            input = 'mysterious'
        elif input == '8':
            input = 'prejudiced'

        unpack = self.bearing[input]
        roll = r.randint(1, 100)
        for i in unpack:
            if(roll <= i.upper):
                bearing = i.description
                break

        bearing_type = input

        roll = r.randint(1, 100)
        for i in self.focus:
            if(roll <= i.upper):
                focus = i.description
                break

        result = '{}: {} ({}); {}: {}'.format(
            colored('NPC Demeanor', 'green'),
            bearing,
            bearing_type,
            colored('NPC Focus', 'yellow'),
            focus,
        )

        return result
